import trimesh
import open3d as o3d
import numpy as np

# Load ParaView surface
mesh = trimesh.load("~/Documents/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/RingCut-Surface-gapA-1stclip-O127.25-110-127.25-n-0.44--1-0_2ndclip-O127.25-154.535-127.25-n--0.5-1.37-0.ply", process=False)

# Sample points on the surface
points, _ = trimesh.sample.sample_surface(mesh, 200000)

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Estimate normals
pcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(
        radius=mesh.scale * 2.0,
        max_nn=30
    )
)
pcd.orient_normals_consistent_tangent_plane(100)

# Poisson surface reconstruction
recon, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
    pcd, depth=6,
    scale=1.1,
    linear_fit=True
)

# Density trimming
densities = np.asarray(densities)
recon.remove_vertices_by_mask(densities < np.percentile(densities, 10))

# Crop to original bounding box
bbox = pcd.get_axis_aligned_bounding_box()
recon = recon.crop(bbox)

# Convert back to Trimesh
vertices = np.asarray(recon.vertices)
faces = np.asarray(recon.triangles)
smooth_mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

# Final normal fix
smooth_mesh.fix_normals()

# Save
smooth_mesh.export("~/Documents/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/cells-surface-smooth.ply")
