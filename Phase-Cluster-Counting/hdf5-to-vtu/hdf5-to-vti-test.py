import h5py
import numpy as np
import pyvista as pv
import os

# all nessary pathes:

# hdf5_file_name= "/media/heidi/Elements/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-G/test/pio-test-10/pio/dyGiLa-sim-pMarker.cycle_002950/domain_000006.hdf5"

hdf5_file_name = "./domain_000005.hdf5"

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

#########################################

### load hdf5 file
h5 = h5py.File(hdf5_file_name, 'r')

# Grid metadata, int convert number to int type
ni = h5[dims_i][()][0].astype(np.uint8)
nj = h5[dims_j][()][0].astype(np.uint8)
nk = h5[dims_k][()][0].astype(np.uint8)

dx = h5[spa_dx][()]
dy = h5[spa_dy][()]
dz = h5[spa_dz][()]

ox = h5[ori_x][()]
oy = h5[ori_y][()]
oz = h5[ori_z][()]

print("ni = ", ni, "isinstance(ni, int) : ", isinstance(ni, int))

# Structured grid
# grid = pv.UniformGrid(), UniformGrid() has been deprectched
grid = pv.ImageData()
grid.dimensions = (ni, nj, nk)
grid.spacing = (dx, dy, dz)
grid.origin = (ox, oy, oz)

# field data
phaseMarker_values = h5[pMarker_path][()]
gapA_values = h5[gapA_path][()]
feDensity_values = h5[feDensity_path][()]

grid["phaseMarker"] = phaseMarker_values.ravel(order='F')
grid["gapA"] = phaseMarker_values.ravel(order='F')
grid["feDensity"] = feDensity_values.ravel(order='F')

# ghost array, marks for ghost cells
ghost = h5[ghost_path][()].astype(np.uint8)
grid.cell_data["vtkGhostType"] = ghost.ravel(order='F')  # Ensure same ordering

## save vts
grid.save("test.vti")
