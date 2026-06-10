# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
from paraview import servermanager

pm = servermanager.vtkProcessModule.GetProcessModule()
print(
    f"Partition {pm.GetPartitionId()} "
    f"of {pm.GetNumberOfLocalPartitions()}"
)

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
# pvdDataSetRaw = PVDReader(registrationName='Aalj-clip-boxClip-54-L170-32-L195-40-L180_0.pvd',
#                       FileName='/scratch/project_2014552/test/pvpost/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/Aalj-clip-boxClip-54-L170-32-L195-40-L180.pvd')

pvtuDataSetRaw = XMLPartitionedUnstructuredGridReader(registrationName='Aalj-clip-boxClip-54-L170-32-L195-40-L180-MPI32withGhost.pvtu',
                                                     FileName=['/scratch/project_2014552/test/pvpost/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/Aalj-clip-boxClip-54-L170-32-L195-40-L180-MPI32withGhost.pvtu'])

# Properties modified on pvdDataSet
#pvdDataSet.PointArrays = ['u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33']
pvtuDataSetRaw.PointArrayStatus = ['u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'vtkGhostType','vtkGhostType']

# create new 'Ghost Cells'
# pvdDataSet = GhostCellsGenerator(registrationName='GhostCellsGenerator1', Input=pvdDataSetRaw)
pvdDataSet = pvtuDataSetRaw

# debug output
# SaveData("ghost.pvtu", proxy=pvdDataSet)
###################################################
#                  grad u_al_j                    #
###################################################

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=pvdDataSet)

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = "gradient(inputs[0].PointData['u11'])"
pythonCalculator1.ArrayName = 'grad_u11'
pythonCalculator1.CopyArrays = 0

# debug output
# SaveData("PC1.pvtu", proxy=pythonCalculator1)

print("grad_u11 calculated. ")

# create a new 'Python Calculator'
pythonCalculator2 = PythonCalculator(registrationName='PythonCalculator2', Input=pvdDataSet)

# Properties modified on pythonCalculator2
pythonCalculator2.Expression = "gradient(inputs[0].PointData['u12'])"
pythonCalculator2.ArrayName = 'grad_u12'
pythonCalculator2.CopyArrays = 0

print("grad_u12 calculated. ")

# create a new 'Python Calculator'
pythonCalculator3 = PythonCalculator(registrationName='PythonCalculator3', Input=pvdDataSet)

# Properties modified on pythonCalculator3
pythonCalculator3.Expression = "gradient(inputs[0].PointData['u13'])"
pythonCalculator3.ArrayName = 'grad_u13'
pythonCalculator3.CopyArrays = 0

print("grad_u13 calculated. ")

# create a new 'Python Calculator'
pythonCalculator4 = PythonCalculator(registrationName='PythonCalculator4', Input=pvdDataSet)

# Properties modified on pythonCalculator4
pythonCalculator4.Expression = "gradient(inputs[0].PointData['u21'])"
pythonCalculator4.ArrayName = 'grad_u21'
pythonCalculator4.CopyArrays = 0

print("grad_u21 calculated. ")

# create a new 'Python Calculator'
pythonCalculator5 = PythonCalculator(registrationName='PythonCalculator5', Input=pvdDataSet)

# Properties modified on pythonCalculator5
pythonCalculator5.Expression = "gradient(inputs[0].PointData['u22'])"
pythonCalculator5.ArrayName = 'grad_u22'
pythonCalculator5.CopyArrays = 0

print("grad_u22 calculated. ")

# create a new 'Python Calculator'
pythonCalculator6 = PythonCalculator(registrationName='PythonCalculator6', Input=pvdDataSet)

# Properties modified on pythonCalculator6
pythonCalculator6.Expression = "gradient(inputs[0].PointData['u23'])"
pythonCalculator6.ArrayName = 'grad_u23'
pythonCalculator6.CopyArrays = 0

print("grad_u23 calculated. ")

# create a new 'Python Calculator'
pythonCalculator7 = PythonCalculator(registrationName='PythonCalculator7', Input=pvdDataSet)

# Properties modified on pythonCalculator7
pythonCalculator7.Expression = "gradient(inputs[0].PointData['u31'])"
pythonCalculator7.ArrayName = 'grad_u31'
pythonCalculator7.CopyArrays = 0

print("grad_u31 calculated. ")

# create a new 'Python Calculator'
pythonCalculator8 = PythonCalculator(registrationName='PythonCalculator8', Input=pvdDataSet)

# Properties modified on pythonCalculator8
pythonCalculator8.Expression = "gradient(inputs[0].PointData['u32'])"
pythonCalculator8.ArrayName = 'grad_u32'
pythonCalculator8.CopyArrays = 0

print("grad_u32 calculated. ")

# create a new 'Python Calculator'
pythonCalculator9 = PythonCalculator(registrationName='PythonCalculator9', Input=pvdDataSet)

# Properties modified on pythonCalculator9
pythonCalculator9.Expression = "gradient(inputs[0].PointData['u33'])"
pythonCalculator9.ArrayName = 'grad_u33'
pythonCalculator9.CopyArrays = 0

print("grad_u33 calculated. ")

# create a new 'Append Attributes'
# appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9])

print("appendAttribute created. ")

# save data
# SaveData('/scratch/project_2014552/test/pvpost/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/Grad_u_v_alj-boxClip-54-L170-32-L195-40-L180.pvd', proxy=appendAttributes1, ChooseArraysToWrite=1, PointDataArrays=['grad_u11', 'grad_u12', 'grad_u13', 'grad_u21', 'grad_u22', 'grad_u23', 'grad_u31', 'grad_u32', 'grad_u33', 'grad_v11', 'grad_v12', 'grad_v13', 'grad_v21', 'grad_v22', 'grad_v23', 'grad_v31', 'grad_v32', 'grad_v33'], GhostLevel=1)
SaveData('/scratch/project_2014552/test/pvpost/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/Grad_u_alj-boxClip-54-L170-32-L195-40-L180-MPI32withGhost.pvtu', proxy=appendAttributes1, ChooseArraysToWrite=1, PointDataArrays=['grad_u11', 'grad_u12', 'grad_u13', 'grad_u21', 'grad_u22', 'grad_u23', 'grad_u31', 'grad_u32', 'grad_u33'], GhostLevel=1)

print("appendAttribute created saved. ")
