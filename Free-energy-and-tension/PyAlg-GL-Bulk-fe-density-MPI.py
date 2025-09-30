from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase

from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
from vtk.util.numpy_support import numpy_to_vtk

import sys

import os
sys.path.append("/home/heidi/Documents/SCC-GL-calculator")
import Module_GLSCC_calculator as gl

import numpy as np
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain

@smproxy.filter(label="SCC-GL-Bulk-FEnergy-MPI Filter")
@smproperty.input(name="Input")
class scc_GL_Bulk_FEnergy_mpi_Class(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(
            self, nInputPorts=1, nOutputPorts=1
            ,outputType='vtkUnstructuredGrid'
        )
        
    def RequestData(self, request, inInfo, outInfo):

        # input and output portals
        self.data = dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))

        output_vtk = vtkUnstructuredGrid()
        output = dsa.WrapDataObject(output_vtk)

        n_points = self.data.GetNumberOfPoints()
        print("n_points = ", n_points)

        # Build A_{ij} as complex dictionary; (al, i) are key, A is a dictionary
        A = {}
        for al in range(3):
            for i in range(3):
                re = self.get_A_al_i(f"u{al+1}{i+1}")  # shape (1, N), N = n_points
                print("re is ", re)
                im = self.get_A_al_i(f"v{al+1}{i+1}")
                print("im is ", im)
                A[(al,i)] = re + 1j * im  # complex field A_al_i

        # Now compute bulk energy density
        f_bulk = np.zeros(n_points, dtype=np.float64)

        if (self._enable_GapAcomputation == 1):
            gap = np.zeros(n_points, dtype=np.float64)
               
        # pre-factors:
        pno=gl.pno()
        betai_prefactor = pno[1]/pno[0]

        # print("beta1_td = ", gl.beta1_td(self.p, self.T))
        # print("beta2_td = ", gl.beta2_td(self.p, self.T))
        # print("beta3_td = ", gl.beta3_td(self.p, self.T))
        # print("beta4_td = ", gl.beta4_td(self.p, self.T))
        # print("beta5_td = ", gl.beta5_td(self.p, self.T))


        for pt in range(n_points):

        # #############################################
        #               S_               #
        # #############################################
            A_pt = np.zeros((3,3), dtype=np.complex128)
    
            for al in range(3):
                for i in range(3):
                    A_pt[al, i] = A[(al,i)][pt]  # scalar field over sites

            # print("A_pt = ",A_pt)
            if (self._enable_GapAcomputation == 1):                
                gap[pt] = np.sqrt(np.real(np.trace(A_pt @ np.conj(A_pt.T))))

            # Tr[A.A^\dagger]
            alpha_term_pt = gl.alpha_td(self.p, self.T) * np.trace(A_pt @ np.conj(A_pt.T))

            # Tr[A.A^T].Tr[A.A^T]^*
            beta1_term_pt = betai_prefactor * gl.beta1_td(self.p, self.T) * (np.conj(np.trace(A_pt @ A_pt.T)) * np.trace(A_pt @ A_pt.T))

            # Tr[A.A^dag].Tr[A.A^dag]
            beta2_term_pt = betai_prefactor * gl.beta2_td(self.p, self.T) * (np.trace(A_pt @ np.conj(A_pt.T)))**2

            # Tr[(A.A^T).(A.A^T)*]
            beta3_term_pt = betai_prefactor * gl.beta3_td(self.p, self.T) * np.trace((A_pt @ A_pt.T) @ (np.conj(A_pt @ A_pt.T)))

            # Tr[(A.A^dag).(A.A^dag)]
            beta4_term_pt = betai_prefactor * gl.beta4_td(self.p, self.T) * np.trace((A_pt @ np.conj(A_pt.T)) @ (A_pt @ np.conj(A_pt.T)))

            # Tr[(A.A^dag).(A.A^dag)*]
            beta5_term_pt = betai_prefactor * gl.beta5_td(self.p, self.T) * np.trace((A_pt @ np.conj(A_pt.T)) @ (np.conj(A_pt @ np.conj(A_pt.T))))
    

            f_bulk[pt] = np.real(alpha_term_pt
                                 + beta1_term_pt + beta2_term_pt
                                 + beta3_term_pt + beta4_term_pt
                                 + beta5_term_pt) 
               

        ###############################
        #   paraview pipline output   #
        ###############################

        #########################################################        
        # --- cell connectivity handling w/ UstracturedGrid --- #
        input_vtk = self.data.VTKObject

        # # Copy points
        # output_vtk.SetPoints(input_vtk.GetPoints())

        # # Copy cells
        # output_vtk.SetCells(
        #     input_vtk.GetCellTypesArray(),
        #     input_vtk.GetCellLocationsArray(),
        #     input_vtk.GetCells()
        # )

        output_vtk.DeepCopy(input_vtk)

        # --- volumetric cell connectivity w/ UstracturedGrid --- #        
        ###########################################################
                
        output.PointData.append(f_bulk, "GLf_bulk")

        if (self._enable_GapAcomputation == 1):
            output.PointData.append(gap, "GapA")                                        
        
        output.PointData.SetActiveScalars("GLf_bulk")

        vtkUnstructuredGrid.GetData(outInfo).ShallowCopy(output.VTKObject)
        
        return 1

    # Helper to get gradients
    def get_A_al_i(self, name):
        return self.data.PointData[f"{name}"][:]

    @smproperty.xml("""
        <DoubleVectorProperty name="configuration pressure"
            number_of_elements="1"
            default_values="1.0"
            command="SetConfPressure">
            <DoubleRangeDomain name="range" />
            <Documentation>Set value of pressure of current configuration in bar</Documentation>
        </DoubleVectorProperty>""")
    def SetConfPressure(self, PValue):
        self.p = PValue
        self.Modified()

    @smproperty.xml("""
        <DoubleVectorProperty name="configuration temperature"
            number_of_elements="1"
            default_values="1.0"
            command="SetConfTemperature">
            <DoubleRangeDomain name="range" />
            <Documentation>Set value of Temperature of current configuration in mK</Documentation>
        </DoubleVectorProperty>""")
    def SetConfTemperature(self, TValue):
        # TValue in mK, gl.alpha() requires Kelvin
        self.T = TValue * 10**(-3) 
        self.Modified()

    @smproperty.xml("""
        <IntVectorProperty name="EnableGapAComputation"
                           label="Enable GapA Computation"
                           number_of_elements="1"
                           default_values="0"
                           command="SetEnableGapAComputation"
                           panel_visibility="default">
            <BooleanDomain name="bool"/>
            <Documentation>Enable or disable the GapA computing.</Documentation>
        </IntVectorProperty>""")
    def SetEnableGapAComputation(self, value):
        self._enable_GapAcomputation = value
        self.Modified()        
