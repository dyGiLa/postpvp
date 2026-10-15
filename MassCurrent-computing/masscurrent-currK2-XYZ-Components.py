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

#########################################################################################

# - v_{01} \p1u_{00} + u_{02} \p2v_{00} - v_{02} \p2u_{00} # -1v12.2gu11[1] +0u13.3gv11[2] -1v13.2gu11[2]
# - v_{11} \p1u_{10} + u_{12} \p2v_{10} - v_{12} \p2u_{10} # -1v22.2gu21[1] +0u23.3gv21[2] -1v23.2gu21[2]
# - v_{21} \p1u_{20} + u_{22} \p2v_{20} - v_{22} \p2u_{20} # -1v32.2gu31[1] +0u33.3gv31[2] -1v33.2gu31[2]
# + u_{00} \p0v_{00} - v_{00} \p0u_{00} + u_{01} \p1v_{00} # +0u11.3gv11[0] -1v11.2gu11[0] +0u12.3gv11[1]
# + u_{10} \p0v_{10} - v_{10} \p0u_{10} + u_{11} \p1v_{10} # +0u21.3gv21[0] -1v21.2gu21[0] +0u22.3gv21[1]
# + u_{20} \p0v_{20} - v_{20} \p0u_{20} + u_{21} \p1v_{20} # +0u31.3gv31[0] -1v31.2gu31[0] +0u32.3gv31[1]

# create a new 'Python Calculator'
# inputs[#] index follows sequence of Input list [0, 1, 2, 3]
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=[OP_u_DataSet, OP_v_DataSet, Grad_u_alj_DataSet, Grad_v_alj_DataSet])

# Properties modified on pythonCalculator20, i = 1 i.e., X
pythonCalculator1.Expression = "inputs[0].PointData['u11']*inputs[3].PointData['grad_v11'][:,0] - inputs[1].PointData['v11']*inputs[2].PointData['grad_u11'][:,0]+inputs[0].PointData['u12']*inputs[3].PointData['grad_v11'][:,1] - inputs[1].PointData['v12']*inputs[2].PointData['grad_u11'][:,1]+inputs[0].PointData['u13']*inputs[3].PointData['grad_v11'][:,2] - inputs[1].PointData['v13']*inputs[2].PointData['grad_u11'][:,2]+inputs[0].PointData['u21']*inputs[3].PointData['grad_v21'][:,0] - inputs[1].PointData['v21']*inputs[2].PointData['grad_u21'][:,0]+inputs[0].PointData['u22']*inputs[3].PointData['grad_v21'][:,1] - inputs[1].PointData['v22']*inputs[2].PointData['grad_u21'][:,1]+inputs[0].PointData['u23']*inputs[3].PointData['grad_v21'][:,2] - inputs[1].PointData['v23']*inputs[2].PointData['grad_u21'][:,2]+inputs[0].PointData['u31']*inputs[3].PointData['grad_v31'][:,0] - inputs[1].PointData['v31']*inputs[2].PointData['grad_u31'][:,0]+inputs[0].PointData['u32']*inputs[3].PointData['grad_v31'][:,1] - inputs[1].PointData['v32']*inputs[2].PointData['grad_u31'][:,1]+inputs[0].PointData['u33']*inputs[3].PointData['grad_v31'][:,2] - inputs[1].PointData['v33']*inputs[2].PointData['grad_u31'][:,2]"

pythonCalculator1.ArrayName = 'currK2X'
pythonCalculator1.CopyArrays = 0

#########################################################################################

# create a new 'Python Calculator'
# inputs[#] index follows sequence of Input list [0, 1, 2, 3]
pythonCalculator2 = PythonCalculator(registrationName='PythonCalculator2', Input=[OP_u_DataSet, OP_v_DataSet, Grad_u_alj_DataSet, Grad_v_alj_DataSet])

# Properties modified on pythonCalculator21, i = 2 i.e., Y
pythonCalculator2.Expression = "inputs[0].PointData['u11']*inputs[3].PointData['grad_v12'][:,0] - inputs[1].PointData['v11']*inputs[2].PointData['grad_u12'][:,0]+inputs[0].PointData['u12']*inputs[3].PointData['grad_v12'][:,1] - inputs[1].PointData['v12']*inputs[2].PointData['grad_u12'][:,1]+inputs[0].PointData['u13']*inputs[3].PointData['grad_v12'][:,2] - inputs[1].PointData['v13']*inputs[2].PointData['grad_u12'][:,2]+inputs[0].PointData['u21']*inputs[3].PointData['grad_v22'][:,0] - inputs[1].PointData['v21']*inputs[2].PointData['grad_u22'][:,0]+inputs[0].PointData['u22']*inputs[3].PointData['grad_v22'][:,1] - inputs[1].PointData['v22']*inputs[2].PointData['grad_u22'][:,1]+inputs[0].PointData['u23']*inputs[3].PointData['grad_v22'][:,2] - inputs[1].PointData['v23']*inputs[2].PointData['grad_u22'][:,2]+inputs[0].PointData['u31']*inputs[3].PointData['grad_v32'][:,0] - inputs[1].PointData['v31']*inputs[2].PointData['grad_u32'][:,0]+inputs[0].PointData['u32']*inputs[3].PointData['grad_v32'][:,1] - inputs[1].PointData['v32']*inputs[2].PointData['grad_u32'][:,1]+inputs[0].PointData['u33']*inputs[3].PointData['grad_v32'][:,2] - inputs[1].PointData['v33']*inputs[2].PointData['grad_u32'][:,2]"

pythonCalculator2.ArrayName = 'currK2Y'
pythonCalculator2.CopyArrays = 0


#########################################################################################

# create a new 'Python Calculator'
# inputs[#] index follows sequence of Input list [0, 1, 2, 3]
pythonCalculator3 = PythonCalculator(registrationName='PythonCalculator3', Input=[OP_u_DataSet, OP_v_DataSet, Grad_u_alj_DataSet, Grad_v_alj_DataSet])

# Properties modified on pythonCalculator22, i = 3 i.e., z
pythonCalculator3.Expression = "inputs[0].PointData['u11']*inputs[3].PointData['grad_v13'][:,0] - inputs[1].PointData['v11']*inputs[2].PointData['grad_u13'][:,0]+inputs[0].PointData['u12']*inputs[3].PointData['grad_v13'][:,1] - inputs[1].PointData['v12']*inputs[2].PointData['grad_u13'][:,1]+inputs[0].PointData['u13']*inputs[3].PointData['grad_v13'][:,2] - inputs[1].PointData['v13']*inputs[2].PointData['grad_u13'][:,2]+inputs[0].PointData['u21']*inputs[3].PointData['grad_v23'][:,0] - inputs[1].PointData['v21']*inputs[2].PointData['grad_u23'][:,0]+inputs[0].PointData['u22']*inputs[3].PointData['grad_v23'][:,1] - inputs[1].PointData['v22']*inputs[2].PointData['grad_u23'][:,1]+inputs[0].PointData['u23']*inputs[3].PointData['grad_v23'][:,2] - inputs[1].PointData['v23']*inputs[2].PointData['grad_u23'][:,2]+inputs[0].PointData['u31']*inputs[3].PointData['grad_v33'][:,0] - inputs[1].PointData['v31']*inputs[2].PointData['grad_u33'][:,0]+inputs[0].PointData['u32']*inputs[3].PointData['grad_v33'][:,1] - inputs[1].PointData['v32']*inputs[2].PointData['grad_u33'][:,1]+inputs[0].PointData['u33']*inputs[3].PointData['grad_v33'][:,2] - inputs[1].PointData['v33']*inputs[2].PointData['grad_u33'][:,2]"

pythonCalculator3.ArrayName = 'currK2Z'
pythonCalculator3.CopyArrays = 0
