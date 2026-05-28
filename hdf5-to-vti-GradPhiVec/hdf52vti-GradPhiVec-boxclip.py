import os
import h5py
import numpy as np

from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkUnstructuredGrid,
    vtkHexahedron,
    vtkTetra,
    vtkWedge,
    vtkPyramid,
    vtkQuad,
    vtkTriangle,
    vtkLine,
    vtkVertex,
    vtkDataSetAttributes
)

from vtkmodules.vtkIOXML import vtkXMLUnstructuredGridWriter
from vtkmodules.util import numpy_support


# ============================================================
# CONFIGURATION
# ============================================================

rank_h5_files = sorted([
    f for f in os.listdir(".")
    if f.startswith("domain_")
    and f.endswith(".hdf5")
])

print("rank_h5_files :", rank_h5_files)

# ------------------------------------------------------------
# Coordinate paths
# ------------------------------------------------------------

x_path = "/mesh/coordsets/coords/values/x"
y_path = "/mesh/coordsets/coords/values/y"
z_path = "/mesh/coordsets/coords/values/z"

# ------------------------------------------------------------
# Topology paths
# ------------------------------------------------------------

topo_base = "/mesh/topologies/topo/elements"

connectivity_path = f"{topo_base}/connectivity"
offsets_path      = f"{topo_base}/offsets"
sizes_path        = f"{topo_base}/sizes"
shapes_path       = f"{topo_base}/shapes"

shape_path = "/mesh/topologies/topo/elements/shape"
type_path  = "/mesh/topologies/topo/type"

shape_map_base = "/mesh/topologies/topo/elements/shape_map"

# ------------------------------------------------------------
# Field paths
# ------------------------------------------------------------

GPhi1_path = "/mesh/fields/GPhi1/values"
GPhi2_path = "/mesh/fields/GPhi2/values"
GPhi3_path = "/mesh/fields/GPhi3/values"

ghost_path = "/mesh/fields/ascent_ghosts/values"


# ============================================================
# Decode conduit-style string arrays
# ============================================================

def decode_hdf5_string(arr):

    return ''.join(
        s.decode() for s in arr
    ).strip('\x00')


# ============================================================
# Build VTK cell object from shape name
# ============================================================

def create_vtk_cell(shape_name):

    if shape_name == "hex":
        return vtkHexahedron()

    elif shape_name == "tet":
        return vtkTetra()

    elif shape_name == "wedge":
        return vtkWedge()

    elif shape_name == "pyramid":
        return vtkPyramid()

    elif shape_name == "quad":
        return vtkQuad()

    elif shape_name == "tri":
        return vtkTriangle()

    elif shape_name == "line":
        return vtkLine()

    elif shape_name == "point":
        return vtkVertex()

    else:
        raise RuntimeError(
            f"Unsupported cell type: {shape_name}"
        )


# ============================================================
# MAIN LOOP
# ============================================================

for idx, rankhdf5 in enumerate(rank_h5_files):

    print()
    print("================================================")
    print("Processing :", rankhdf5)
    print("================================================")

    with h5py.File(rankhdf5, 'r') as h5f:

        # ====================================================
        # Read topology metadata
        # ====================================================

        topo_type = decode_hdf5_string(
            h5f[type_path][()]
        )

        shape_mode = decode_hdf5_string(
            h5f[shape_path][()]
        )

        print("Topology Type :", topo_type)
        print("Shape Mode    :", shape_mode)

        if topo_type != "unstructured":

            raise RuntimeError(
                f"Unsupported topology type: {topo_type}"
            )

        # ====================================================
        # Read coordinates
        # ====================================================

        x = h5f[x_path][()].astype(np.float64)
        y = h5f[y_path][()].astype(np.float64)
        z = h5f[z_path][()].astype(np.float64)

        npoints = x.size

        print("Number of points :", npoints)

        points_np = np.column_stack((x, y, z))

        vtk_points = vtkPoints()

        vtk_points.SetData(
            numpy_support.numpy_to_vtk(
                points_np,
                deep=True
            )
        )

        # ====================================================
        # Create grid
        # ====================================================

        vtk_grid = vtkUnstructuredGrid()

        vtk_grid.SetPoints(vtk_points)

        # ====================================================
        # Uniform HEX mesh
        # ====================================================

        if shape_mode == "hex":

            connectivity = h5f[
                connectivity_path
            ][()].astype(np.int64)

            nodes_per_cell = 8

            ncells = connectivity.size // nodes_per_cell

            conn = connectivity.reshape(
                (ncells, nodes_per_cell)
            )

            for cell_conn in conn:

                cell = vtkHexahedron()

                vtk_hex_order = [0, 1, 3, 2, 4, 5, 7, 6]

                for i in range(8):

                    cell.GetPointIds().SetId(
                        i,
                        int(cell_conn[vtk_hex_order[i]])
                    )                

                vtk_grid.InsertNextCell(
                    cell.GetCellType(),
                    cell.GetPointIds()
                )

        # ====================================================
        # MIXED TOPOLOGY
        # ====================================================

        elif shape_mode == "mixed":

            connectivity = h5f[
                connectivity_path
            ][()].astype(np.int64)

            offsets = h5f[
                offsets_path
            ][()].astype(np.int64)

            sizes = h5f[
                sizes_path
            ][()].astype(np.int64)

            shapes = h5f[
                shapes_path
            ][()].astype(np.int64)

            print("Connectivity size :", connectivity.size)
            print("Number of cells   :", shapes.size)

            # ------------------------------------------------
            # Build reverse shape map
            # ------------------------------------------------

            shape_map = {}

            shape_map_group = h5f[shape_map_base]

            for key in shape_map_group.keys():

                #value = int(shape_map_group[key][()])
                value = int(np.array(shape_map_group[key][()]).flatten()[0])

                shape_map[value] = key

            print("Shape map :", shape_map)

            # ------------------------------------------------
            # Build cells
            # ------------------------------------------------

            ncells = shapes.size

            for cell_id in range(ncells):

                shape_id = int(shapes[cell_id])

                shape_name = shape_map[shape_id]

                cell_size = int(sizes[cell_id])

                offset = int(offsets[cell_id])

                cell_conn = connectivity[
                    offset : offset + cell_size
                ]

                vtk_cell = create_vtk_cell(
                    shape_name
                )

             # ------------------------------------------------
             # Special ordering for HEX cells
             # ------------------------------------------------

                if shape_name == "hex":

                    vtk_hex_order = [0, 1, 3, 2, 4, 5, 7, 6]

                    for i in range(8):

                        vtk_cell.GetPointIds().SetId(
                            i,
                            int(cell_conn[vtk_hex_order[i]])
                        )

             # ------------------------------------------------
             # Other cell types
             # ------------------------------------------------

                else:

                    for i in range(cell_size):

                        vtk_cell.GetPointIds().SetId(
                            i,
                            int(cell_conn[i])
                        )
                
                vtk_grid.InsertNextCell(
                    vtk_cell.GetCellType(),
                    vtk_cell.GetPointIds()
                )

        else:

            raise RuntimeError(
                f"Unsupported shape mode: {shape_mode}"
            )

        # ====================================================
        # Read point fields
        # ====================================================

        GPhi1_values = h5f[
            GPhi1_path
        ][()].astype(np.float64)

        GPhi2_values = h5f[
            GPhi2_path
        ][()].astype(np.float64)

        GPhi3_values = h5f[
            GPhi3_path
        ][()].astype(np.float64)

        # ----------------------------------------------------
        # Convert to vtk arrays
        # ----------------------------------------------------

        vtk_GPhi1 = numpy_support.numpy_to_vtk(
            GPhi1_values,
            deep=True
        )

        vtk_GPhi1.SetName("GradPhi1")

        vtk_GPhi2 = numpy_support.numpy_to_vtk(
            GPhi2_values,
            deep=True
        )

        vtk_GPhi2.SetName("GradPhi2")

        vtk_GPhi3 = numpy_support.numpy_to_vtk(
            GPhi3_values,
            deep=True
        )

        vtk_GPhi3.SetName("GradPhi3")

        # ----------------------------------------------------
        # Attach point data
        # ----------------------------------------------------

        point_data = vtk_grid.GetPointData()

        point_data.AddArray(vtk_GPhi1)
        point_data.AddArray(vtk_GPhi2)
        point_data.AddArray(vtk_GPhi3)

        point_data.SetScalars(vtk_GPhi1)

        # ====================================================
        # Ghost cells
        # ====================================================

        ghost_values = h5f[
            ghost_path
        ][()].astype(np.uint8)

        vtk_ghost = numpy_support.numpy_to_vtk(
            ghost_values,
            deep=True
        )

        vtk_ghost.SetName(
            vtkDataSetAttributes.GhostArrayName()
        )

        vtk_ghost.SetNumberOfComponents(1)

        vtk_grid.GetCellData().AddArray(
            vtk_ghost
        )

    # ========================================================
    # Write VTU
    # ========================================================

    vtu_filename = f"domain_{idx:06d}.vtu"

    writer = vtkXMLUnstructuredGridWriter()

    writer.SetFileName(vtu_filename)

    writer.SetInputData(vtk_grid)

    writer.Write()

    print("Wrote :", vtu_filename)

print()
print("All VTU files written successfully.")
