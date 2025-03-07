# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
solution_12pvtu = XMLPartitionedUnstructuredGridReader(registrationName='solution_12.pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/test-after-lumi-update/test-afterlumi-update-III/refine-cycle_0/solution_08.pvtu'])
solution_12pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# Properties modified on solution_12pvtu
solution_12pvtu.PointArrayStatus = ['subdomain', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33']
solution_12pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solution_12pvtuDisplay = Show(solution_12pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
solution_12pvtuDisplay.Representation = 'Surface'
solution_12pvtuDisplay.ColorArrayName = [None, '']
solution_12pvtuDisplay.SelectTCoordArray = 'None'
solution_12pvtuDisplay.SelectNormalArray = 'None'
solution_12pvtuDisplay.SelectTangentArray = 'None'
solution_12pvtuDisplay.OSPRayScaleArray = 'subdomain'
solution_12pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution_12pvtuDisplay.SelectOrientationVectors = 'None'
solution_12pvtuDisplay.ScaleFactor = 6.0
solution_12pvtuDisplay.SelectScaleArray = 'None'
solution_12pvtuDisplay.GlyphType = 'Arrow'
solution_12pvtuDisplay.GlyphTableIndexArray = 'None'
solution_12pvtuDisplay.GaussianRadius = 0.3
solution_12pvtuDisplay.SetScaleArray = ['POINTS', 'subdomain']
solution_12pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution_12pvtuDisplay.OpacityArray = ['POINTS', 'subdomain']
solution_12pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution_12pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution_12pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
solution_12pvtuDisplay.ScalarOpacityUnitDistance = 5.153882032022076
solution_12pvtuDisplay.OpacityArrayName = ['POINTS', 'subdomain']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution_12pvtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution_12pvtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=solution_12pvtu)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'gap'
calculator1.Function = 'sqrt(u_11^2+u_12^2+u_13^2+u_21^2+u_22^2+u_23^2+u_31^2+u_32^2+u_33^2+v_11^2+v_12^2+v_13^2+v_21^2+v_22^2+v_23^2+v_31^2+v_32^2+v_33^2)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'gap'
gapLUT = GetColorTransferFunction('gap')
gapLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.2615471917570853, 0.865003, 0.865003, 0.865003, 2.5230943835141706, 0.705882, 0.0156863, 0.14902]
gapLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'gap'
gapPWF = GetOpacityTransferFunction('gap')
gapPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.5230943835141706, 1.0, 0.5, 0.0]
gapPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'gap']
calculator1Display.LookupTable = gapLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'gap'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 6.0
calculator1Display.SelectScaleArray = 'gap'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'gap'
calculator1Display.GaussianRadius = 0.3
calculator1Display.SetScaleArray = ['POINTS', 'gap']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'gap']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = gapPWF
calculator1Display.ScalarOpacityUnitDistance = 5.153882032022076
calculator1Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5230943835141706, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5230943835141706, 1.0, 0.5, 0.0]

# hide data in view
Hide(solution_12pvtu, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on calculator1Display.DataAxesGrid
calculator1Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on calculator1Display.DataAxesGrid
calculator1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_0$'
calculator1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_0$'
calculator1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_0$'
calculator1Display.DataAxesGrid.XTitleFontFamily = 'Times'
calculator1Display.DataAxesGrid.XTitleBold = 1
calculator1Display.DataAxesGrid.XTitleFontSize = 24
calculator1Display.DataAxesGrid.YTitleFontFamily = 'Times'
calculator1Display.DataAxesGrid.YTitleBold = 1
calculator1Display.DataAxesGrid.YTitleFontSize = 24
calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Times'
calculator1Display.DataAxesGrid.ZTitleBold = 1
calculator1Display.DataAxesGrid.ZTitleFontSize = 24
calculator1Display.DataAxesGrid.XLabelFontFamily = 'Times'
calculator1Display.DataAxesGrid.XLabelBold = 1
calculator1Display.DataAxesGrid.XLabelFontSize = 18
calculator1Display.DataAxesGrid.YLabelFontFamily = 'Times'
calculator1Display.DataAxesGrid.YLabelBold = 1
calculator1Display.DataAxesGrid.YLabelFontSize = 18
calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Times'
calculator1Display.DataAxesGrid.ZLabelBold = 1
calculator1Display.DataAxesGrid.ZLabelFontSize = 18

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1935, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-159.3045683320738, 0.0, 0.0]
renderView1.CameraFocalPoint = [1e-20, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 41.23105625617661

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
