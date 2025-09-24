# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# load plugin
LoadPlugin('./PyAlg-dmnl-vector-filter-MPI-II.py', remote=False, ns=globals())

# create a new 'XML Partitioned Image Data Reader'
piopvti = XMLPartitionedImageDataReader(registrationName='pio.pvti', FileName=['./pio.pvti'])

# Properties modified on piopvti
# piopvti.CellArrayStatus = []
piopvti.PointArrayStatus = ['gapA','u11','u12','u13','u21','u22','u23','u31','u32','u33','v11','v12','v13','v21','v22','v23','v31','v32','v33']
piopvti.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=piopvti)

print("*vti files loaded. \n")

# create a new 'Ghost Cells'
ghostCells1 = GhostCells(registrationName='GhostCells1', Input=piopvti)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=ghostCells1)

# Properties modified on threshold1, gapA * (1+/-0.0009)
threshold1.Scalars = ['POINTS', 'gapA']
threshold1.LowerThreshold = 1.8770584315796253
threshold1.UpperThreshold = 1.8804401803303439

UpdatePipeline(time=0.0, proxy=threshold1)

print("Threshold pipe line done! \n")

# create a new 'DMNL-A-phase-A-matrix-MPI Filter'
dMNLAphaseAmatrixMPIFilter1 = DMNLAphaseAmatrixMPIFilter(registrationName='DMNLAphaseAmatrixMPIFilter1', Input=threshold1)

UpdatePipeline(time=0.0, proxy=dMNLAphaseAmatrixMPIFilter1)

print("dmnl SVD filter pipe line done! \n")

# save data
SaveData('./dmnl/dmnl-phi-A-phase-AMatrix.pvtu',
         proxy=dMNLAphaseAmatrixMPIFilter1,
         ChooseArraysToWrite=1,
         PointDataArrays=['U1_phi', 'd1', 'd2', 'd3', 'gapA', 'l1', 'l2', 'l3', 'm1', 'm2', 'm3', 'n1', 'n2', 'n3', 'vtkGhostType'],
         CellDataArrays=['vtkGhostType'])

# SaveData('./dmnl/threshod.pvtu',
#          proxy=threshold1,
#          ChooseArraysToWrite=1,
#          PointDataArrays=['gapA','u11','u12','u13','u21','u22','u23','u31','u32','u33','v11','v12','v13','v21','v22','v23','v31','v32','v33','vtkGhostType'],
#          CellDataArrays=['vtkGhostType'])


print("*pvtu saving done! \n")
