# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# load OP U data
OP_u_DataSet = XMLPartitionedUnstructuredGridReader(registrationName='PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu',
                                                     FileName=['/home/heidi/Documents/p-27.0bar-T0-0.30-0.40-B-phase-critical-Bubble/E0-866.0125732eV/RSeed-1224-T0-0.3873/p-27.0-T1-12.659350932588-pio-II/pio/dyGiLa-sim-Amatrix_t-000005800.cycle_005800/PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu'])

OP_u_DataSet.PointArrayStatus = ['u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'vtkGhostType','vtkGhostType']

# load OP V data
OP_v_DataSet = XMLPartitionedUnstructuredGridReader(registrationName='PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu',
                                                     FileName=['/home/heidi/Documents/p-27.0bar-T0-0.30-0.40-B-phase-critical-Bubble/E0-866.0125732eV/RSeed-1224-T0-0.3873/p-27.0-T1-12.659350932588-pio-II/pio/dyGiLa-sim-Amatrix_t-000005800.cycle_005800/PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu'])

OP_v_DataSet.PointArrayStatus = ['v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33', 'vtkGhostType','vtkGhostType']


# load gradient_u data
Grad_u_alj_DataSet = XMLPartitionedUnstructuredGridReader(registrationName='Grad_u_alj-PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu',
                                                     FileName=['/home/heidi/Documents/p-27.0bar-T0-0.30-0.40-B-phase-critical-Bubble/E0-866.0125732eV/RSeed-1224-T0-0.3873/p-27.0-T1-12.659350932588-pio-II/pio/dyGiLa-sim-Amatrix_t-000005800.cycle_005800/Grad_u_alj-PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu'])

Grad_u_alj_DataSet.PointArrayStatus = ['grad_u11', 'grad_u12', 'grad_u13', 'grad_u21', 'grad_u22', 'grad_u23', 'grad_u31', 'grad_u32', 'grad_u33', 'vtkGhostType','vtkGhostType']

# load gradient_v data
Grad_v_alj_DataSet = XMLPartitionedUnstructuredGridReader(registrationName='Grad_v_alj-PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu',
                                                     FileName=['/home/heidi/Documents/p-27.0bar-T0-0.30-0.40-B-phase-critical-Bubble/E0-866.0125732eV/RSeed-1224-T0-0.3873/p-27.0-T1-12.659350932588-pio-II/pio/dyGiLa-sim-Amatrix_t-000005800.cycle_005800/Grad_v_alj-PlaneClip-x122.5-boxClip-Rotated-gapA-u_ali-v_ali-x70-y80-z72.5-Lx105-Ly100-Lz100.pvtu'])

Grad_v_alj_DataSet.PointArrayStatus = ['grad_v11', 'grad_v12', 'grad_v13', 'grad_v21', 'grad_v22', 'grad_v23', 'grad_v31', 'grad_v32', 'grad_v33', 'vtkGhostType','vtkGhostType']

# create a new 'Python Calculator'
# inputs[#] index follows sequence of Input list [0, 1, 2, 3]
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=[OP_u_DataSet, OP_v_DataSet, Grad_u_alj_DataSet, Grad_v_alj_DataSet])

## mass current K1 contribution formilism:
# -ui11 v11 - ui12 v12 - ui13 v13 - ui21 v21 - ui22 v22 - ui23 v23 - ui31 v31 - ui32 v32 - ui33 v33 +
#  u11 vi11 + u12 vi12 + u13 vi13 + u21 vi21 + u22 vi22 + u23 vi23 + u31 vi31 + u32 vi32 + u33 vi33

# Properties modified on pythonCalculator19
pythonCalculator1.Expression = "-inputs[2].PointData['grad_u11']*inputs[1].PointData['v11']-inputs[2].PointData['grad_u12']*inputs[1].PointData['v12']-inputs[2].PointData['grad_u13']*inputs[1].PointData['v13']-inputs[2].PointData['grad_u21']*inputs[1].PointData['v21']-inputs[2].PointData['grad_u22']*inputs[1].PointData['v22']-inputs[2].PointData['grad_u23']*inputs[1].PointData['v23']-inputs[2].PointData['grad_u31']*inputs[1].PointData['v31']-inputs[2].PointData['grad_u32']*inputs[1].PointData['v32']-inputs[2].PointData['grad_u33']*inputs[1].PointData['v33']+inputs[0].PointData['u11']*inputs[3].PointData['grad_v11']+inputs[0].PointData['u12']*inputs[3].PointData['grad_v12']+inputs[0].PointData['u13']*inputs[3].PointData['grad_v13']+inputs[0].PointData['u21']*inputs[3].PointData['grad_v21']+inputs[0].PointData['u22']*inputs[3].PointData['grad_v22']+inputs[0].PointData['u23']*inputs[3].PointData['grad_v23']+inputs[0].PointData['u31']*inputs[3].PointData['grad_v31']+inputs[0].PointData['u32']*inputs[3].PointData['grad_v32']+inputs[0].PointData['u33']*inputs[3].PointData['grad_v33']"

pythonCalculator19.ArrayName = 'currK1'
pythonCalculator19.CopyArrays = 0

