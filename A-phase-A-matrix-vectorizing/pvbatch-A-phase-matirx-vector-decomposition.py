# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# load plugin
LoadPlugin('./PyAlg-mnl-vector-filter.py', remote=False, ns=globals())

# create a new 'XML Partitioned Image Data Reader'
piopvti = XMLPartitionedImageDataReader(registrationName='pio.pvti', FileName=['./pio.pvti'])

# Properties modified on piopvti
piopvti.CellArrayStatus = []
piopvti.PointArrayStatus = ['gapA','u11','u12','u13','u21','u22','u23','u31','u32','u33','v11','v12','v13','v21','v22','v23','v31','v32','v33']
piopvti.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=piopvti)

print("*vti files loaded. \n")

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=piopvti)

# Properties modified on threshold1, gapA * (1+/-0.01)
threshold1.Scalars = ['POINTS', 'gapA']
threshold1.LowerThreshold = 1.8599618128954347
threshold1.UpperThreshold = 1.8975367990145346

UpdatePipeline(time=0.0, proxy=threshold1)

print("Threshold pipe line done! \n")

# create a new 'DMNL-A-phase-A-matrix Filter'
dMNLAphaseAmatrixFilter1 = DMNLAphaseAmatrixFilter(registrationName='DMNLAphaseAmatrixFilter1', Input=threshold1)

UpdatePipeline(time=0.0, proxy=dMNLAphaseAmatrixFilter1)

print("dmnl SVD filter pipe line done! \n")

# save data
SaveData('./dmnl/dmnl-phi-A-phase-AMatrix.pvtu',
         proxy=dMNLAphaseAmatrixFilter1,
         ChooseArraysToWrite=1,
         PointDataArrays=['U1_phi', 'd1', 'd2', 'd3', 'l1', 'l2', 'l3', 'm1', 'm2', 'm3', 'n1', 'n2', 'n3'])

print("*pvtu saving done! \n")
