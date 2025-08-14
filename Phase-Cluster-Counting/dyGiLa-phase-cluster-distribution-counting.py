# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'

LoadPlugin("/home/heidi/Documents/dyGiLa-project/dyGiLa-pvpython-scripts/Phase-Cluster-Counting/Cluster-Counting-HK.py", False, globals()) 

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Image Data Reader'
piopvti = XMLPartitionedImageDataReader(registrationName='pio.pvti', FileName=['/home/heidi/Documents/dyGiLa-project/dyGiLa-pvpython-scripts/Phase-Cluster-Counting/hdf5-to-vtu/pio.pvti'])

# Properties modified on piopvti
piopvti.CellArrayStatus = []
piopvti.PointArrayStatus = ['phaseMarker']
piopvti.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
piopvtiDisplay = Show(piopvti, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
piopvtiDisplay.Representation = 'Outline'

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Cluster-Counting-HK Filter'
clusterCountingHKFilter1 = ClusterCountingHKFilter(registrationName='ClusterCountingHKFilter1', Input=piopvti)

# Properties modified on clusterCountingHKFilter1
clusterCountingHKFilter1.phase_Marker = 5.0

# show data in view
clusterCountingHKFilter1Display = Show(clusterCountingHKFilter1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
clusterCountingHKFilter1Display.Representation = 'Surface'

# hide data in view
Hide(piopvti, renderView1)

# show color bar/color legend
clusterCountingHKFilter1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Labeledclusters'
labeledclustersLUT = GetColorTransferFunction('Labeledclusters')

# get opacity transfer function/opacity map for 'Labeledclusters'
labeledclustersPWF = GetOpacityTransferFunction('Labeledclusters')

# get 2D transfer function for 'Labeledclusters'
labeledclustersTF2D = GetTransferFunction2D('Labeledclusters')

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=clusterCountingHKFilter1)

# Properties modified on programmableFilter1
programmableFilter1.Script = """from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

import numpy as np
from collections import Counter

import matplotlib.pyplot as plt

labeled_pMCluster_Arr=inputs[0].PointData[\'Labeled-clusters\']

print("pMarker_Array : ", labeled_pMCluster_Arr)

# Get only the non-zero (occupied) labels
labels = labeled_pMCluster_Arr[labeled_pMCluster_Arr > 0]

# Count how many times each label appears (i.e., cluster size)
label_counts = Counter(labels)

# Now count how many clusters are of each size
size_distribution = Counter(label_counts.values())

total_clusters = np.sum(list(size_distribution.values()))
normalized_dist = {size: count / total_clusters for size, count in size_distribution.items()}

sizes = np.array(sorted(normalized_dist.keys()), dtype=float)
probs = [normalized_dist[size] for size in sizes]

sizes2 = np.array(sorted(size_distribution.keys()),dtype=float)
sizesNum = [size_distribution[size] for size in sizes2]

# Stack as rows first
combined = np.vstack((sizes, probs, sizes2, sizesNum))

# Transpose to get desired shape
combined = combined.T

# Save to CSV
np.savetxt("/home/heidi/Documents/dyGiLa-project/dyGiLa-pvpython-scripts/Phase-Cluster-Counting/cluster-prob-num.csv", combined, delimiter=",", fmt="%.8f")

print("csv saved.")

#########################

fig, ax = plt.subplots(1,1)

#ax.plot(sizes, probs, marker=\'o\', linestyle=\'-\', color=\'blue\')
ax.scatter(sizes*(0.5**3), probs, marker=\'o\', color=\'blue\')
ax.set_xscale(\'log\')
ax.set_yscale(\'log\')
ax.set_ylim(10**-3, 1)
ax.set_xlabel(r\'cluster Size $cs$/$\\xi^{3}_{GL_{0}}$\')
ax.set_ylabel(\'Fraction $p(cs)$\')
ax.set_title(\'Cluster Size Probability Distribution\')
ax.grid(True, which="major", ls="-")

fig.savefig(\'/home/heidi/Documents/dyGiLa-project/dyGiLa-pvpython-scripts/Phase-Cluster-Counting/cluster_prob_distribution.png\')

##########################

fig2, ax2 = plt.subplots(1,1)

#ax.plot(sizes2, sizesNum, marker=\'o\', linestyle=\'-\', color=\'blue\')
ax2.scatter(sizes2*(0.5**3), sizesNum, marker=\'o\', color=\'blue\')
ax2.set_xscale(\'log\')
ax2.set_yscale(\'linear\')
ax2.set_xlabel(r\'Cluster Size/$\\xi^{3}_{GL_{0}}$\')
ax2.set_ylabel(\'Number\')
ax2.set_title(\'Cluster Size Distribution\')
ax2.grid(True, which="major", ls="-")

fig2.savefig(\'/home/heidi/Documents/dyGiLa-project/dyGiLa-pvpython-scripts/Phase-Cluster-Counting/cluster_num_distribution.png\')"""
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# show data in view
programmableFilter1Display = Show(programmableFilter1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
programmableFilter1Display.Representation = 'Surface'

# hide data in view
Hide(clusterCountingHKFilter1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1529, 1087)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [63.25, 63.25, 493.2193801212333]
renderView1.CameraFocalPoint = [63.25, 63.25, 63.25]
renderView1.CameraParallelScale = 111.28426438630036


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
