import h5py
import xml.etree.ElementTree as ET
import os
import numpy as np


# === HELPER FUNCTIONS ===

def read_slice_metadata(h5file_path):
    with h5py.File(h5file_path, 'r') as f:
        x = f['/mesh/coordsets/coords/values/x'][()]
        y = f['/mesh/coordsets/coords/values/y'][()]
        z = f['/mesh/coordsets/coords/values/z'][()]

    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    ux = np.unique(x)
    uy = np.unique(y)

    ni = len(ux)
    nj = len(uy)
    nk = 1

    dx = ux[1] - ux[0] if ni > 1 else 1.0
    dy = uy[1] - uy[0] if nj > 1 else 1.0
    dz = 1.0

    origin = [ux.min(), uy.min(), z[0]]
    spacing = [dx, dy, dz]
    dims = [ni, nj, nk]

    return dims, origin, spacing

def compute_extent_from_coords(h5file_path, global_origin, spacing):
    with h5py.File(h5file_path, 'r') as f:
        x = f['/mesh/coordsets/coords/values/x'][()]
        y = f['/mesh/coordsets/coords/values/y'][()]

    x = x.flatten()
    y = y.flatten()

    ux = np.unique(x)
    uy = np.unique(y)

    # convert points - cells (remove duplicated boundary)
    ni = len(ux) - 1
    nj = len(uy) - 1

    dx, dy, _ = spacing
    ox, oy, _ = global_origin

    i0 = int(round((ux.min() - ox) / dx))
    j0 = int(round((uy.min() - oy) / dy))

    return (i0, i0 + ni,
            j0, j0 + nj,
            0, 0)

# Compute full grid size (for WholeExtent), for global
def compute_whole_extent(all_extents):
    return [
        min(e[0] for e in all_extents),
        max(e[1] for e in all_extents),
        min(e[2] for e in all_extents),
        max(e[3] for e in all_extents),
        0, 0
    ]
    
# ================================ #
# ========= Main Program ========= #
# ================================ #

# === CONFIGURATION ===
rank_h5_files = sorted([f for f in os.listdir(".") if f.startswith("domain_") and f.endswith(".hdf5")])

print('rank_h5_files : ', rank_h5_files)

## pvti master file name
output_pvti = "pio.pvti"

## ghost path
ghost_path = '/mesh/fields/ascent_ghosts/values'

# === All ranks' extents, vti source ===
all_extents = []
all_sources = []

# all rank use the same spacing and origin basis, so find them in 1st rank
# _, global_origin, global_spacing = read_slice_metadata(rank_h5_files[0])
dims0, global_origin, global_spacing = read_slice_metadata(rank_h5_files[0])

for idx, h5file in enumerate(rank_h5_files):
    print("idx :", idx, "h5file :", h5file)

    extent = compute_extent_from_coords(
        h5file,
        global_origin,
        global_spacing
    )

    vti_filename = f"domain_{idx:0>6d}.vti"

    all_extents.append(extent)
    all_sources.append(vti_filename)

# === return the global extent ===
whole_extent = compute_whole_extent(all_extents)

# === Condtruct pvti Master File

# Create XML structure named pvti through f-string
# pvti = ET.Element("VTKFile", type="PImageData", version="0.1", byte_order="LittleEndian")
pvti = ET.Element("VTKFile", type="PImageData", version="0.1", byte_order="LittleEndian")

# PImageData element
pimg = ET.SubElement(
    pvti,
    "PImageData",
    WholeExtent=f"{whole_extent[0]} {whole_extent[1]} {whole_extent[2]} {whole_extent[3]} 0 0",
    Origin=f"{global_origin[0]} {global_origin[1]} {global_origin[2]}",
    Spacing=f"{global_spacing[0]} {global_spacing[1]} 1.0"
)

# Declare point data arrays, Scalars="u11" tells ParaView to treat u11 as the default scalar.
ppoint = ET.SubElement(pimg, "PPointData", Scalars="u11")

ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u11", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u12", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u13", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u21", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u22", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u23", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u31", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u32", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="u33", NumberOfComponents="1")

ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v11", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v12", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v13", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v21", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v22", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v23", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v31", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v32", NumberOfComponents="1")
ET.SubElement(ppoint, "PDataArray", type="Float64", Name="v33", NumberOfComponents="1")


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

    
