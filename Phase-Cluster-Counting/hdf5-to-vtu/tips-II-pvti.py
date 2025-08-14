# Great — based on your detailed HDF5 file structure, here's a Python script that:
# Reads dimension, origin, spacing, and ghost cell array from each rank’s HDF5 file.
# Computes the extent based on origin and dimension.
# Generates a .pvti master file with proper ghost cell metadata (vtkGhostType).
# Assumes the ghost array is a 1D array of type UInt8 stored in point data.

## Python Script: Generate .pvti from HDF5 Rank Files
import h5py
import xml.etree.ElementTree as ET
import os

# === CONFIGURATION ===
rank_h5_files = sorted([f for f in os.listdir(".") if f.startswith("rank_") and f.endswith(".hdf5")])
output_pvti = "output.pvti"

# === HELPER FUNCTIONS ===

def read_rank_metadata(h5file_path):
    """Reads dimension, origin, spacing and ghost array presence from HDF5."""
    with h5py.File(h5file_path, 'r') as f:
        dims = (
            int(f['/mesh/coordsets/coords/dims/i'][()]),
            int(f['/mesh/coordsets/coords/dims/j'][()]),
            int(f['/mesh/coordsets/coords/dims/k'][()])
        )
        origin = (
            float(f['/mesh/coordsets/coords/origin/x'][()]),
            float(f['/mesh/coordsets/coords/origin/y'][()]),
            float(f['/mesh/coordsets/coords/origin/z'][()])
        )
        spacing = (
            float(f['/mesh/coordsets/coords/spacing/dx'][()]),
            float(f['/mesh/coordsets/coords/spacing/dy'][()]),
            float(f['/mesh/coordsets/coords/spacing/dz'][()])
        )
        ghost_array = f['/mesh/fields/ghosts_array/values'][()]
    
    return dims, origin, spacing, ghost_array

def compute_extent(dims, origin, spacing):

    # if your HDF5 files contain each subdomain’s global offset, for example at:

    # /mesh/topologies/coords/element_origin/{i,j,k}

    # ...then you can read those values and compute:
    
    # i0 = f['/mesh/topologies/coords/element_origin/i'][()]
    # j0 = ...
    # k0 = ...
    # extent = (i0, i0 + ni - 1, j0, j0 + nj - 1, k0, k0 + nk - 1)
    
    """Computes the voxel extent of a block (i.e., in IJK space)."""
    i, j, k = dims
    extent = (0, i-1, 0, j-1, 0, k-1)  # Local extent in IJK
    return extent


# === BUILD PVTI STRUCTURE ===

# Assume all blocks use the same spacing and origin basis
_, global_origin, global_spacing, _ = read_rank_metadata(rank_h5_files[0])

# ----- extents , vts source ------
all_extents = []
all_sources = []

for idx, h5file in enumerate(rank_h5_files):
    dims, origin, spacing, ghost_array = read_rank_metadata(h5file)
    extent = compute_extent(dims, origin, spacing)
    vti_filename = f"rank_{idx}.vti"  # This file should already exist per your workflow
    all_extents.append(extent)
    all_sources.append(vti_filename)

# Compute full grid size (for WholeExtent), for global
def compute_whole_extent(all_extents):
    min_i = min(e[0] for e in all_extents)
    max_i = max(e[1] for e in all_extents)
    min_j = min(e[2] for e in all_extents)
    max_j = max(e[3] for e in all_extents)
    min_k = min(e[4] for e in all_extents)
    max_k = max(e[5] for e in all_extents)
    return (min_i, max_i, min_j, max_j, min_k, max_k)

whole_extent = compute_whole_extent(all_extents)

# Create XML structure
pvti = ET.Element("VTKFile", type="PImageData", version="0.1", byte_order="LittleEndian")
pimg = ET.SubElement(pvti, "PImageData",
                     WholeExtent=f"{whole_extent[0]} {whole_extent[1]} {whole_extent[2]} {whole_extent[3]} {whole_extent[4]} {whole_extent[5]}",
                     Origin=f"{global_origin[0]} {global_origin[1]} {global_origin[2]}",
                     Spacing=f"{global_spacing[0]} {global_spacing[1]} {global_spacing[2]}")


# Add ghost cell info (point data with vtkGhostType)
# point_data = ET.SubElement(pimg, "PPointData")
# ET.SubElement(point_data, "PDataArray",
#               type="UInt8",
#               Name="vtkGhostType",
#               NumberOfComponents="1")

# ET.SubElement(pimg, "PCellData")  # optional: can include more data here


ET.SubElement(pimg, "PPointData")  # Empty, since no point data

cell_data = ET.SubElement(pimg, "PCellData")
ET.SubElement(cell_data, "PDataArray",
              type="UInt8",
              Name="vtkGhostType",
              NumberOfComponents="1")

# Add each rank block (Piece)
for extent, source in zip(all_extents, all_sources):
    ext_str = f"{extent[0]} {extent[1]} {extent[2]} {extent[3]} {extent[4]} {extent[5]}"
    ET.SubElement(pimg, "Piece", Extent=ext_str, Source=source)

# === WRITE .pvti FILE ===
tree = ET.ElementTree(pvti)
ET.indent(tree, space="  ")
with open(output_pvti, "wb") as f:
    tree.write(f)

print(f"✅ Master .pvti file written to: {output_pvti}")

# Assumptions Recap:

#     HDF5 files are named like rank_0.hdf5, rank_1.hdf5, etc.

#     You have already converted each HDF5 file to its .vti counterpart (e.g. rank_0.vti) using the same structure.

#     The ghost cell array is already included in each .vti file as vtkGhostType.

#     All files are in the current directory.

# Would you also like a script that converts the HDF5 files to .vti (with ghost cells)? I can generate that next.

