from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase
from vtkmodules.vtkParallelCore import vtkMultiProcessController

from vtkmodules.vtkCommonCore import vtkPoints, vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid, vtkHexahedron, vtkCellArray

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


@smproxy.filter(label="DMNL-A-phase-A-matrix Filter")
@smproperty.input(name="Input")
class dmnl_A_phase_A_matrix_Class(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(
            # The following are matter for PV recognize Unstrctured grid
            self,
            nInputPorts=1,
            nOutputPorts=1,
            outputType='vtkUnstructuredGrid'
        )
        
    def RequestData(self, request, inInfo, outInfo):
        
        data=dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))

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
                
        Nofelem = u11_Array.shape[0]

        # side dimension of corresponding lattice
        dim = np.rint(np.power(Nofelem, 1/3)).astype(int)
        # print("dim : ", dim)

        # U(1)/SO(2) angle arrays, same lattice, same dim as u11
        self.phi_arr = np.zeros_like(u11_Array, dtype=float)
                      
        # d1, d2, d3 arrays, same lattice, same dim as u11
        self.d1_arr = np.zeros_like(u11_Array, dtype=float)
        self.d2_arr = np.zeros_like(u11_Array, dtype=float)
        self.d3_arr = np.zeros_like(u11_Array, dtype=float)
        
        # m1, m2, m3 arrays, same lattice, same dim as u11
        self.m1_arr = np.zeros_like(u11_Array, dtype=float)
        self.m2_arr = np.zeros_like(u11_Array, dtype=float)
        self.m3_arr = np.zeros_like(u11_Array, dtype=float)

        # n1, n2, n3 arrays, same lattice, same dim as u11
        self.n1_arr = np.zeros_like(u11_Array, dtype=float)
        self.n2_arr = np.zeros_like(u11_Array, dtype=float)
        self.n3_arr = np.zeros_like(u11_Array, dtype=float)

        # l1, l2, l3 arrays, same lattice, same dim as u11
        self.l1_arr = np.zeros_like(u11_Array, dtype=float)
        self.l2_arr = np.zeros_like(u11_Array, dtype=float)
        self.l3_arr = np.zeros_like(u11_Array, dtype=float)

        # declare the output handling
        # vtk_output = vtkDataSet.GetData(outInfo)
        vtk_output = vtkUnstructuredGrid()

        # declare the lattice sites output handing
        points = vtkPoints()

        # reference Vh of Delta_A*x (x + iy) A-phase OP
        z_ref = np.array([1.+0.j, 0.-1.j, 0.+0.j])
        
        """run Singlar Value Decomposition algorithm."""
        for zidx in np.arange(dim):
            for yidx in np.arange(dim):
                for xidx in np.arange(dim):

                    x = -0.5 + xidx * 0.5
                    y = -0.5 + yidx * 0.5
                    z = -0.5 + zidx * 0.5
                    points.InsertNextPoint(x, y, z)

                    ###########################################
                    #        SVD A-matrix of A-phase          #
                    ###########################################
                    
                    # convert 3d indices to 1d array index
                    idxArray = zidx * (dim * dim) + yidx * dim + xidx

                    uxx = np.array([u11_Array[idxArray],u12_Array[idxArray],u13_Array[idxArray],
                                    u21_Array[idxArray],u22_Array[idxArray],u23_Array[idxArray],
                                    u31_Array[idxArray],u32_Array[idxArray],u33_Array[idxArray]])

                    vxx = np.array([v11_Array[idxArray],v12_Array[idxArray],v13_Array[idxArray],
                                    v21_Array[idxArray],v22_Array[idxArray],v23_Array[idxArray],
                                    v31_Array[idxArray],v32_Array[idxArray],v33_Array[idxArray]])

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
                    d /= np.linalg.norm(d)

                    # --- Scale z_rot properly ---
                    z_rot = Vh[0, :].conj()  # m + in up to phase
                    z_rot /= np.linalg.norm(z_rot) # nomalized by l2 norm    
                    scale = (np.sqrt(2) * sigma) / Delta_A
                    z_rot_scaled = z_rot * scale

                    m = np.real(z_rot_scaled)
                    # This "-" is very nessary for keeping righthandness
                    n = -np.imag(z_rot_scaled)
                    # orthogonalize n against m if there is fluctuation   
                    n -= np.dot(n, m) * m  

                    # l = m x n
                    l = np.cross(m, n)

                    # compute relative phase against x (x + iy)
                    phase = np.vdot(z_ref, z_rot_scaled)
                    phi = np.angle(phase)

                    ###########################################
                    #  put mi, ni, li, di, phi back to arrays #
                    ###########################################

                    self.phi_arr[idxArray] = phi

                    self.d1_arr[idxArray] = d[0]
                    self.d2_arr[idxArray] = d[1]
                    self.d3_arr[idxArray] = d[2]                                        

                    self.m1_arr[idxArray] = m[0]
                    self.m2_arr[idxArray] = m[1]
                    self.m3_arr[idxArray] = m[2]                                        

                    self.n1_arr[idxArray] = n[0]
                    self.n2_arr[idxArray] = n[1]
                    self.n3_arr[idxArray] = n[2]                                        

                    self.l1_arr[idxArray] = l[0]
                    self.l2_arr[idxArray] = l[1]
                    self.l3_arr[idxArray] = l[2]                                        
                                   
                    ############################################
                    #            SVD of A done at here         #
                    ############################################                    


        ###############################
        #   paraview pipline output   #
        ###############################

        #################################################        
        # --- volumetric cell connectivity handling --- #
        
        # --- build right 3D cell data and put on vtkUnstureGrid --- #        
        vtk_output.SetPoints(points)

        hexs = vtkCellArray()
        for z in range(dim - 1):
            for y in range(dim - 1):
                for x in range(dim - 1):
                    p0 = x + y * dim + z * dim * dim
                    p1 = p0 + 1
                    p2 = p0 + dim + 1
                    p3 = p0 + dim
                    p4 = p0 + dim * dim
                    p5 = p4 + 1
                    p6 = p4 + dim + 1
                    p7 = p4 + dim

                    hex_cell = vtkHexahedron()
                    hex_cell.GetPointIds().SetId(0, p0)
                    hex_cell.GetPointIds().SetId(1, p1)
                    hex_cell.GetPointIds().SetId(2, p2)
                    hex_cell.GetPointIds().SetId(3, p3)
                    hex_cell.GetPointIds().SetId(4, p4)
                    hex_cell.GetPointIds().SetId(5, p5)
                    hex_cell.GetPointIds().SetId(6, p6)
                    hex_cell.GetPointIds().SetId(7, p7)

                    hexs.InsertNextCell(hex_cell)

        vtk_output.SetCells(vtkHexahedron().GetCellType(), hexs)

        # --- volumetric cell connectivity handling --- #        
        #################################################
        
        num_points = data.VTKObject.GetNumberOfPoints()
        # print("num_points :", num_points)
        # print("len(self.phi_arr) :", len(self.phi_arr), "self.phi_arr.shape : ", self.phi_arr.shape)
        # print("len(self.l1_arr) :", len(self.l1_arr), "self.l1_arr.shape", self.l1_arr.shape)
                
        assert len(self.phi_arr) == num_points, "Mismatch in point count and phi_arr"
        assert len(self.l1_arr) == num_points, "Mismatch in point count and l1_arr"
        
        # Convert to vtk arrays
        vtk_phi = numpy_to_vtk(self.phi_arr, deep=True)
        vtk_phi.SetName("U1_phi")

        vtk_d1 = numpy_to_vtk(self.d1_arr, deep=True)
        vtk_d1.SetName("d1")
        vtk_d2 = numpy_to_vtk(self.d2_arr, deep=True)
        vtk_d2.SetName("d2")
        vtk_d3 = numpy_to_vtk(self.d3_arr, deep=True)
        vtk_d3.SetName("d3")

        vtk_m1 = numpy_to_vtk(self.m1_arr, deep=True)
        vtk_m1.SetName("m1")
        vtk_m2 = numpy_to_vtk(self.m2_arr, deep=True)
        vtk_m2.SetName("m2")
        vtk_m3 = numpy_to_vtk(self.m3_arr, deep=True)
        vtk_m3.SetName("m3")

        vtk_n1 = numpy_to_vtk(self.n1_arr, deep=True)
        vtk_n1.SetName("n1")
        vtk_n2 = numpy_to_vtk(self.n2_arr, deep=True)
        vtk_n2.SetName("n2")
        vtk_n3 = numpy_to_vtk(self.n3_arr, deep=True)
        vtk_n3.SetName("n3")

        vtk_l1 = numpy_to_vtk(self.l1_arr, deep=True)
        vtk_l1.SetName("l1")
        vtk_l2 = numpy_to_vtk(self.l2_arr, deep=True)
        vtk_l2.SetName("l2")
        vtk_l3 = numpy_to_vtk(self.l3_arr, deep=True)
        vtk_l3.SetName("l3")
        
        # Append them
        vtk_output.GetPointData().AddArray(vtk_phi)
        vtk_output.GetPointData().AddArray(vtk_d1)
        vtk_output.GetPointData().AddArray(vtk_d2)
        vtk_output.GetPointData().AddArray(vtk_d3)        
        vtk_output.GetPointData().AddArray(vtk_m1)
        vtk_output.GetPointData().AddArray(vtk_m2)
        vtk_output.GetPointData().AddArray(vtk_m3)        
        vtk_output.GetPointData().AddArray(vtk_n1)
        vtk_output.GetPointData().AddArray(vtk_n2)
        vtk_output.GetPointData().AddArray(vtk_n3)
        vtk_output.GetPointData().AddArray(vtk_l1)
        vtk_output.GetPointData().AddArray(vtk_l2)
        vtk_output.GetPointData().AddArray(vtk_l3)        
        
        # print("Arrays in PointData:")
        # for i in range(vtk_output.GetPointData().GetNumberOfArrays()):
        #     print("-", vtk_output.GetPointData().GetArrayName(i))

        vtk_output.GetPointData().SetActiveScalars("U1_phi")

        # copy every things data, points, cells back to ParaView
        vtkDataSet.GetData(outInfo).ShallowCopy(vtk_output)
        
        return 1
