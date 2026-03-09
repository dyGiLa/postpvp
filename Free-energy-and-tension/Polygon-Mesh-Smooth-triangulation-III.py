import trimesh
import open3d as o3d
import numpy as np

mesh = trimesh.load("~/Documents/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/RingCut-Surface-gapA-1stclip-O127.25-110-127.25-n-0.44--1-0_2ndclip-O127.25-154.535-127.25-n--0.5-1.37-0.ply", process=False)

#points, _ = trimesh.sample.sample_surface(mesh, 300000)
points, _ = trimesh.sample.sample_surface_even(mesh, 300000)


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Balanced normal estimation
pcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(
        radius=mesh.scale * 1.0,
        max_nn=80
    )
)
pcd.orient_normals_consistent_tangent_plane(500)

# ------------------------------------------------------------
# === AXIS-FREE POLE COMPLETION (NEW PART) ===
# ------------------------------------------------------------

# Convert to numpy
pts = np.asarray(pcd.points)
nrms = np.asarray(pcd.normals)

# ---------- Step 1: PCA to find principal direction ----------

V = mesh.vertices
V_centered = V - V.mean(axis=0)

_, _, vh = np.linalg.svd(V_centered, full_matrices=False)
principal_dir = vh[0]   # dominant elongation direction

# ---------- Step 2: find extremal regions along that direction ----------

proj = V_centered @ principal_dir
min_p, max_p = proj.min(), proj.max()

eps = 0.02 * (max_p - min_p)  # thickness of pole region

pole_masks = [
    proj < min_p + eps,
    proj > max_p - eps
]

# ---------- Helper functions for steps 3 & 4 ----------

def estimate_planar_frame(points):
    """
    Estimate center, normal, and tangent basis of a planar cap
    """
    center = points.mean(axis=0)
    P = points - center

    _, _, vh = np.linalg.svd(P, full_matrices=False)

    normal = vh[2]      # least variance direction
    t1 = vh[0]
    t2 = vh[1]

    return center, normal, t1, t2


def seed_planar_cap(center, normal, t1, t2, radius, n=2000):
    """
    Seed points in a local tangent plane disk
    """
    angles = np.random.rand(n) * 2.0 * np.pi
    r = radius * np.sqrt(np.random.rand(n))

    pts = (
        center
        + r[:, None] * np.cos(angles)[:, None] * t1
        + r[:, None] * np.sin(angles)[:, None] * t2
    )

    nrms = np.tile(normal, (n, 1))
    return pts, nrms


# ---------- Steps 3–5: detect planar caps and inject points ----------

for mask in pole_masks:
    pole_vertices = V[mask]

    # Skip if region is too small / noisy
    if pole_vertices.shape[0] < 50:
        continue

    center, normal, t1, t2 = estimate_planar_frame(pole_vertices)

    # Estimate cap radius from existing geometry
    radius = np.linalg.norm(pole_vertices - center, axis=1).max()

    # Seed synthetic points
    seed_pts, seed_nrms = seed_planar_cap(
        center=center,
        normal=normal,
        t1=t1,
        t2=t2,
        radius=radius,
        n=3000
    )

    pts = np.vstack([pts, seed_pts])
    nrms = np.vstack([nrms, seed_nrms])

# Write back to Open3D point cloud
pcd.points = o3d.utility.Vector3dVector(pts)
pcd.normals = o3d.utility.Vector3dVector(nrms)

# ------------------------------------------------------------
# Poisson reconstruction
# ------------------------------------------------------------

# Poisson reconstruction
recon, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
    pcd,
    depth=7,
    scale=1.1,
    linear_fit=True
)

# Crop
bbox = pcd.get_axis_aligned_bounding_box()
recon = recon.crop(bbox)

# Convert back
smooth_mesh = trimesh.Trimesh(
    vertices=np.asarray(recon.vertices),
    faces=np.asarray(recon.triangles),
    process=True
)


smooth_mesh.fix_normals()
print("Watertight:", smooth_mesh.is_watertight)


smooth_mesh.export("~/Documents/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/cells-surface-smooth.ply")
