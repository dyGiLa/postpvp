from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase
from vtkmodules.vtkParallelCore import vtkMultiProcessController

from vtkmodules.vtkCommonCore import vtkPoints, vtkFloatArray, vtkIntArray
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkCommonDataModel import vtkCellArray

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
from vtkmodules.util.numpy_support import vtk_to_numpy, numpy_to_vtk

import vtk
import sys

import os
sys.path.append("/home/heidi/Documents/SCC-GL-calculator")
import Module_GLSCC_calculator as sc

import numpy as np
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain


@smproxy.filter(label="Cluster-Counting-HK-MPI Filter")
@smproperty.input(name="Input")
class ClusterCounting_HK_Class(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(self)
        
    def RequestData(self, request, inInfo, outInfo):

        # gather MPI rank info
        controller = vtkMultiProcessController.GetGlobalController()
        rank = controller.GetLocalProcessId()
        num_ranks = controller.GetNumberOfProcesses()

        print(f"MPI Rank: {rank} / {num_ranks}")
        
        # access data from last pipeline
        data=dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))

        # fetch phaseMarker dataset, it is local portion 
        pMarker_Array=data.PointData['phaseMarker']

        # print("pMarker_Array.shape", pMarker_Array.shape)
        print("local pMarker_Array.shape :", pMarker_Array.shape)

        # fetch rank's element pMarker Array number 
        Nofelem_local = pMarker_Array.shape[0]

        # prapare recv_buf list to receive Nofelem_local all over ranks
        # recv_buf = [0] * num_ranks


        # Create VTK arrays
        send_array = vtkIntArray()
        send_array.SetNumberOfTuples(1)
        send_array.SetValue(0, Nofelem_local)

        recv_array = vtkIntArray()
        recv_array.SetNumberOfTuples(num_ranks)

        # Perform AllGather, board cast Nofelem_local and receive Nofelem_locals
        controller.AllGather(send_array, recv_array)        
        # board cast Nofelem_local and receive Nofelem_locals
        # controller.AllGather([Nofelem_local], recv_buf, 1, vtk.VTK_INT)

        # compute global extent dim
        np_recv_array = vtk_to_numpy(recv_array)
        total_points = np.sum(np_recv_array)
        dim = np.rint(np.power(total_points, 1/3)).astype(int)

        # This should be true if there is no ghost layers
        # assert dim**3 == Nofelem, "Input array must be a perfect cube for 3D grid"

        #####################################################
        # each rank handles a dim x dim x local_z_dim slab. #
        #####################################################
        
        # Determine z-slice range for each rank
        slabs_per_rank = dim // num_ranks
        extra = dim % num_ranks

        # Assign extra slabs to first few ranks
        z_start = rank * slabs_per_rank + np.min([rank, extra])
        z_end = z_start + slabs_per_rank - 1
        if rank < extra:
            z_end += 1

        local_z_dim = z_end - z_start + 1

        #####################################################
        #           initilize loacal labels array           #
        #####################################################

        # initilize local_labels as 1D array with numOfElems on rank
        local_labels = np.zeros(local_z_dim * dim * dim, dtype=int)
        # local_pMarker = np.zeros((local_z_dim, dim, dim), dtype=int)
        
        #####################################################
        #####################################################
        
        # cluster labeling array, same lattice
        self.labels = np.zeros_like(pMarker_Array, dtype=int)
        # print("self.labels.shape = ", self.labels.shape)

        # primary labelsArr, init with size dim
        max_labels = pMarker_Array.size + 1  # e.g., N + 1
        self.labelsArr = np.arange(max_labels, dtype=int)
        # self.labelsArr = np.zeros_like(pMarker_Array, dtype=int)        
        # print("self.labelsArr.shape = ", self.labelsArr.shape)

        # relabeled labelsArr
        # labelsArrRelabel must be initialized as zero array
        self.labelsArrRelabel = np.zeros_like(self.labelsArr, dtype=int)
        # print("self.labelsArrRelabel.shape = ", self.labelsArrRelabel.shape)

        #####################################################
        #####################################################
        
        vtk_output = vtkDataSet.GetData(outInfo)
        points = vtkPoints()

        #####################################################
        #####################################################
        
        
        """Run Hoshen-Kopelman algorithm on Rank."""
        for zidx in np.arange(local_z_dim):
            print(f"rank {rank}: zidx {zidx} loop")
            for yidx in np.arange(dim):
                for xidx in np.arange(dim):

                    # geometric points computing
                    x = -0.5 + xidx * 0.5
                    y = -0.5 + yidx * 0.5
                    z = -0.5 + zidx * 0.5
                    points.InsertNextPoint(x, y, z)

                    # convert 3d indices to 1d array index
                    idxArray = zidx * (local_z_dim * local_z_dim) + yidx * dim + xidx
                    idx_zn1_Array = (zidx-1) * (local_z_dim * local_z_dim) + yidx * dim + xidx
                    idx_yn1_Array = zidx * (local_z_dim * local_z_dim) + (yidx-1) * dim + xidx
                    idx_xn1_Array = zidx * (local_z_dim * local_z_dim) + yidx * dim + (xidx-1)

                    # print("zidx = ", zidx, ", yidx = ", yidx, ", xidx = ", xidx, "\n")
                    # print("pMarker_Array[idxArray] = ", pMarker_Array[idxArray], "\n")            
                    # print("idxArray = ", idxArray, "\n")
                    # print("idx_zn1_Array = ", idx_zn1_Array, "\n")
                    # print("idx_yn1_Array = ", idx_yn1_Array, "\n")
                    # print("idx_xn1_Array = ", idx_xn1_Array, "\n")

                    # print("labels : ", self.labels, "\n")
                    # print("labelsArr : ", self.labelsArr, "\n")            
                                        
                    if pMarker_Array[idxArray] == self.pM:

                        # Check back beighbor
                        # with MPI local zidx = 0 doesn't have back, then zidx have to > 0
                        # exchange boundary ghost layer later.
                        if zidx > 0 and local_labels[idx_zn1_Array] > 0:
                            back = local_labels[idx_zn1_Array]
                        else:
                            back = 0

                        # print("back = ", back)     
                            
                        # yidx = 0 is first row in x-y plane, not peridic no neighbor, then yidx > 0    
                        if yidx > 0 and local_labels[idx_yn1_Array] > 0:
                            top = local_labels[idx_yn1_Array]
                        else:
                            top = 0

                        # print("left = ", top)                                             
                            
                        # xidx = 0 is first column in x-y plane, not peridic no neighbor, then xidx > 0                    
                        if xidx > 0 and local_labels[idx_xn1_Array] > 0:
                            left = local_labels[idx_xn1_Array]
                        else:
                            left = 0

                        # print("left = ", left)                                                 

                        if (back == 0) and (top == 0) and (left==0):
                            # New label, if no occupied neighbor
                            self.labelsArr[0] += 1
                            self.labelsArr[self.labelsArr[0]] = self.labelsArr[0]
                            self.labels[idxArray] = self.labelsArr[0]
                            
                        elif (((back != 0) and (top == 0) and (left==0))
                              or ((back ==0) and (top != 0) and (left==0))
                              or ((back == 0) and (top == 0) and (left != 0))):
                            # occupied site has one neighbors
                            local_labels[idxArray] = np.max(np.array([back, top, left]))
                            
                        elif ((back != 0) and (top != 0) and (left==0)):
                            # two neighbors: back n top
                            local_labels[idxArray] = self.uf_union(top, back)
                            
                        elif ((back != 0) and (top == 0) and (left != 0)):
                            # two neighbors: back n left
                            local_labels[idxArray] = self.uf_union(left, back)
                            
                        elif ((back == 0) and (top != 0) and (left != 0)):
                            # two neighbors: back n left
                            local_labels[idxArray] = self.uf_union(left, top)
                            
                        else:
                            # three neighbors
                            equvlent_repres = self.uf_union(top, back)
                            local_labels[idxArray] = self.uf_union(left, equvlent_repres)

        print(f"{rank} triple loops done.")                            
        #####################################################                                                                        
        #   Communicate Ghost Layer Labels Between Ranks    #
        #####################################################                                                                                
                            
        if rank > 0:
        # Send first slice to rank-1, look of pyhton exclusive upper bound" in Python slicing
           elemIDx_0th_slab = (dim-1)*dim + (dim-1)
           vtk_loc_labels = numpy_to_vtk(local_labels[0:(elemIDx_0th_slab + 1)].copy(), True, vtk.VTK_INT)           
           controller.Send(vtk_loc_labels, rank - 1, 100)
           print(f"rank {rank} : (if rank > 0) vtk_loc_labels sent ")
        # Receive last slice from rank-1
           vtk_recv_slice = vtkIntArray()
           vtk_recv_slice.SetNumberOfTuples(dim * dim)
           
           controller.Receive(vtk_recv_slice, rank - 1, 101)
           recv_slice = vtk_to_numpy(vtk_recv_slice)

           print(f"rank {rank} recv_slice (if rank > 0):", recv_slice)
    
        # For each (x, y), if neighbor has nonzero label and our first slice has one too:
           for yidx in range(dim):
               for xidx in range(dim):
                   idxArraySlab = yidx * dim + xidx
                   if recv_slice[idxArraySlab] > 0 and local_labels[idxArraySlab] > 0:
                       l2 = recv_slice[idxArraySlab]
                       l1 = local_labels[idxArraySlab]
                       local_labels[idxArraySlab] = self.uf_union(l1, l2)
                       print(f"rank {rank} : (if rank > 0) local_labels[idxArraySlab] = ", local_labels[idxArraySlab])
                       
           print(f"{rank}: rank > 0 if block loops done.")            

                                   
                       
        if rank < (num_ranks - 1):
        # Send last slice to rank+1
           elemIDx_lastSlab_start = (local_z_dim-1) * (dim * dim)
           elemIDx_lastSlab_end = (local_z_dim-1) * (dim * dim) + (dim-1) * dim + (dim-1)
           vtk_loc_labels = numpy_to_vtk(local_labels[elemIDx_lastSlab_start:(elemIDx_lastSlab_end + 1)].copy(), True, vtk.VTK_INT)
           print(f"rank {rank} : (if rank > num_ranks - 1) vtk_loc_labels sent ")           
           controller.Send(vtk_loc_labels, rank + 1, 101)
           
        # Create empty VTK array with the right number of tuples
           vtk_recv_slice = vtkIntArray()
           vtk_recv_slice.SetNumberOfTuples(dim * dim)
           controller.Receive(vtk_recv_slice, rank + 1, 100)

        # Convert to NumPy array 
           recv_slice = vtk_to_numpy(vtk_recv_slice)

           print(f"rank {rank} recv_slice (if rank < num_rank - 1):", recv_slice)           
           
           for yidx in range(dim):
               for xidx in range(dim):
                   idxArraySlab = (local_z_dim-1) * (dim * dim) + yidx * dim + xidx
                   if local_labels[idxArraySlab] > 0 and recv_slice[yidx * dim + xidx] > 0:
                       l2 = recv_slice[yidx * dim + xidx]
                       l1 = local_labels[idxArraySlab]                       
                       local_labels[idxArraySlab] = self.uf_union(l1, l2)
                       print(f"rank {rank} : (rank < num_ranks - 1) local_labels[idxArraySlab] = ", local_labels[idxArraySlab])                       
                       
           print(f"{rank}: rank < (num_ranks - 1) if block loops done.")            
                            
                                            
        #####################################################                                                                        
        #         Second pass: re-label labels Array        #
        #####################################################                                                                                
        for zidx in range(local_z_dim):
            for yidx in range(dim):
                for xidx in range(dim):

                    # convert 3d indices to 1d array index
                    idxArray = zidx * (dim * dim) + yidx * dim + xidx
                    
                    if local_labels[idxArray] != 0:
                        root=self.uf_find(local_labels[idxArray])
                        if self.labelsArrRelabel[root] == 0:
                            self.labelsArrRelabel[0] += 1
                            self.labelsArrRelabel[root] = self.labelsArrRelabel[0]
                        self.labels[idxArray]=self.labelsArrRelabel[root]
                        print(f"rank {rank} : (2nd pass) self.labels[idxArray] = ", self.labels[idxArray])                       

        print(f"{rank}: relabel block loops done.")                                                            
        #####################################################      
        #      Convert Local Labels Back to Flat Array      #
        #####################################################
        
        # for local_z in range(local_z_dim):
        #     global_z = z_start + local_z
        #     for y in range(dim):
        #         for x in range(dim):
        #            gidx = global_z * (dim * dim) + y * dim + x
        #            self.labels[gidx] = local_labels[local_z, y, x]
        #            self.labelsArrRelabel[gidx] = self.labelsArrRelabel[local_labels[local_z, y, x]]


        #####################################################
        #####################################################
                    
        vtk_output.SetPoints(points)

        # Add vertices for rendering (helps if no topology defined)        
        # numPts = points.GetNumberOfPoints()
        # print("numPts : ", numPts)
        # numLocCells = (local_z_dim - 1)*(dim-1)*(dim-1)
        # print("numCells", numCells)
        verts = vtkCellArray()
        # for i in range(numLocCells):
        for i in range(points.GetNumberOfPoints()):
            verts.InsertNextCell(1)
            verts.InsertCellPoint(i)
        vtk_output.SetVerts(verts)    

        # num_points = data.VTKObject.GetNumberOfPoints()                
        # assert len(self.labels) == num_points, "Mismatch in point count and labels"
        assert self.labels.shape[0] == vtk_output.GetNumberOfPoints(), "Mismatch in point count and labels"

        # assert len(self.labelsArrRelabel) == num_points, "Mismatch in point count and labels"

        ###########################################################
        #             add rank self.labels as point data          #
        ###########################################################
        
        # Convert to vtk arrays
        vtk_labels = numpy_to_vtk(self.labels, deep=True)
        vtk_labels.SetName("Labeled-clusters")

        # vtk_total_labels = numpy_to_vtk(self.labelsArrRelabel[0], deep=True)
        # vtk_total_labels.SetName("Total-Cluster-labels")

        # Append them
        vtk_output.GetPointData().AddArray(vtk_labels)
        # vtk_output.GetPointData().AddArray(vtk_total_labels)

        ###########################################################
        #  add the 0th element of labelsArrRelabel as Field data  #
        ###########################################################
        
        total_clusters = int(self.labelsArrRelabel[0])

        vtk_total_labels = vtkIntArray()
        vtk_total_labels.SetName("Total-Cluster-labels")
        vtk_total_labels.SetNumberOfComponents(1)
        vtk_total_labels.InsertNextValue(total_clusters)

        vtk_output.GetFieldData().AddArray(vtk_total_labels)

        ###########################################################        

        # set paraview pipeline default active object
        vtk_output.GetPointData().SetActiveScalars("Labeled-clusters")
        
        return 1

    @smproperty.xml("""
        <DoubleVectorProperty name="phase_Marker"
            number_of_elements="1"
            default_values="1.0"
            command="SetphaseMarker">
            <DoubleRangeDomain name="range" />
            <Documentation>Set value of phase Marker</Documentation>
        </DoubleVectorProperty>""")
    def SetphaseMarker(self, pMvalue):
        self.pM = pMvalue
        self.Modified()

    
    # union-find altorithm: find fuc
    def uf_find(self, x):
        """
        Find root of label x with path compression.
        """
        y = x
        while self.labelsArr[y] != y:
            y = self.labelsArr[y]

        while self.labelsArr[x] != x:
            z = self.labelsArr[x]
            self.labelsArr[x] = y
            x = z
            
        return y
        
    # union-find altorithm: union fuc
    def uf_union(self, l1, l2):
        """
        Union two labels.
        """
        # find() return label
        # Finds the root representatives of labels l1 and l2
        repres_l2 = self.uf_find(l2)
        repres_l1 = self.uf_find(l1)

        # Unifies them by pointing repres_l1 to repres_l2
        self.labelsArr[repres_l1] = repres_l2

        # Returns the new representative repres_l2
        return self.labelsArr[repres_l1]
