from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase

from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkCommonExecutionModel import vtkDataObject

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

import sys
import os
sys.path.append("/home/heidi/Documents/SCC-GL-calculator")
import Module_GLSCC_calculator as sc

import numpy as np
np.set_printoptions(precision=10)

                
data=inputs[0]
pMarker_Array=data.PointData['phaseMarker'][0:1024]

print("pMarker_Array.shape : ", pMarker_Array.shape, "\n")

Nofelem = pMarker_Array.shape[0]

print("Nofelem : ", Nofelem, "\n")

# side dimension of corresponding lattice
dim = np.rint(np.power(Nofelem, 1/3)).astype(int)
print("dim : ", dim)
        
# cluster labeling array, same lattice
labels = np.zeros_like(pMarker_Array, dtype=int)
print("labels.shape = ", labels.shape)

# primary labelsArr, init with size dim
# labelsArr = np.zeros(dim*dim*dim, dtype=int)
labelsArr = np.zeros_like(pMarker_Array, dtype=int)
print("labelsArr.shape = ", labelsArr.shape)

# relabeled labelsArr
# labelsArrRelabel must be initialized as zero array
labelsArrRelabel = np.zeros_like(labelsArr, dtype=int)
print("labelsArrRelabel.shape = ", labelsArrRelabel.shape)

# ==== uf functions : ====

# union-find altorithm: find fuc
def uf_find(x):
    """
    Find root of label x with path compression.
    """
    y = x
    while labelsArr[y] != y:
        y = labelsArr[y]

    while labelsArr[x] != x:
        z = labelsArr[x]
        labelsArr[x] = y
        x = z
            
    return y
        
# union-find altorithm: union fuc
def uf_union(l1, l2):
    """
    Union two labels.
    """
    # find() return label
    repres_l2 = uf_find(l2)
    repres_l1 = uf_find(l1)

    labelsArr[repres_l1] = repres_l2
    return labelsArr[repres_l1]

        
"""Run Hoshen-Kopelman algorithm."""
pM = 5.

for zidx in np.arange(dim):
    for yidx in np.arange(dim):
        for xidx in np.arange(dim):

            # convert 3d indices to 1d array index
            idxArray = zidx * (dim * dim) + yidx * dim + xidx
            idx_zn1_Array = (zidx-1) * (dim * dim) + yidx * dim + xidx
            idx_yn1_Array = zidx * (dim * dim) + (yidx-1) * dim + xidx
            idx_xn1_Array = zidx * (dim * dim) + yidx * dim + (xidx-1)

            print("zidx = ", zidx, ", yidx = ", yidx, ", xidx = ", xidx, "\n")
            print("pMarker_Array[idxArray] = ", pMarker_Array[idxArray], "\n")            
            print("idxArray = ", idxArray, "\n")
            print("idx_zn1_Array = ", idx_zn1_Array, "\n")
            print("idx_yn1_Array = ", idx_yn1_Array, "\n")
            print("idx_xn1_Array = ", idx_xn1_Array, "\n")

            print("labels : ", labels, "\n")
            print("labelsArr : ", labelsArr, "\n")            
                    
            if pMarker_Array[idxArray] == pM:
                # Check back beighbor

                # zidx = 0 is first slice of x-y, not peridic no neighbor, then zidx > 0
                if zidx > 0 and labels[idx_zn1_Array] > 0:
                    back = labels[idx_zn1_Array]
                else:
                    back = 0

                print("back = ", back)     

                # yidx = 0 is first row in x-y plane, not peridic no neighbor, then yidx > 0
                if yidx > 0 and labels[idx_yn1_Array] > 0:
                    top = labels[idx_yn1_Array]
                else:
                    top = 0

                print("back = ", top)                         

                # xidx = 0 is first column in x-y plane, not peridic no neighbor, then xidx > 0                
                if xidx > 0 and labels[idx_xn1_Array] > 0:
                    left = labels[idx_xn1_Array]
                else:
                    left = 0

                print("left = ", left)                                             

                if (back == 0) and (top == 0) and (left==0):
                    # New label, if no occupied neighbor
                    labelsArr[0] += 1
                    labelsArr[labelsArr[0]] = labelsArr[0]
                    labels[idxArray] = labelsArr[0]
                            
                elif (((back != 0) and (top == 0) and (left==0))
                      or ((back ==0) and (top != 0) and (left==0))
                      or ((back == 0) and (top == 0) and (left != 0))):
                    # occupied site has one neighbors
                    labels[idxArray] = np.max(np.array([back, top, left]))
                            
                elif ((back != 0) and (top != 0) and (left==0)):
                    # two neighbors: back n top
                    labels[idxArray] = uf_union(top, back)
                            
                elif ((back != 0) and (top == 0) and (left != 0)):
                    # two neighbors: back n left
                    labels[idxArray] = uf_union(left, back)
                            
                elif ((back == 0) and (top != 0) and (left != 0)):
                    # two neighbors: back n left
                    labels[idxArray] = uf_union(left, top)
                            
                else:
                    # three neighbors
                    equvlent_repres = uf_union(top, back)
                    labels[idxArray] = uf_union(left, equvlent_repres)
                                 
             
# print("labels :")
# print(.labels, "\n")
print("labelsArr :")
print(labelsArr, "\n")        
                        
# Second pass: re-label labels Array
for zidx in range(dim):
    for yidx in range(dim):
        for xidx in range(dim):

            # convert 3d indices to 1d array index
            idxArray = zidx * (dim * dim) + yidx * dim + xidx
                    
            if labels[idxArray] != 0:
                repres_idx=uf_find(labels[idxArray])
                if labelsArrRelabel[repres_idx] == 0:
                    labelsArrRelabel[0] += 1
                    labelsArrRelabel[repres_idx] = labelsArrRelabel[0]
                    labels[idxArray]=labelsArrRelabel[repres_idx]

print("labelsArrRelabel :")
print(labelsArrRelabel, "\n")

print("labels :", labels)

        
