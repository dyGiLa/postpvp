import h5py
import numpy as np
# import pyvista as pv

from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkCommonDataModel import vtkDataSetAttributes
from vtkmodules.vtkIOXML import vtkXMLImageDataWriter

from vtkmodules.util import numpy_support

import os


def read_slice_metadata(h5file_path):
    with h5py.File(h5file_path, 'r') as f:
        x = f['/mesh/coordsets/coords/values/x'][()]
        y = f['/mesh/coordsets/coords/values/y'][()]
        z = f['/mesh/coordsets/coords/values/z'][()]
        ghost_array = f['/mesh/fields/ascent_ghosts/values'][()].astype(np.uint8)

    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    # unique coordinates
    ux = np.unique(x)
    uy = np.unique(y)

    ni = len(ux)
    nj = len(uy)
    nk = 1  # slice

    # spacing
    dx = ux[1] - ux[0] if ni > 1 else 1.0
    dy = uy[1] - uy[0] if nj > 1 else 1.0
    dz = 1.0  # arbitrary (since nk=1)

    # origin
    origin = [ux.min(), uy.min(), z[0]]

    dims = [ni, nj, nk]
    spacing = [dx, dy, dz]

    print("dims:", dims)
    print("origin:", origin)
    print("spacing:", spacing)

    return dims, origin, spacing, ghost_array

def compute_extent_from_coords(h5file_path, global_origin, spacing):
    with h5py.File(h5file_path, 'r') as f:
        x = f['/mesh/coordsets/coords/values/x'][()]
        y = f['/mesh/coordsets/coords/values/y'][()]

    x = x.flatten()
    y = y.flatten()

    ux = np.unique(x)
    uy = np.unique(y)

    dx, dy, _ = spacing
    ox, oy, _ = global_origin

    # starting index in global grid
    i0 = int(round((ux.min() - ox) / dx))
    j0 = int(round((uy.min() - oy) / dy))

    # number of points → extent end index
    ni = len(ux)
    nj = len(uy)

    return (i0, i0 + ni - 1,
            j0, j0 + nj - 1,
            0, 0)

# Compute full grid size (for WholeExtent), for global
def compute_whole_extent(all_extents):
    min_i = min(e[0] for e in all_extents)
    max_i = max(e[1] for e in all_extents)
    min_j = min(e[2] for e in all_extents)
    max_j = max(e[3] for e in all_extents)
    min_k = min(e[4] for e in all_extents)
    max_k = max(e[5] for e in all_extents)
    
    return (min_i, max_i, min_j, max_j, min_k, max_k)

# Convert field array in to C-style array
def CStyle_array_conversion(ni, nj, values_arr):
    # reshape to (ni, nj)
    values_arr_2d = values_arr.reshape(ni, nj)
    # transpose → (nj, ni)
    values_arr_2d = values_arr_2d.T
    # flatten in C-order
    values_arr_CStyle = values_arr_2d.flatten(order='C')
    vtk_values_array = numpy_support.numpy_to_vtk(values_arr_CStyle)

    return vtk_values_array



# === CONFIGURATION ===
rank_h5_files = sorted([f for f in os.listdir(".") if f.startswith("domain_") and f.endswith(".hdf5")])
print("rank_h5_files : ", rank_h5_files)

## fields path
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

_, global_origin, global_spacing, _ = read_slice_metadata(rank_h5_files[0])

for idx, h5file in enumerate(rank_h5_files):
    print("idx :", idx, "h5file :", h5file)

    rank_extent = compute_extent_from_coords(
        h5file,
        global_origin,
        global_spacing
    )
    
    # domain extents list
    all_extents.append(rank_extent)

WholeExtent = compute_whole_extent(all_extents)
print("WholeExtent : ", WholeExtent)

    
# === Loop Over all Rank HDF5 file ===
for idx, rankhdf5 in enumerate(rank_h5_files):
    
    dims, origin, spacing, _ = read_slice_metadata(rankhdf5)

    # rank extent
    rank_extent = compute_extent_from_coords(
        rankhdf5,
        global_origin,
        global_spacing
    )

    # all_extents.append(extent)

    print("rank_extent : ", rank_extent)

    # extent of h5file in current rank
    # local_extent = compute_extent(dims, origin, spacing)

    # Create a VTK image data object
    vtk_grid = vtkImageData()

    # Set dimensions (local extent)
    vtk_grid.SetExtent(*rank_extent)  # e.g., [i0, i1, j0, j1, k0, k1]

    # Optionally, set spacing and origin
    # vtk_grid.SetSpacing(*spacing)
    # Force z-thickness to behave nicely in ParaView:
    vtk_grid.SetSpacing(spacing[0], spacing[1], 1.0)
    vtk_grid.SetOrigin(*origin)

    # If using in parallel or multi-block, set the WHOLE extent
    # Whole extent refers to the global data extent across all ranks
    # vtk_grid.SetWholeExtent(WholeExtent)  # e.g., [0, ni-1, 0, nj-1, 0, nk-1]
    
    h5f = h5py.File(rankhdf5, 'r')
    
    # field data, numpy array
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
    ni, nj, _ = dims

    vtk_u11_array = CStyle_array_conversion(ni, nj, u11_values)
    vtk_u11_array.SetName("u11")
    vtk_u12_array = CStyle_array_conversion(ni, nj, u12_values)
    vtk_u12_array.SetName("u12")
    vtk_u13_array = CStyle_array_conversion(ni, nj, u13_values)
    vtk_u13_array.SetName("u13")

    vtk_u21_array = CStyle_array_conversion(ni, nj, u21_values)
    vtk_u21_array.SetName("u21")
    vtk_u22_array = CStyle_array_conversion(ni, nj, u22_values)
    vtk_u22_array.SetName("u22")
    vtk_u23_array = CStyle_array_conversion(ni, nj, u23_values)
    vtk_u23_array.SetName("u23")

    vtk_u31_array = CStyle_array_conversion(ni, nj, u31_values)
    vtk_u31_array.SetName("u31")
    vtk_u32_array = CStyle_array_conversion(ni, nj, u32_values)
    vtk_u32_array.SetName("u32")
    vtk_u33_array = CStyle_array_conversion(ni, nj, u33_values)
    vtk_u33_array.SetName("u33")

    vtk_v11_array = CStyle_array_conversion(ni, nj, v11_values)
    vtk_v11_array.SetName("v11")
    vtk_v12_array = CStyle_array_conversion(ni, nj, v12_values)
    vtk_v12_array.SetName("v12")
    vtk_v13_array = CStyle_array_conversion(ni, nj, v13_values)
    vtk_v13_array.SetName("v13")

    vtk_v21_array = CStyle_array_conversion(ni, nj, v21_values)
    vtk_v21_array.SetName("v21")
    vtk_v22_array = CStyle_array_conversion(ni, nj, v22_values)
    vtk_v22_array.SetName("v22")
    vtk_v23_array = CStyle_array_conversion(ni, nj, v23_values)
    vtk_v23_array.SetName("v23")

    vtk_v31_array = CStyle_array_conversion(ni, nj, v31_values)
    vtk_v31_array.SetName("v31")
    vtk_v32_array = CStyle_array_conversion(ni, nj, v32_values)
    vtk_v32_array.SetName("v32")
    vtk_v33_array = CStyle_array_conversion(ni, nj, v33_values)
    vtk_v33_array.SetName("v33")

    
    # # reshape to (ni, nj)
    # GPhi1_2d = GPhi1_values.reshape(ni, nj)
    # # transpose → (nj, ni)
    # GPhi1_2d = GPhi1_2d.T
    # # flatten in C-order
    # GPhi1_fixed = GPhi1_2d.flatten(order='C')
    # vtk_GPhi1_array = numpy_support.numpy_to_vtk(GPhi1_fixed)    
    # # vtk_GPhi1_array = numpy_support.numpy_to_vtk(GPhi1_values)
    # vtk_GPhi1_array.SetName("GradPhi1")
    
    # Attach to image data
    pd = vtk_grid.GetPointData()

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
    pd.SetScalars(vtk_u11_array)
    
    # =====================

    # load ghost cell mask array
    ghost_cell_array = h5f[ghost_path][()].astype(np.uint8)
    print("ghost shape:", ghost_cell_array.shape)
    # === Ghost cell consistency check (for 2D slice) ===
    ni, nj, nk = dims
    expected_cells = (ni - 1) * (nj - 1)

    print("Ghost raw size:", ghost_cell_array.size)
    print("Expected :", expected_cells)

    if ghost_cell_array.size == expected_cells:
        ghost_cell_array_final = ghost_cell_array

    elif ghost_cell_array.size == 2 * expected_cells:
        print("Detected interleaved 2-component ghost array")
        ghost_cell_array_final = ghost_cell_array.reshape(expected_cells, 2)[:, 0]

    else:
        raise RuntimeError("Unexpected ghost array layout")

    # reshape to cell grid
    ghost_2d = ghost_cell_array_final.reshape(ni-1, nj-1)
    # # transpose
    ghost_2d = ghost_2d.T
    # # flatten
    ghost_fixed = ghost_2d.flatten(order='C')
    ghost_vtk_array = numpy_support.numpy_to_vtk(ghost_fixed)    
    
    # ---- Wrap ghost array into VTK array ----
    # ghost_vtk_array = numpy_support.numpy_to_vtk(ghost_cell_array)
    # ghost_vtk_array = numpy_support.numpy_to_vtk(ghost_cell_array_final)    
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
    
