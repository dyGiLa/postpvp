from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.util.numpy_support import numpy_to_vtk, vtk_to_numpy

import numpy as np
# from vtk.util.numpy_support import vtk_to_numpy, numpy_to_vtk
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain

@smproxy.filter(label="PolyLine-Ellipse-Tangent Filter")
@smproperty.input(name="Input", port_index=0)

class PolyLine_Ellipse_Tangent_Class(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(
            self, nInputPorts=1, nOutputPorts=1
        )    
    def RequestData(self, request, inInfo, outInfo):
        # get input/output VTK objects
        input0 = self.GetInputData(inInfo, 0, 0)
        output = self.GetOutputData(outInfo, 0)

        # copy geometry/cells to output
        output.ShallowCopy(input0)

        # get point coordinates
        vtk_pts = input0.GetPoints().GetData()
        pts = vtk_to_numpy(vtk_pts)

        n = len(pts)
        tangent = np.zeros_like(pts)

        # central difference
        # tangent[1:-1] = pts[2:] - pts[:-2]
        # tangent[0] = pts[1] - pts[0]
        # tangent[-1] = pts[-1] - pts[-2]
        tangent[1:-1] = pts[2:] - pts[:-2]
        tangent[0] = pts[1] - pts[-1]
        tangent[-1] = pts[0] - pts[-2]        

        # normalize
        norm = np.linalg.norm(tangent, axis=1)
        norm[norm == 0] = 1
        tangent = tangent / norm[:, None]

        # convert back to VTK
        vtk_tangent = numpy_to_vtk(tangent)
        vtk_tangent.SetNumberOfComponents(3)        
        vtk_tangent.SetName("Tangent")

        output.GetPointData().AddArray(vtk_tangent)

        return 1        

