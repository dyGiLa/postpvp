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
gapA_path = "/mesh/fields/gapA/values"
u11_path = "/mesh/fields/u11Container/values"
u12_path = "/mesh/fields/u12Container/values"
u13_path = "/mesh/fields/u13Container/values"
u21_path = "/mesh/fields/u21Container/values"
u22_path = "/mesh/fields/u22Container/values"
u23_path = "/mesh/fields/u23Container/values"
u31_path = "/mesh/fields/u31Container/values"
u32_path = "/mesh/fields/u32Container/values"
u33_path = "/mesh/fields/u33Container/values"

v11_path = "/mesh/fields/v11Container/values"
v12_path = "/mesh/fields/v12Container/values"
v13_path = "/mesh/fields/v13Container/values"
v21_path = "/mesh/fields/v21Container/values"
v22_path = "/mesh/fields/v22Container/values"
v23_path = "/mesh/fields/v23Container/values"
v31_path = "/mesh/fields/v31Container/values"
v32_path = "/mesh/fields/v32Container/values"
v33_path = "/mesh/fields/v33Container/values"

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
    gapA_values = h5f[gapA_path][()].astype('float')
    u11_values = h5f[u11_path][()].astype('float')
    u12_values = h5f[u12_path][()].astype('float')
    u13_values = h5f[u13_path][()].astype('float')
    u21_values = h5f[u21_path][()].astype('float')
    u22_values = h5f[u22_path][()].astype('float')
    u23_values = h5f[u23_path][()].astype('float')
    u31_values = h5f[u31_path][()].astype('float')
    u32_values = h5f[u32_path][()].astype('float')
    u33_values = h5f[u33_path][()].astype('float')        
    v11_values = h5f[v11_path][()].astype('float')
    v12_values = h5f[v12_path][()].astype('float')
    v13_values = h5f[v13_path][()].astype('float')
    v21_values = h5f[v21_path][()].astype('float')
    v22_values = h5f[v22_path][()].astype('float')
    v23_values = h5f[v23_path][()].astype('float')
    v31_values = h5f[v31_path][()].astype('float')
    v32_values = h5f[v32_path][()].astype('float')
    v33_values = h5f[v33_path][()].astype('float')        

    

    # covert to vtk_array
    vtk_gapA_array = numpy_support.numpy_to_vtk(gapA_values)
    vtk_gapA_array.SetName("gapA")

    vtk_u11_array = numpy_support.numpy_to_vtk(u11_values)
    vtk_u11_array.SetName("u11")

    vtk_u12_array = numpy_support.numpy_to_vtk(u12_values)
    vtk_u12_array.SetName("u12")

    vtk_u13_array = numpy_support.numpy_to_vtk(u13_values)
    vtk_u13_array.SetName("u13")

    vtk_u21_array = numpy_support.numpy_to_vtk(u21_values)
    vtk_u21_array.SetName("u21")

    vtk_u22_array = numpy_support.numpy_to_vtk(u22_values)
    vtk_u22_array.SetName("u22")

    vtk_u23_array = numpy_support.numpy_to_vtk(u23_values)
    vtk_u23_array.SetName("u23")

    vtk_u31_array = numpy_support.numpy_to_vtk(u31_values)
    vtk_u31_array.SetName("u31")

    vtk_u32_array = numpy_support.numpy_to_vtk(u32_values)
    vtk_u32_array.SetName("u32")

    vtk_u33_array = numpy_support.numpy_to_vtk(u33_values)
    vtk_u33_array.SetName("u33")


    
    vtk_v11_array = numpy_support.numpy_to_vtk(v11_values)
    vtk_v11_array.SetName("v11")

    vtk_v12_array = numpy_support.numpy_to_vtk(v12_values)
    vtk_v12_array.SetName("v12")

    vtk_v13_array = numpy_support.numpy_to_vtk(v13_values)
    vtk_v13_array.SetName("v13")

    vtk_v21_array = numpy_support.numpy_to_vtk(v21_values)
    vtk_v21_array.SetName("v21")

    vtk_v22_array = numpy_support.numpy_to_vtk(v22_values)
    vtk_v22_array.SetName("v22")

    vtk_v23_array = numpy_support.numpy_to_vtk(v23_values)
    vtk_v23_array.SetName("v23")

    vtk_v31_array = numpy_support.numpy_to_vtk(v31_values)
    vtk_v31_array.SetName("v31")

    vtk_v32_array = numpy_support.numpy_to_vtk(v32_values)
    vtk_v32_array.SetName("v32")

    vtk_v33_array = numpy_support.numpy_to_vtk(v33_values)
    vtk_v33_array.SetName("v33")
    
    
    # Attach to image data
    pd = vtk_grid.GetPointData()

    pd.AddArray(vtk_gapA_array)

    pd.AddArray(vtk_u11_array)
    pd.AddArray(vtk_u12_array)
    pd.AddArray(vtk_u13_array)
    pd.AddArray(vtk_u21_array)
    pd.AddArray(vtk_u22_array)
    pd.AddArray(vtk_u23_array)
    pd.AddArray(vtk_u31_array)
    pd.AddArray(vtk_u32_array)
    pd.AddArray(vtk_u33_array)    

    pd.AddArray(vtk_v11_array)
    pd.AddArray(vtk_v12_array)
    pd.AddArray(vtk_v13_array)
    pd.AddArray(vtk_v21_array)
    pd.AddArray(vtk_v22_array)
    pd.AddArray(vtk_v23_array)
    pd.AddArray(vtk_v31_array)
    pd.AddArray(vtk_v32_array)
    pd.AddArray(vtk_v33_array)    
    

    # Optionally make one of them the default for visualization
    pd.SetScalars(vtk_gapA_array)
    
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
    
