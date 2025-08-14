from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

import sys
import os
sys.path.append("/home/heidi/Documents/SCC-GL-calculator")
import Module_GLSCC_calculator as sc

import numpy as np
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain


@smproxy.filter(label="ABWall-Thick Filter")
@smproperty.input(name="Input")
class ABWall_Thickness(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(self)
        self.pre = 0.
        self.red_t = 0.
        self.tol_gap = 0.


    def RequestData(self, request, inInfo, outInfo):
        
#        data=inputs[0]
        data=dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))

        gap=data.PointData['gap']

        gapA=sc.gapA(self.pre, self.red_t)
        gapB=sc.gapB(self.pre, self.red_t)

        PointsArray=data.GetPoints()

        x0y0PointsArray=PointsArray[:,2]

        zArrayAphase=x0y0PointsArray[np.abs(gap - gapA) <= self.tol_gap]
        zArrayBphase=x0y0PointsArray[np.abs(gap - gapB) <= self.tol_gap]

        dzArrayAphase=np.diff(zArrayAphase)
        i, = np.where(dzArrayAphase==np.max(dzArrayAphase))
        zArrayAphase=zArrayAphase[0:(i[0]+1)]
        ABthick=zArrayBphase[0]-zArrayAphase[len(zArrayAphase)-1]
        Tol_Gap=self.tol_gap

        output = dsa.WrapDataObject(vtkDataSet.GetData(outInfo))
        output.ShallowCopy(data.VTKObject)
        output.PointData.append(ABthick, "ABW-thick");
        output.PointData.append(Tol_Gap, "tol-gap");
        output.PointData.append(zArrayBphase[0], "ZBphase");
        output.PointData.append(zArrayAphase[len(zArrayAphase)-1], "ZAphase");        

        return 1

    @smproperty.xml("""
        <DoubleVectorProperty name="pressure"
            number_of_elements="1"
            default_values="0.0"
            command="SetPressure">
            <DoubleRangeDomain name="range" />
            <Documentation>Set pressure for gap calculation</Documentation>
        </DoubleVectorProperty>""")
    def SetPressure(self, p):
        self.pre = p
        self.Modified()

    @smproperty.xml("""
        <DoubleVectorProperty name="red-t"
            number_of_elements="1"
            default_values="0.0"
            command="SetReducedT">
            <DoubleRangeDomain name="range" />
            <Documentation>Set reduced Temperature for gap calculation</Documentation>
        </DoubleVectorProperty>""")
    def SetReducedT(self, t):
        self.red_t = t
        self.Modified()

    @smproperty.xml("""
        <DoubleVectorProperty name="Tol_gap"
            number_of_elements="1"
            default_values="0.007"
            command="SetTol_gap">
            <DoubleRangeDomain name="range" />
            <Documentation>Set tolrence for gap value match</Documentation>
        </DoubleVectorProperty>""")
    def SetTol_gap(self, Tol_gap):
        self.tol_gap = Tol_gap
        self.Modified()
        

