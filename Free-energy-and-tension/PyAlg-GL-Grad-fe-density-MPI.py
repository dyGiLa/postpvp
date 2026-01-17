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

@smproxy.filter(label="SCC-GL-Grad-FEnergy-MPI Filter")
@smproperty.input(name="Input")
class scc_GL_Grad_FEnergy_mpi_Class(VTKPythonAlgorithmBase):
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

        # Build gradients of A_{ij} as complex vectors; (al, i) are key, grad_A is a dictionary
        grad_A = {}
        for al in range(3):
            for i in range(3):
                re = get_grad_A_al_i(f"grad_u{al+1}{i+1}")  # shape (3, N), N = n_points
                print("re is ", re)
                im = get_grad_A_al_i(f"grad_v{al+1}{i+1}")  # shape (3, N), N = n_points
                print("im is ", im)
                grad_A[(al,i)] = re + 1j * im  # complex vector gradient per component

        ####################################                        
        # compute OP field f_grad(x)
        ####################################                
        f_grad = np.zeros(n_points, dtype=np.float64)
               
        for pt in range(n_points):

        # #############################################
        #        S_pkAaljpkACalj. Laplacian           #
        # #############################################
            grad_A_x = np.zeros((3,3), dtype=np.complex128)
            grad_A_y = np.zeros((3,3), dtype=np.complex128)
            grad_A_z = np.zeros((3,3), dtype=np.complex128)
    
            for al in range(3):
                for i in range(3):
                    # 3-vector (\partial_x, \partial_y, \partial_z)
                    grad_vec = grad_A[(al,i)][:, pt]
                    
                    grad_A_x[al, i] = grad_vec[0]
                    grad_A_y[al, i] = grad_vec[1]
                    grad_A_z[al, i] = grad_vec[2]
    
            term_x = np.trace(grad_A_x @ np.conj(grad_A_x.T))
            term_y = np.trace(grad_A_y @ np.conj(grad_A_y.T))
            term_z = np.trace(grad_A_z @ np.conj(grad_A_z.T))

            # pkAalj.pkACalj
            f_grad[pt] += np.real(term_x + term_y + term_z)

        # #############################################
        #      S_pjAalj.pkACalk  S_pkAalj.pjACalk     #
        # #############################################

            pjAaljpkACalk_pt = 0.0 + 1j* 0.0
            pkAaljpjACalk_pt = 0.0 + 1j* 0.0

            for al in range(3):
                # Term pjAalj.pkACalk:
                div_A_al = 0.0 + 1j* 0.0  # ∂_j M_{αj}
                div_A_al_conj = 0.0 + 1j* 0.0  # ∂_k M*_{αk}

                # j and k index same range here
                for j in range(3): 
                    grad_Aalj = grad_A[(al, j)][:, pt]  # ∂_j M_{αj}
                    div_A_al += grad_Aalj[j]  # ∂_j component
                    div_A_al_conj += np.conj(grad_Aalj[j])  # ∂_k M*_{αk}, same j=k
            
                pjAaljpkACalk_pt += div_A_al * div_A_al_conj

                # Term pkAalj.pjACalk:
                for j in range(3):
                    for k in range(3):
                        grad_Aalj = grad_A[(al, j)][:, pt]  # ∂_k M_{αj}
                        grad_Aalk = grad_A[(al, k)][:, pt]  # ∂_j M*_{αk}
                
                        pkAaljpjACalk_pt += grad_Aalj[k] * np.conj(grad_Aalk[j])

            f_grad[pt] += np.real(pjAaljpkACalk_pt) + np.real(pkAaljpjACalk_pt)             
                
        ###############################
        #   paraview pipline output   #
        ###############################

        #########################################################        
        # --- cell connectivity handling w/ UstracturedGrid --- #
        input_vtk = self.data.VTKObject

        output_vtk.DeepCopy(input_vtk)

        # --- volumetric cell connectivity w/ UstracturedGrid --- #        
        ###########################################################
                
        output.PointData.append(f_grad, "GLf_grad")
        
        output.PointData.SetActiveScalars("GLf_grad")

        vtkUnstructuredGrid.GetData(outInfo).ShallowCopy(output.VTKObject)
        
        return 1

    # Helper to get gradients
    def get_grad_A_al_i(self, name):
        return np.array([self.data.PointData[f"{name}"][:, i] for i in range(3)])
