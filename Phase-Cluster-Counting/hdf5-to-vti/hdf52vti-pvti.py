import h5py
import xml.etree.ElementTree as ET
import os
import numpy as np


# === HELPER FUNCTIONS ===

def read_rank_metadata(h5file_path):
    """Reads dimension, origin, spacing and ghost array presence from HDF5."""
    with h5py.File(h5file_path, 'r') as f:

        # Grid metadata, int convert number to int type
        ni = f[dims_i][()][0].astype(np.int64)
        nj = f[dims_j][()][0].astype(np.int64)
        nk = f[dims_k][()][0].astype(np.int64)

        dx = f[spa_dx][()][0].astype(np.float32)
        dy = f[spa_dy][()][0].astype(np.float32)
        dz = f[spa_dz][()][0].astype(np.float32)

        ox = f[ori_x][()][0].astype(np.float32)
        oy = f[ori_y][()][0].astype(np.float32)
        oz = f[ori_z][()][0].astype(np.float32)
                
        ghost_array = f['/mesh/fields/ascent_ghosts/values'][()].astype(np.float32)

        dims = [ni, nj, nk]
        origin = [ox, oy, oz]
        spacing = [dx, dy, dz]

        print("dims : ", dims)
        print("origin : ", origin)
        print("spacing : ", spacing)
        print("ghost_array : ", ghost_array)                
    
    return dims, origin, spacing, ghost_array

def compute_extent(dims, origin, spacing):    
    """Computes the voxel extent of a block (i.e., in IJK space)."""
    x0, y0, z0 = origin    
    ni, nj, nk = dims
    dx, dy, dz = spacing

    io = (x0/dx).astype(np.int64)
    jo = (y0/dy).astype(np.int64)
    ko = (z0/dz).astype(np.int64)    
       
    # return (x0, x0 + ((ni - 1) * dx), y0, y0 + ((nj - 1) * dy), z0, z0 + ((nk - 1) * dz))  
    return (io, io + (ni - 1), jo, jo + (nj - 1), ko, ko + (nk - 1))  # Local extent in IJK

# Compute full grid size (for WholeExtent), for global
def compute_whole_extent(all_extents):
    min_i = min(e[0] for e in all_extents)
    max_i = max(e[1] for e in all_extents)
    min_j = min(e[2] for e in all_extents)
    max_j = max(e[3] for e in all_extents)
    min_k = min(e[4] for e in all_extents)
    max_k = max(e[5] for e in all_extents)
    
    return [min_i, max_i, min_j, max_j, min_k, max_k]

    
# ================================ #
# ========= Main Program ========= #
# ================================ #

# === CONFIGURATION ===
rank_h5_files = sorted([f for f in os.listdir(".") if f.startswith("domain_") and f.endswith(".hdf5")])

print('rank_h5_files : ', rank_h5_files)

## pvti master file name
output_pvti = "pio.pvti"

## coordset pathes
dims_i = '/mesh/coordsets/coords/dims/i'
dims_j = '/mesh/coordsets/coords/dims/j'
dims_k = '/mesh/coordsets/coords/dims/k'

## spaceing pathes
spa_dx = '/mesh/coordsets/coords/spacing/dx'
spa_dy = '/mesh/coordsets/coords/spacing/dy'
spa_dz = '/mesh/coordsets/coords/spacing/dz'

## origin pathes
ori_x = '/mesh/coordsets/coords/origin/x'
ori_y = '/mesh/coordsets/coords/origin/y'
ori_z = '/mesh/coordsets/coords/origin/z'

## ghost path
ghost_path = '/mesh/fields/ascent_ghosts/values'

# === All ranks' extents, vti source ===
all_extents = []
all_sources = []

for idx, h5file in enumerate(rank_h5_files):
    print("idx :", idx, "h5file :", h5file)

    # return dims, origin, spacing list and np.array of ghost cell
    dims, origin, spacing, ghost_array = read_rank_metadata(h5file)

    # extent of h5file in current rank
    extent = compute_extent(dims, origin, spacing)

    # vti file should already exist per your workflow
    vti_filename = f"domain_{idx:0>6d}.vti"  

    # domain extents list
    all_extents.append(extent)

    # domain_000xxx.vti files list
    all_sources.append(vti_filename)


# === return the global extent ===
whole_extent = compute_whole_extent(all_extents)

# all rank use the same spacing and origin basis, so find them in 1st rank
_, global_origin, global_spacing, _ = read_rank_metadata(rank_h5_files[0])


# === Condtruct pvti Master File

# Create XML structure called pvti through f-string
pvti = ET.Element("VTKFile", type="PImageData", version="0.1", byte_order="LittleEndian")

# PImageData element
pimg = ET.SubElement(pvti, "PImageData",
                     WholeExtent=f"{whole_extent[0]} {whole_extent[1]} {whole_extent[2]} {whole_extent[3]} {whole_extent[4]} {whole_extent[5]}",
                     Origin=f"{global_origin[0]} {global_origin[1]} {global_origin[2]}",
                     Spacing=f"{global_spacing[0]} {global_spacing[1]} {global_spacing[2]}")

# Declare point data arrays, Scalars="phaseMarker" tells ParaView to treat phaseMarker as the default scalar.
ppoint = ET.SubElement(pimg, "PPointData", Scalars="phaseMarker")

ET.SubElement(ppoint, "PDataArray", type="Float64", Name="phaseMarker", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="gapA", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="feDensity", NumberOfComponents="1")


# ghost cell element
cell_data = ET.SubElement(pimg, "PCellData")
ET.SubElement(cell_data, "PDataArray",type="UInt8",Name="vtkGhostType",NumberOfComponents="1")

# Add each ranks' Piece element
for extent, source in zip(all_extents, all_sources):
    ext_str = f"{extent[0]} {extent[1]} {extent[2]} {extent[3]} {extent[4]} {extent[5]}"
    ET.SubElement(pimg, "Piece", Extent=ext_str, Source=source)

    
# === WRITE .pvti FILE ===

tree = ET.ElementTree(pvti)

ET.indent(tree, space="  ")

with open(output_pvti, "wb") as f:
    tree.write(f)

    
