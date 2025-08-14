# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
labeledclusterspvd = FindSource('labeled-clusters.pvd')

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=labeledclusterspvd)

# Properties modified on threshold1
threshold1.UpperThreshold = 1.0

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'

# hide data in view
Hide(labeledclusterspvd, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'Labeledclusters'
labeledclustersTF2D = GetTransferFunction2D('Labeledclusters')

# get color transfer function/color map for 'Labeledclusters'
labeledclustersLUT = GetColorTransferFunction('Labeledclusters')
labeledclustersLUT.TransferFunction2D = labeledclustersTF2D
labeledclustersLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 294.0, 0.865003, 0.865003, 0.865003, 588.0, 0.705882, 0.0156863, 0.14902]
labeledclustersLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Labeledclusters'
labeledclustersPWF = GetOpacityTransferFunction('Labeledclusters')
labeledclustersPWF.Points = [0.0, 0.0, 0.5, 0.0, 588.0, 1.0, 0.5, 0.0]
labeledclustersPWF.ScalarRangeInitialized = 1

# Properties modified on threshold1Display.DataAxesGrid
threshold1Display.DataAxesGrid.GridAxesVisibility = 1

renderView1.ApplyIsometricView()

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.05

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.01

# Rescale transfer function
labeledclustersLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
labeledclustersPWF.RescaleTransferFunction(0.0, 1.0)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
labeledclustersLUT.ApplyPreset('Cool to Warm (Extended)', True)

# Properties modified on labeledclustersLUT
labeledclustersLUT.NumberOfTableValues = 2

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
renderView1.CameraPosition = [624.5675694550702, 613.3539871767686, 630.6466565746248]
renderView1.CameraFocalPoint = [129.2948317195824, 118.08124944128076, 135.37391883913693]
renderView1.CameraViewUp = [-0.4082482904638631, 0.816496580927726, -0.40824829046386296]
renderView1.CameraParallelScale = 222.0246943435797


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