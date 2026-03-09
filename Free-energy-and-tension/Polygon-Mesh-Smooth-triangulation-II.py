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
        radius=mesh.scale * 3.0,
        max_nn=80
    )
)
pcd.orient_normals_consistent_tangent_plane(500)

# Poisson reconstruction
recon, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
    pcd,
    depth=7,
    scale=1.1,
    linear_fit=True
)

# Gentle density trimming
# densities = np.asarray(densities)
# low = densities.mean() - 1.5 * densities.std()
# #low = np.percentile(densities, 2)
# recon.remove_vertices_by_mask(densities < low)

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
