from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase
from vtkmodules.vtkParallelCore import vtkMultiProcessController

from vtkmodules.vtkCommonCore import vtkPoints, vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkCommonDataModel import vtkCellArray

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
from vtk.util.numpy_support import numpy_to_vtk

import sys

import os
sys.path.append("/home/heidi/Documents/SCC-GL-calculator")
import Module_GLSCC_calculator as sc

import numpy as np
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain


@smproxy.filter(label="Cluster-Counting-HK Filter")
@smproperty.input(name="Input")
class ClusterCounting_HK_Class(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(self)
        
    def RequestData(self, request, inInfo, outInfo):
        
        data=dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))

        # pMarker_Array=data.PointData['phaseMarker'][0:512]
        pMarker_Array=data.PointData['phaseMarker']             

        Nofelem = pMarker_Array.shape[0]

        # side dimension of corresponding lattice
        dim = np.rint(np.power(Nofelem, 1/3)).astype(int)
        # print("dim : ", dim)
        
        # cluster labeling array, same lattice
        self.labels = np.zeros_like(pMarker_Array, dtype=int)
        # print("self.labels.shape = ", self.labels.shape)

        # primary labelsArr, init with size dim
        self.labelsArr = np.zeros_like(pMarker_Array, dtype=int)
        # print("self.labelsArr.shape = ", self.labelsArr.shape)

        # relabeled labelsArr
        # labelsArrRelabel must be initialized as zero array
        self.labelsArrRelabel = np.zeros_like(self.labelsArr, dtype=int)
        # print("self.labelsArrRelabel.shape = ", self.labelsArrRelabel.shape)

        vtk_output = vtkDataSet.GetData(outInfo)
        points = vtkPoints()
        
        """Run Hoshen-Kopelman algorithm."""
        for zidx in np.arange(dim):
            for yidx in np.arange(dim):
                for xidx in np.arange(dim):

                    x = -0.5 + xidx * 0.5
                    y = -0.5 + yidx * 0.5
                    z = -0.5 + zidx * 0.5
                    points.InsertNextPoint(x, y, z)

                    # convert 3d indices to 1d array index
                    idxArray = zidx * (dim * dim) + yidx * dim + xidx
                    idx_zn1_Array = (zidx-1) * (dim * dim) + yidx * dim + xidx
                    idx_yn1_Array = zidx * (dim * dim) + (yidx-1) * dim + xidx
                    idx_xn1_Array = zidx * (dim * dim) + yidx * dim + (xidx-1)

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

                        # zidx = 0 is first slice of x-y, not peridic no neighbor, then zidx > 0
                        if zidx > 0 and self.labels[idx_zn1_Array] > 0:
                            back = self.labels[idx_zn1_Array]
                        else:
                            back = 0

                        # print("back = ", back)     
                            
                        # yidx = 0 is first row in x-y plane, not peridic no neighbor, then yidx > 0    
                        if yidx > 0 and self.labels[idx_yn1_Array] > 0:
                            top = self.labels[idx_yn1_Array]
                        else:
                            top = 0

                        # print("left = ", top)                                             
                            
                        # xidx = 0 is first column in x-y plane, not peridic no neighbor, then xidx > 0                    
                        if xidx > 0 and self.labels[idx_xn1_Array] > 0:
                            left = self.labels[idx_xn1_Array]
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
                            self.labels[idxArray] = np.max(np.array([back, top, left]))
                            
                        elif ((back != 0) and (top != 0) and (left==0)):
                            # two neighbors: back n top
                            self.labels[idxArray] = self.uf_union(top, back)
                            
                        elif ((back != 0) and (top == 0) and (left != 0)):
                            # two neighbors: back n left
                            self.labels[idxArray] = self.uf_union(left, back)
                            
                        elif ((back == 0) and (top != 0) and (left != 0)):
                            # two neighbors: back n left
                            self.labels[idxArray] = self.uf_union(left, top)
                            
                        else:
                            # three neighbors
                            equvlent_repres = self.uf_union(top, back)
                            self.labels[idxArray] = self.uf_union(left, equvlent_repres)
                                                
        # print("labels :")
        # print(self.labels, "\n")
        # print("labelsArr :")
        # print(self.labelsArr, "\n")        
                        
        # Second pass: re-label labels Array
        for zidx in range(dim):
            for yidx in range(dim):
                for xidx in range(dim):

                    # convert 3d indices to 1d array index
                    idxArray = zidx * (dim * dim) + yidx * dim + xidx
                    
                    if self.labels[idxArray] != 0:
                        repres_idx=self.uf_find(self.labels[idxArray])
                        if self.labelsArrRelabel[repres_idx] == 0:
                            self.labelsArrRelabel[0] += 1
                            self.labelsArrRelabel[repres_idx] = self.labelsArrRelabel[0]
                        self.labels[idxArray]=self.labelsArrRelabel[repres_idx]

        # print("self.labelsArrRelabel :")
        # print(self.labelsArrRelabel, "\n")

        vtk_output.SetPoints(points)

        # (Optional) Add vertices for rendering (helps if no topology defined)        
        # numPts = points.GetNumberOfPoints()
        # print("numPts : ", numPts)
        numCells = (dim-1)*(dim-1)*(dim-1)
        # print("numCells", numCells)
        verts = vtkCellArray()
        for i in range(numCells):
            verts.InsertNextCell(1)
            verts.InsertCellPoint(i)
        vtk_output.SetVerts(verts)    

        # Now wrap after copy
        output = dsa.WrapDataObject(vtk_output)

        # num_points = output.GetNumberOfPoints()
        num_points = data.VTKObject.GetNumberOfPoints()
        # print("num_points :", num_points)
        # print("len(self.labels) :", len(self.labels), "self.labels.shape : ", self.labels.shape)
        # print("len(self.labelsArrRelabel) :", len(self.labelsArrRelabel), "self.labelsArrRelabel.shape", self.labelsArrRelabel.shape)
                
        assert len(self.labels) == num_points, "Mismatch in point count and labels"
        assert len(self.labelsArrRelabel) == num_points
        
        # original_indices = numpy_to_vtk(np.arange(num_points), deep=True)
        # original_indices.SetName("vtkOriginalIndices")        

        # Convert to vtk arrays
        vtk_labels = numpy_to_vtk(self.labels, deep=True)
        vtk_labels.SetName("Labeled-clusters")

        vtk_labels_relabeled = numpy_to_vtk(self.labelsArrRelabel, deep=True)
        vtk_labels_relabeled.SetName("Cluster-labels")

        # vtk_dim = numpy_to_vtk(dim, deep=True)
        # vtk_dim.SetName("lattice-sideDim")

        # Append them
        vtk_output.GetPointData().AddArray(vtk_labels)
        vtk_output.GetPointData().AddArray(vtk_labels_relabeled)

        # print("Arrays in PointData:")
        # for i in range(vtk_output.GetPointData().GetNumberOfArrays()):
        #     print("-", vtk_output.GetPointData().GetArrayName(i))

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
        repres_l2 = self.uf_find(l2)
        repres_l1 = self.uf_find(l1)

        self.labelsArr[repres_l1] = repres_l2
        return self.labelsArr[repres_l1]
