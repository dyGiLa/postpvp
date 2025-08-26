# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Image Data Reader'
piopvti = XMLPartitionedImageDataReader(registrationName='pio.pvti', FileName=['/home/heidi/ReHD/dyGiLa-project/dyGiLa-data/lumi-project_462000960/project_462000960/test/pio-II/pio/dyGiLa-sim-Amatrix.cycle_190000/pio.pvti'])

# Properties modified on piopvti
piopvti.CellArrayStatus = []
piopvti.PointArrayStatus = ['gapA', 'u23', 'v23']
piopvti.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=piopvti)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=piopvti)

# Properties modified on threshold1
threshold1.LowerThreshold = 1.8599618128954347
threshold1.UpperThreshold = 1.8975367990145346

UpdatePipeline(time=0.0, proxy=threshold1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)

# Properties modified on calculator1
calculator1.ResultArrayName = 'uv23'
calculator1.Function = 'u23/v23'

UpdatePipeline(time=0.0, proxy=calculator1)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)

# Properties modified on calculator2
calculator2.ResultArrayName = 'n22'
calculator2.Function = '(uv23^2)'

UpdatePipeline(time=0.0, proxy=calculator2)

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)

# Properties modified on calculator3
calculator3.ResultArrayName = 'n32'
calculator3.Function = '-(uv23^2)'

UpdatePipeline(time=0.0, proxy=calculator3)

# save data
SaveData('/home/heidi/ReHD/dyGiLa-project/dyGiLa-data/lumi-project_462000960/project_462000960/test/pio-II/pio/dyGiLa-sim-Amatrix.cycle_190000/ni2-mi2-li/ni2.pvd', proxy=calculator3, ChooseArraysToWrite=1,
    PointDataArrays=['gapA', 'n22', 'n32'],
    GhostLevel=1)