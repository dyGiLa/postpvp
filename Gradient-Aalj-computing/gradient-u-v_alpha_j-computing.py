# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd = PVDReader(registrationName='RingCut-Aalj-1stclip-O127.25-110-127.25-n-0.44--1-0_2ndclip-O127.25-154.535-127.25-n--0.5-1.37-0.pvd', FileName='/home/heidi/Documents/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/RingCut-Aalj-1stclip-O127.25-110-127.25-n-0.44--1-0_2ndclip-O127.25-154.535-127.25-n--0.5-1.37-0.pvd')

# Properties modified on ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd
ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd.PointArrays = ['u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33']

UpdatePipeline(time=0.0, proxy=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = "gradient(inputs[0].PointData['u11'])"
pythonCalculator1.ArrayName = 'grad_u11'
pythonCalculator1.CopyArrays = 0

UpdatePipeline(time=0.0, proxy=pythonCalculator1)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# set active source
SetActiveSource(pythonCalculator1)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator2 = PythonCalculator(registrationName='PythonCalculator2', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator2
pythonCalculator2.Expression = "gradient(inputs[0].PointData['u12'])"
pythonCalculator2.ArrayName = 'grad_u12'

UpdatePipeline(time=0.0, proxy=pythonCalculator2)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator3 = PythonCalculator(registrationName='PythonCalculator3', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator3
pythonCalculator3.Expression = "gradient(inputs[0].PointData['u13'])"
pythonCalculator3.ArrayName = 'grad_u13'

UpdatePipeline(time=0.0, proxy=pythonCalculator3)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator4 = PythonCalculator(registrationName='PythonCalculator4', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator4
pythonCalculator4.Expression = "gradient(inputs[0].PointData['u21'])"
pythonCalculator4.ArrayName = 'grad_u21'

UpdatePipeline(time=0.0, proxy=pythonCalculator4)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator5 = PythonCalculator(registrationName='PythonCalculator5', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# set active source
SetActiveSource(pythonCalculator4)

# set active source
SetActiveSource(pythonCalculator5)

# Properties modified on pythonCalculator5
pythonCalculator5.Expression = "gradient(inputs[0].PointData['u22'])"
pythonCalculator5.ArrayName = 'grad_u22'

UpdatePipeline(time=0.0, proxy=pythonCalculator5)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator6 = PythonCalculator(registrationName='PythonCalculator6', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator6
pythonCalculator6.Expression = "gradient(inputs[0].PointData['u33'])"
pythonCalculator6.ArrayName = 'grad_u33'

UpdatePipeline(time=0.0, proxy=pythonCalculator6)

# set active source
SetActiveSource(pythonCalculator5)

# set active source
SetActiveSource(pythonCalculator6)

# Properties modified on pythonCalculator6
pythonCalculator6.Expression = "gradient(inputs[0].PointData['u23'])"
pythonCalculator6.ArrayName = 'grad_u23'

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator7 = PythonCalculator(registrationName='PythonCalculator7', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator7
pythonCalculator7.Expression = "gradient(inputs[0].PointData['u31'])"
pythonCalculator7.ArrayName = 'grad_u31'

UpdatePipeline(time=0.0, proxy=pythonCalculator7)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator8 = PythonCalculator(registrationName='PythonCalculator8', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# set active source
SetActiveSource(pythonCalculator7)

# set active source
SetActiveSource(pythonCalculator8)

# Properties modified on pythonCalculator8
pythonCalculator8.Expression = "gradient(inputs[0].PointData['u32'])"
pythonCalculator8.ArrayName = 'grad_u32'

UpdatePipeline(time=0.0, proxy=pythonCalculator8)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator9 = PythonCalculator(registrationName='PythonCalculator9', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator9
pythonCalculator9.Expression = "gradient(inputs[0].PointData['u33'])"
pythonCalculator9.ArrayName = 'grad_u33'

UpdatePipeline(time=0.0, proxy=pythonCalculator9)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# set active source
SetActiveSource(pythonCalculator9)

# set active source
SetActiveSource(pythonCalculator1)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator10 = PythonCalculator(registrationName='PythonCalculator10', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator10
pythonCalculator10.Expression = "gradient(inputs[0].PointData['v11'])"
pythonCalculator10.ArrayName = 'grad_v11'

UpdatePipeline(time=0.0, proxy=pythonCalculator10)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator11 = PythonCalculator(registrationName='PythonCalculator11', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator11
pythonCalculator11.Expression = "gradient(inputs[0].PointData['v12'])"
pythonCalculator11.ArrayName = 'grad_v12'

UpdatePipeline(time=0.0, proxy=pythonCalculator11)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# set active source
SetActiveSource(pythonCalculator11)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator12 = PythonCalculator(registrationName='PythonCalculator12', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator12
pythonCalculator12.Expression = "gradient(inputs[0].PointData['v13'])"
pythonCalculator12.ArrayName = 'grad_v13'

UpdatePipeline(time=0.0, proxy=pythonCalculator12)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator13 = PythonCalculator(registrationName='PythonCalculator13', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator13
pythonCalculator13.Expression = "gradient(inputs[0].PointData['v21'])"
pythonCalculator13.ArrayName = 'grad_v21'

UpdatePipeline(time=0.0, proxy=pythonCalculator13)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator14 = PythonCalculator(registrationName='PythonCalculator14', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator14
pythonCalculator14.Expression = "gradient(inputs[0].PointData['v22'])"
pythonCalculator14.ArrayName = 'grad_v22'

UpdatePipeline(time=0.0, proxy=pythonCalculator14)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator15 = PythonCalculator(registrationName='PythonCalculator15', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator15
pythonCalculator15.Expression = "gradient(inputs[0].PointData['v23'])"
pythonCalculator15.ArrayName = 'grad_v23'

UpdatePipeline(time=0.0, proxy=pythonCalculator15)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator16 = PythonCalculator(registrationName='PythonCalculator16', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator16
pythonCalculator16.Expression = "gradient(inputs[0].PointData['v31'])"
pythonCalculator16.ArrayName = 'grad_v31'

UpdatePipeline(time=0.0, proxy=pythonCalculator16)

# create a new 'Python Calculator'
pythonCalculator17 = PythonCalculator(registrationName='PythonCalculator17', Input=pythonCalculator16)

# set active source
SetActiveSource(pythonCalculator16)

# destroy pythonCalculator17
Delete(pythonCalculator17)
del pythonCalculator17

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator17 = PythonCalculator(registrationName='PythonCalculator17', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator17
pythonCalculator17.Expression = "gradient(inputs[0].PointData['v32'])"
pythonCalculator17.ArrayName = 'grad_v32'

UpdatePipeline(time=0.0, proxy=pythonCalculator17)

# set active source
SetActiveSource(ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# create a new 'Python Calculator'
pythonCalculator18 = PythonCalculator(registrationName='PythonCalculator18', Input=ringCutAalj1stclipO1272511012725n04410_2ndclipO1272515453512725n051370pvd)

# Properties modified on pythonCalculator18
pythonCalculator18.Expression = "gradient(inputs[0].PointData['v33'])"
pythonCalculator18.ArrayName = 'grad_v33'

UpdatePipeline(time=0.0, proxy=pythonCalculator18)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=pythonCalculator18)

# set active source
SetActiveSource(pythonCalculator18)

# destroy appendAttributes1
Delete(appendAttributes1)
del appendAttributes1

# set active source
SetActiveSource(pythonCalculator1)

# set active source
SetActiveSource(pythonCalculator18)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

UpdatePipeline(time=0.0, proxy=appendAttributes1)

# get active source.
appendAttributes1 = GetActiveSource()

# save data
SaveData('/home/heidi/Documents/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/RingCut-Grad_u_v_alj-1stclip-O127.25-110-127.25-n-0.44--1-0_2ndclip-O127.25-154.535-127.25-n--0.5-1.37-0.pvd', proxy=appendAttributes1, ChooseArraysToWrite=1,
    PointDataArrays=['grad_u11', 'grad_u12', 'grad_u13', 'grad_u21', 'grad_u22', 'grad_u23', 'grad_u31', 'grad_u32', 'grad_u33', 'grad_v11', 'grad_v12', 'grad_v13', 'grad_v21', 'grad_v22', 'grad_v23', 'grad_v31', 'grad_v32', 'grad_v33'],
    GhostLevel=1)