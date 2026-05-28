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
js11_path = "/mesh/fields/js11Container/values"
js12_path = "/mesh/fields/js12Container/values"
js13_path = "/mesh/fields/js13Container/values"
js21_path = "/mesh/fields/js21Container/values"
js22_path = "/mesh/fields/js22Container/values"
js23_path = "/mesh/fields/js23Container/values"
js31_path = "/mesh/fields/js31Container/values"
js32_path = "/mesh/fields/js32Container/values"
js33_path = "/mesh/fields/js33Container/values"

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
    js11_values = h5f[js11_path][()].astype('float')
    js12_values = h5f[js12_path][()].astype('float')
    js13_values = h5f[js13_path][()].astype('float')        
    js21_values = h5f[js21_path][()].astype('float')
    js22_values = h5f[js22_path][()].astype('float')
    js23_values = h5f[js23_path][()].astype('float')        
    js31_values = h5f[js31_path][()].astype('float')
    js32_values = h5f[js32_path][()].astype('float')
    js33_values = h5f[js33_path][()].astype('float')        
        
    # covert to vtk_array
    ni, nj, _ = dims

    vtk_js11_array = CStyle_array_conversion(ni, nj, js11_values)
    vtk_js11_array.SetName("js11")
    vtk_js12_array = CStyle_array_conversion(ni, nj, js12_values)
    vtk_js12_array.SetName("js12")
    vtk_js13_array = CStyle_array_conversion(ni, nj, js13_values)
    vtk_js13_array.SetName("js13")

    vtk_js21_array = CStyle_array_conversion(ni, nj, js21_values)
    vtk_js21_array.SetName("js21")
    vtk_js22_array = CStyle_array_conversion(ni, nj, js22_values)
    vtk_js22_array.SetName("js22")
    vtk_js23_array = CStyle_array_conversion(ni, nj, js23_values)
    vtk_js23_array.SetName("js23")

    vtk_js31_array = CStyle_array_conversion(ni, nj, js31_values)
    vtk_js31_array.SetName("js31")
    vtk_js32_array = CStyle_array_conversion(ni, nj, js32_values)
    vtk_js32_array.SetName("js32")
    vtk_js33_array = CStyle_array_conversion(ni, nj, js33_values)
    vtk_js33_array.SetName("js33")
        
    # Attach to image data
    pd = vtk_grid.GetPointData()

    pd.AddArray(vtk_js11_array)
    pd.AddArray(vtk_js12_array)
    pd.AddArray(vtk_js13_array)    
    pd.AddArray(vtk_js21_array)
    pd.AddArray(vtk_js22_array)
    pd.AddArray(vtk_js23_array)    
    pd.AddArray(vtk_js31_array)
    pd.AddArray(vtk_js32_array)
    pd.AddArray(vtk_js33_array)    

    # Optionally make one of them the default for visualization
    pd.SetScalars(vtk_js11_array)
    
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
    
