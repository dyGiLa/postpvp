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

@smproxy.filter(label="Grad-Phase-ImTrApjAd-MPI Filter")
@smproperty.input(name="Input")
class Grad_Phase_ImTrApjAd_mpi_Class(VTKPythonAlgorithmBase):
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

        # construct A_{ij} as complex dictionary;
        # (al, i) are key, A is a dictionary
        A = {}
        for al in range(3):
            for i in range(3):
                re = self.get_A_al_i(f"u{al+1}{i+1}")  # shape (1, N), N = n_points
                print("re is ", re)
                im = self.get_A_al_i(f"v{al+1}{i+1}")
                print("im is ", im)
                A[(al,i)] = re + 1j * im  # complex field A_al_i

        
        # Build gradients of A_{ij} as complex vectors;
        # (al, i) are key, grad_A is a dictionary
        grad_A = {}
        for al in range(3):
            for i in range(3):
                re = self.get_grad_A_al_i(f"grad_u{al+1}{i+1}")  # shape (3, N), N = n_points
                print("re is ", re)
                im = self.get_grad_A_al_i(f"grad_v{al+1}{i+1}")  # shape (3, N), N = n_points
                print("im is ", im)
                grad_A[(al,i)] = re + 1j * im  # complex vector gradient per component

        ########################################                        
        # compute -(1/TrAdA)Im(A \partial_j A^*)
        ########################################                
        mip_Xni = np.zeros(n_points, dtype=np.float64)
        mip_Yni = np.zeros(n_points, dtype=np.float64)
        mip_Zni = np.zeros(n_points, dtype=np.float64)
               
        for pt in range(n_points):

        # #############################################
        #        for every pt:                        #            
        #        -(1/TrAdA)Im(A \partial_X A^d)       #
        #        -(1/TrAdA)Im(A \partial_Y A^d)       #
        #        -(1/TrAdA)Im(A \partial_Z A^d)       #            
        # #############################################
            # prapare containers
            A_pt = np.zeros((3,3), dtype=np.complex128)            
            grad_A_x_pt = np.zeros((3,3), dtype=np.complex128)
            grad_A_y_pt = np.zeros((3,3), dtype=np.complex128)
            grad_A_z_pt = np.zeros((3,3), dtype=np.complex128)
    
            for al in range(3):
                for i in range(3):
                    # 3-vector (\partial_x, \partial_y, \partial_z)
                    grad_vec = grad_A[(al,i)][:, pt]
                    
                    grad_A_x_pt[al, i] = grad_vec[0]
                    grad_A_y_pt[al, i] = grad_vec[1]
                    grad_A_z_pt[al, i] = grad_vec[2]

                    A_pt[al, i] = A[(al,i)][pt]

            # Tr(AdA)
            invTrAdA_pt = 1./np.trace(np.conj(A_pt.T) @ A_pt)
                        
            mip_Xni[pt] = np.trace(A_pt @ np.conj(grad_A_x_pt.T)) * invTrAdA_pt
            mip_Yni[pt] = np.trace(A_pt @ np.conj(grad_A_y_pt.T)) * invTrAdA_pt
            mip_Zni[pt] = np.trace(A_pt @ np.conj(grad_A_z_pt.T)) * invTrAdA_pt
                
        ###############################
        #   paraview pipline output   #
        ###############################

        #########################################################        
        # --- cell connectivity handling w/ UstracturedGrid --- #
        input_vtk = self.data.VTKObject

        output_vtk.DeepCopy(input_vtk)

        # --- volumetric cell connectivity w/ UstracturedGrid --- #        
        ###########################################################
                
        output.PointData.append(mip_Xni, "mip_Xni")
        output.PointData.append(mip_Yni, "mip_Yni")
        output.PointData.append(mip_Zni, "mip_Zni")        
        
        output.PointData.SetActiveScalars("mip_Xni")

        vtkUnstructuredGrid.GetData(outInfo).ShallowCopy(output.VTKObject)
        
        return 1

    # Helper to get gradients
    def get_grad_A_al_i(self, name):
        return np.array([self.data.PointData[f"{name}"][:, i] for i in range(3)])

    # Helper to get gradients
    def get_A_al_i(self, name):
        return self.data.PointData[f"{name}"][:]
    
