import h5py
import numpy as np
# import pyvista as pv

from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkCommonDataModel import vtkDataSetAttributes
from vtkmodules.vtkIOXML import vtkXMLImageDataWriter

from vtkmodules.util import numpy_support

import os


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
    return [io, io + (ni - 1), jo, jo + (nj - 1), ko, ko + (nk - 1)]  # Local extent in IJK

# Compute full grid size (for WholeExtent), for global
def compute_whole_extent(all_extents):
    min_i = min(e[0] for e in all_extents)
    max_i = max(e[1] for e in all_extents)
    min_j = min(e[2] for e in all_extents)
    max_j = max(e[3] for e in all_extents)
    min_k = min(e[4] for e in all_extents)
    max_k = max(e[5] for e in all_extents)
    
    return (min_i, max_i, min_j, max_j, min_k, max_k)




# === CONFIGURATION ===
rank_h5_files = sorted([f for f in os.listdir(".") if f.startswith("domain_") and f.endswith(".hdf5")])
print("rank_h5_files : ", rank_h5_files)

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

## fields path
pMarker_path = "/mesh/fields/phaseMarker/values"
gapA_path = "/mesh/fields/gapA/values"
feDensity_path = "/mesh/fields/feDensity/values"

## ghost path
ghost_path = '/mesh/fields/ascent_ghosts/values'

# === Loop For cook up all_extents
all_extents = []

for idx, h5file in enumerate(rank_h5_files):
    print("idx :", idx, "h5file :", h5file)

    # return dims, origin, spacing list and np.array of ghost cell
    dims, origin, spacing, ghost_array = read_rank_metadata(h5file)

    # extent of h5file in current rank
    extent = compute_extent(dims, origin, spacing)

    # domain extents list
    all_extents.append(extent)

WholeExtent = compute_whole_extent(all_extents)
print("WholeExtent : ", WholeExtent)

    
# === Loop Over all Rank HDF5 file ===
for idx, rankhdf5 in enumerate(rank_h5_files):
    
    dims, origin, spacing, _ = read_rank_metadata(rankhdf5)

    # rank extent
    rank_extent = compute_extent(dims, origin, spacing)
    # all_extents.append(extent)

    print("rank_extent : ", rank_extent)

    # extent of h5file in current rank
    # local_extent = compute_extent(dims, origin, spacing)

    # Create a VTK image data object
    vtk_grid = vtkImageData()

    # Set dimensions (local extent)
    vtk_grid.SetExtent(*rank_extent)  # e.g., [i0, i1, j0, j1, k0, k1]

    # Optionally, set spacing and origin
    vtk_grid.SetSpacing(*spacing)
    vtk_grid.SetOrigin(*origin)

    # If using in parallel or multi-block, set the WHOLE extent
    # Whole extent refers to the global data extent across all ranks
    # vtk_grid.SetWholeExtent(WholeExtent)  # e.g., [0, ni-1, 0, nj-1, 0, nk-1]
    
    h5f = h5py.File(rankhdf5, 'r')
    
    # field data, numpy array
    phaseMarker_values = h5f[pMarker_path][()].astype('float')
    gapA_values = h5f[gapA_path][()].astype('float')
    feDensity_values = h5f[feDensity_path][()].astype('float')

    # covert to vtk_array
    vtk_phaseMarker_array = numpy_support.numpy_to_vtk(phaseMarker_values)
    vtk_phaseMarker_array.SetName("phaseMarker")

    vtk_gapA_array = numpy_support.numpy_to_vtk(gapA_values)
    vtk_gapA_array.SetName("gapA")
    
    vtk_feDensity_array = numpy_support.numpy_to_vtk(feDensity_values)
    vtk_feDensity_array.SetName("feDensity")

    # Attach to image data
    pd = vtk_grid.GetPointData()

    pd.AddArray(vtk_phaseMarker_array)
    pd.AddArray(vtk_gapA_array)
    pd.AddArray(vtk_feDensity_array)

    # Optionally make one of them the default for visualization
    pd.SetScalars(vtk_phaseMarker_array)
    
    # =====================

    # load ghost cell mask array
    ghost_cell_array = h5f[ghost_path][()].astype(np.uint8)

    # ---- Wrap ghost array into VTK array ----
    ghost_vtk_array = numpy_support.numpy_to_vtk(ghost_cell_array)
    ghost_vtk_array.SetName(vtkDataSetAttributes.GhostArrayName())  # "vtkGhostType"
    ghost_vtk_array.SetNumberOfComponents(1)

    vtk_grid.GetCellData().AddArray(ghost_vtk_array)
    
    # ---- Write to .vti file ----

    # vti file name
    vti_filename = f"domain_{idx:0>6d}.vti"  
    
    writer = vtkXMLImageDataWriter()
    writer.SetFileName(vti_filename)
    writer.SetInputData(vtk_grid)
    writer.Write()
    
