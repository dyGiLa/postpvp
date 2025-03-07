# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
calculator1 = FindSource('Calculator1')

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=calculator1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'gap']
clip1.Value = 2.489373695662491

# find source
solution_01pvtu = FindSource('solution_01.pvtu')

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'gap'
gapLUT = GetColorTransferFunction('gap')
gapLUT.RGBPoints = [2.3774185224056135, 0.231373, 0.298039, 0.752941, 2.489373695662491, 0.865003, 0.865003, 0.865003, 2.6013288689193677, 0.705882, 0.0156863, 0.14902]
gapLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'gap'
gapPWF = GetOpacityTransferFunction('gap')
gapPWF.Points = [2.3774185224056135, 0.0, 0.5, 0.0, 2.6013288689193677, 1.0, 0.5, 0.0]
gapPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'gap']
clip1Display.LookupTable = gapLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'gap'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 4.0
clip1Display.SelectScaleArray = 'gap'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'gap'
clip1Display.GaussianRadius = 0.2
clip1Display.SetScaleArray = ['POINTS', 'gap']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'gap']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = gapPWF
clip1Display.ScalarOpacityUnitDistance = 1.1236866521719455
clip1Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [2.3774299984419076, 0.0, 0.5, 0.0, 2.6013288689193677, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [2.3774299984419076, 0.0, 0.5, 0.0, 2.6013288689193677, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1Display.DataAxesGrid
clip1Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on clip1Display.DataAxesGrid
clip1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
clip1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
clip1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
clip1Display.DataAxesGrid.XTitleFontFamily = 'Times'
clip1Display.DataAxesGrid.XTitleBold = 1
clip1Display.DataAxesGrid.XTitleFontSize = 22
clip1Display.DataAxesGrid.YTitleFontFamily = 'Times'
clip1Display.DataAxesGrid.YTitleBold = 1
clip1Display.DataAxesGrid.YTitleFontSize = 22
clip1Display.DataAxesGrid.ZTitleFontFamily = 'Times'
clip1Display.DataAxesGrid.ZTitleBold = 1
clip1Display.DataAxesGrid.ZTitleFontSize = 22
clip1Display.DataAxesGrid.XLabelFontFamily = 'Times'
clip1Display.DataAxesGrid.XLabelBold = 1
clip1Display.DataAxesGrid.XLabelFontSize = 18
clip1Display.DataAxesGrid.YLabelFontFamily = 'Times'
clip1Display.DataAxesGrid.YLabelBold = 1
clip1Display.DataAxesGrid.YLabelFontSize = 18
clip1Display.DataAxesGrid.ZLabelFontFamily = 'Times'
clip1Display.DataAxesGrid.ZLabelBold = 1
clip1Display.DataAxesGrid.ZLabelFontSize = 1

# get color legend/bar for gapLUT in view renderView1
gapLUTColorBar = GetScalarBar(gapLUT, renderView1)
gapLUTColorBar.WindowLocation = 'Upper Right Corner'
gapLUTColorBar.Title = 'gap'
gapLUTColorBar.ComponentTitle = ''

# change scalar bar placement
gapLUTColorBar.WindowLocation = 'Any Location'
gapLUTColorBar.Position = [0.8530440867739678, 0.49375]
gapLUTColorBar.ScalarBarLength = 0.32999999999999996

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1429, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, -0.6354454743162429, 113.26921461638914]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraViewUp = [0.0, 0.9999842640648654, 0.005609957455249585]
renderView1.CameraParallelScale = 29.316691292078854

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).