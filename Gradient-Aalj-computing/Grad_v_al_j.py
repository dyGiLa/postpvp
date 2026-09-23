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

# load data 
pvtuDataSetRaw = XMLPartitionedUnstructuredGridReader(registrationName='PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu',
                                                     FileName=['/home/heidi/Documents/p-27.0bar-T0-0.30-0.40-B-phase-critical-Bubble/E0-866.0125732eV/RSeed-1224-T0-0.3873/p-27.0-T1-12.659350932588-pio-II/pio/dyGiLa-sim-Amatrix_t-000005800.cycle_005800/PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu'])


# Properties modified on pvdDataSet
# pvdDataSet.PointArrays = ['u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33']
pvtuDataSetRaw.PointArrayStatus = ['v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33', 'vtkGhostType','vtkGhostType']

# create new 'Ghost Cells'
# pvdDataSet = GhostCellsGenerator(registrationName='GhostCellsGenerator1', Input=pvdDataSetRaw)
pvtuDataSet = pvtuDataSetRaw
###################################################
#                  grad v_al_j                    #
###################################################

# create a new 'Python Calculator'
pythonCalculator10 = PythonCalculator(registrationName='PythonCalculator10', Input=pvtuDataSet)

# Properties modified on pythonCalculator1
pythonCalculator10.Expression = "gradient(inputs[0].PointData['v11'])"
pythonCalculator10.ArrayName = 'grad_v11'
pythonCalculator10.CopyArrays = 0

print("grad_v11 calculated. ")

# create a new 'Python Calculator'
pythonCalculator11 = PythonCalculator(registrationName='PythonCalculator11', Input=pvtuDataSet)

# Properties modified on pythonCalculator2
pythonCalculator11.Expression = "gradient(inputs[0].PointData['v12'])"
pythonCalculator11.ArrayName = 'grad_v12'
pythonCalculator11.CopyArrays = 0

print("grad_v12 calculated. ")

# create a new 'Python Calculator'
pythonCalculator12 = PythonCalculator(registrationName='PythonCalculator12', Input=pvtuDataSet)

# Properties modified on pythonCalculator3
pythonCalculator12.Expression = "gradient(inputs[0].PointData['v13'])"
pythonCalculator12.ArrayName = 'grad_v13'
pythonCalculator12.CopyArrays = 0

print("grad_v13 calculated. ")

# create a new 'Python Calculator'
pythonCalculator13 = PythonCalculator(registrationName='PythonCalculator13', Input=pvtuDataSet)

# Properties modified on pythonCalculator4
pythonCalculator13.Expression = "gradient(inputs[0].PointData['v21'])"
pythonCalculator13.ArrayName = 'grad_v21'
pythonCalculator13.CopyArrays = 0

print("grad_v21 calculated. ")

# create a new 'Python Calculator'
pythonCalculator14 = PythonCalculator(registrationName='PythonCalculator14', Input=pvtuDataSet)

# Properties modified on pythonCalculator5
pythonCalculator14.Expression = "gradient(inputs[0].PointData['v22'])"
pythonCalculator14.ArrayName = 'grad_v22'
pythonCalculator14.CopyArrays = 0

print("grad_v22 calculated. ")

# create a new 'Python Calculator'
pythonCalculator15 = PythonCalculator(registrationName='PythonCalculator15', Input=pvtuDataSet)

# Properties modified on pythonCalculator6
pythonCalculator15.Expression = "gradient(inputs[0].PointData['v23'])"
pythonCalculator15.ArrayName = 'grad_v23'
pythonCalculator15.CopyArrays = 0

print("grad_v23 calculated. ")

# create a new 'Python Calculator'
pythonCalculator16 = PythonCalculator(registrationName='PythonCalculator16', Input=pvtuDataSet)

# Properties modified on pythonCalculator7
pythonCalculator16.Expression = "gradient(inputs[0].PointData['v31'])"
pythonCalculator16.ArrayName = 'grad_v31'
pythonCalculator16.CopyArrays = 0

print("grad_v31 calculated. ")

# create a new 'Python Calculator'
pythonCalculator17 = PythonCalculator(registrationName='PythonCalculator17', Input=pvtuDataSet)

# Properties modified on pythonCalculator8
pythonCalculator17.Expression = "gradient(inputs[0].PointData['v32'])"
pythonCalculator17.ArrayName = 'grad_v32'
pythonCalculator17.CopyArrays = 0

print("grad_v32 calculated. ")

# create a new 'Python Calculator'
pythonCalculator18 = PythonCalculator(registrationName='PythonCalculator18', Input=pvtuDataSet)

# Properties modified on pythonCalculator9
pythonCalculator18.Expression = "gradient(inputs[0].PointData['v33'])"
pythonCalculator18.ArrayName = 'grad_v33'
pythonCalculator18.CopyArrays = 0

print("grad_v33 calculated. ")

# create a new 'Append Attributes'
#appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

print("appendAttribute created. ")

# save data
# SaveData('/scratch/project_2014552/test/pvpost/E01500-RSeed313-p-22.0-T1-18.4684-dyGiLa-sim-Amatrix.cycle_018000/Grad_u_v_alj-boxClip-54-L170-32-L195-40-L180.pvd', proxy=appendAttributes1, ChooseArraysToWrite=1, PointDataArrays=['grad_u11', 'grad_u12', 'grad_u13', 'grad_u21', 'grad_u22', 'grad_u23', 'grad_u31', 'grad_u32', 'grad_u33', 'grad_v11', 'grad_v12', 'grad_v13', 'grad_v21', 'grad_v22', 'grad_v23', 'grad_v31', 'grad_v32', 'grad_v33'], GhostLevel=1)
SaveData('/home/heidi/Documents/p-27.0bar-T0-0.30-0.40-B-phase-critical-Bubble/E0-866.0125732eV/RSeed-1224-T0-0.3873/p-27.0-T1-12.659350932588-pio-II/pio/dyGiLa-sim-Amatrix_t-000005800.cycle_005800/Grad_v_alj-PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu', proxy=appendAttributes1, ChooseArraysToWrite=1, PointDataArrays=['grad_v11', 'grad_v12', 'grad_v13', 'grad_v21', 'grad_v22', 'grad_v23', 'grad_v31', 'grad_v32', 'grad_v33'], GhostLevel=1)

print("appendAttribute created saved. ")
