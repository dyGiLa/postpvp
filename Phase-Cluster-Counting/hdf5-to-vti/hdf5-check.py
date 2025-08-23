import h5py
import numpy as np

# all nessary pathes:

# hdf5_file_name= "/media/heidi/Elements/dyGiLa-project/dyGiLa-data/dyGiLa-Langevin/thermal-bath-UniT-Hfield-quenches/lumi-runs/thermal-bath-UniT-Hfield-quenches/LUMI-G/test/pio-test-10/pio/dyGiLa-sim-pMarker.cycle_002950/domain_000006.hdf5"

hdf5_file_name = "./domain_000005.hdf5"
## fields path
pMarker_path = "/mesh/fields/phaseMarker/values"

## coordset pathes
coords_i = '/mesh/coordsets/coords/dims/i'
coords_j = '/mesh/coordsets/coords/dims/j'
coords_k = '/mesh/coordsets/coords/dims/k'

##########################

### load hdf5 file
h5 = h5py.File(hdf5_file_name, 'r')

### access phase marker values through path
pMarker = h5[pMarker_path]
#pMValues = pMarker['values']

### access coords i, j, k through path
dim_i = h5[coords_i]
dim_j = h5[coords_j]
dim_k = h5[coords_k]

print('h5.keys() : ', h5.keys(), ', h5["mesh"].keys() : ', h5["mesh"].keys())

print('isinstance(pMarker, np.ndarray) : ', isinstance(pMarker, np.ndarray))

print('pMarker.shape =', pMarker.shape)

print('pMarker[100:200] =', pMarker[100:200])

print('dim i = ', dim_i[0], ', dim j = ',dim_j[0], ',dim k = ', dim_k[0])

##########################

isH5    = isinstance(pMarker, h5py.File)
isGroup   = isinstance(pMarker, h5py.Group)
isDataset = isinstance(pMarker, h5py.Dataset)

print("isH5 : ", isH5, ",isGroup : ", isGroup, ",isDataset : ", isDataset)

#########################

### hdf5 objects parameters
print("pMarker.parent : ", pMarker.parent, "dim_j.parent : ", dim_j.parent)

print("pMarker.file : ", pMarker.file, "dim_j.name : ", dim_j.name)

### hdf5 object attributes
print("pMarker.attrs : ", pMarker.attrs,
      ", pMarker.attrs.keys() : ", pMarker.attrs.keys(),
      ", pMarker.attrs.values() : ", pMarker.attrs.values(),      
      ", dim_j.attrs : ", dim_j.attrs,
      ", dim_j.attrs.keys() : ", dim_j.attrs.keys())

    

