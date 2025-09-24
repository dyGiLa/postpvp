from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase

from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
from vtk.util.numpy_support import numpy_to_vtk

import sys

import os
# sys.path.append("./SCC-GL-calculator")
# import Module_GLSCC_calculator as sc

import numpy as np
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain

@smproxy.filter(label="DMNL-A-phase-A-matrix-MPI Filter")
@smproperty.input(name="Input")
class dmnl_A_phase_A_matrix_mpi_Class(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(
            self, nInputPorts=1, nOutputPorts=1
            ,outputType='vtkUnstructuredGrid'
        )
        
    def RequestData(self, request, inInfo, outInfo):

        # input and output portals
        data = dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))

        output_vtk = vtkUnstructuredGrid()
        output = dsa.WrapDataObject(output_vtk)
        
        u11_Array=data.PointData['u11']
        u12_Array=data.PointData['u12']
        u13_Array=data.PointData['u13']
        u21_Array=data.PointData['u21']
        u22_Array=data.PointData['u22']
        u23_Array=data.PointData['u23']
        u31_Array=data.PointData['u31']
        u32_Array=data.PointData['u32']
        u33_Array=data.PointData['u33']

        v11_Array=data.PointData['v11']
        v12_Array=data.PointData['v12']
        v13_Array=data.PointData['v13']
        v21_Array=data.PointData['v21']
        v22_Array=data.PointData['v22']
        v23_Array=data.PointData['v23']
        v31_Array=data.PointData['v31']
        v32_Array=data.PointData['v32']
        v33_Array=data.PointData['v33']
                
        # Nofelem = u11_Array.shape[0]
        N = data.GetNumberOfPoints()

        # U(1)/SO(2) angle arrays, same lattice
        phi_arr = np.zeros(N, dtype=float)

        d1_arr = np.zeros(N, dtype=float)
        d2_arr = np.zeros(N, dtype=float)        
        d3_arr = np.zeros(N, dtype=float)
        
        # m1, m2, m3 arrays, same lattice, same dim as u11
        m1_arr = np.zeros(N, dtype=float)
        m2_arr = np.zeros(N, dtype=float)
        m3_arr = np.zeros(N, dtype=float)

        # n1, n2, n3 arrays, same lattice, same dim as u11
        n1_arr = np.zeros(N, dtype=float)
        n2_arr = np.zeros(N, dtype=float)
        n3_arr = np.zeros(N, dtype=float)

        # l1, l2, l3 arrays, same lattice, same dim as u11
        l1_arr = np.zeros(N, dtype=float)
        l2_arr = np.zeros(N, dtype=float)
        l3_arr = np.zeros(N, dtype=float)

        # reference Vh of Delta_A*x (x + iy) A-phase OP
        z_ref = np.array([1.+0.j, 0.-1.j, 0.+0.j])
        
        """run Singlar Value Decomposition algorithm."""
        for i in range(N):
            
        ###########################################
        #        SVD A-matrix of A-phase          #
        ###########################################
                    
            uxx = np.array([u11_Array[i],u12_Array[i],u13_Array[i],
                            u21_Array[i],u22_Array[i],u23_Array[i],
                            u31_Array[i],u32_Array[i],u33_Array[i]])

            vxx = np.array([v11_Array[i],v12_Array[i],v13_Array[i],
                            v21_Array[i],v22_Array[i],v23_Array[i],
                            v31_Array[i],v32_Array[i],v33_Array[i]])

            # construct A matrix
            u_values = uxx.reshape(3, 3)
            v_values = vxx.reshape(3, 3)
            A = u_values + 1j * v_values
            # print("A = ",A)    

            # compute gapA
            Delta_A = np.sqrt(np.trace(A.conj().T @ A).real)

            # --- SVD on A ---
            U, S, Vh = np.linalg.svd(A, full_matrices=True)

            # 1st sigular value for rank-1 OP tensor
            sigma = S[0]

            # --- Normalize d ---
            d_raw = U[:, 0]
            # print("U[:, 0] = ", U[:, 0])
            d = np.real(d_raw)
            # d /= np.linalg.norm(d)

            # --- Scale z_rot properly ---
            z_rot = Vh[0, :].conj()  # m + in up to phase
            # z_rot /= np.linalg.norm(z_rot) # nomalized by l2 norm    
            scale = (np.sqrt(2) * sigma) / Delta_A
            z_rot_scaled = z_rot * scale

            m = np.real(z_rot_scaled)
            # This "-" is very nessary for keeping righthandness
            n = -np.imag(z_rot_scaled)
            # orthogonalize n against m if there is fluctuation   
            # n -= np.dot(n, m) * m  

            # l = m x n
            l = np.cross(m, n)

            # compute relative phase against x (x + iy)
            phase = np.vdot(z_ref, z_rot_scaled)
            phi = np.angle(phase)

            ###########################################
            #  put mi, ni, li, di, phi back to arrays #
            ###########################################

            phi_arr[i] = phi

            d1_arr[i], d2_arr[i], d3_arr[i] = d                                        
            m1_arr[i], m2_arr[i], m3_arr[i] = m                                        
            n1_arr[i], n2_arr[i], n3_arr[i] = n                                        
            l1_arr[i], l2_arr[i], l3_arr[i] = l                                        
                                   
            ############################################
            #            SVD of A done at here         #
            ############################################                    


        ###############################
        #   paraview pipline output   #
        ###############################

        #########################################################        
        # --- cell connectivity handling w/ UstracturedGrid --- #
        input_vtk = data.VTKObject

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
                
        output.PointData.append(phi_arr, "U1_phi")        
        
        output.PointData.append(d1_arr, "d1")
        output.PointData.append(d2_arr, "d2")
        output.PointData.append(d3_arr, "d3")        

        output.PointData.append(m1_arr, "m1")
        output.PointData.append(m2_arr, "m2")
        output.PointData.append(m3_arr, "m3")        

        output.PointData.append(n1_arr, "n1")
        output.PointData.append(n2_arr, "n2")
        output.PointData.append(n3_arr, "n3")        

        output.PointData.append(l1_arr, "l1")
        output.PointData.append(l2_arr, "l2")
        output.PointData.append(l3_arr, "l3")        
                
        output.PointData.SetActiveScalars("U1_phi")

        vtkUnstructuredGrid.GetData(outInfo).ShallowCopy(output.VTKObject)
        
        return 1
