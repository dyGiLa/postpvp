# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
solution_05pvtu = XMLPartitionedUnstructuredGridReader(registrationName='solution_05.pvtu', FileName=['/home/heidi/Documents/VerHem-repo_and_data/visualization-and-data/xyzAdGR/VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-monople-config-run-3/refine-cycle_0/solution_05.pvtu'])
solution_05pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# Properties modified on solution_05pvtu
solution_05pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solution_05pvtuDisplay = Show(solution_05pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
solution_05pvtuDisplay.Representation = 'Surface'
solution_05pvtuDisplay.ColorArrayName = [None, '']
solution_05pvtuDisplay.SelectTCoordArray = 'None'
solution_05pvtuDisplay.SelectNormalArray = 'None'
solution_05pvtuDisplay.SelectTangentArray = 'None'
solution_05pvtuDisplay.OSPRayScaleArray = 'du_11'
solution_05pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution_05pvtuDisplay.SelectOrientationVectors = 'None'
solution_05pvtuDisplay.ScaleFactor = 4.0
solution_05pvtuDisplay.SelectScaleArray = 'None'
solution_05pvtuDisplay.GlyphType = 'Arrow'
solution_05pvtuDisplay.GlyphTableIndexArray = 'None'
solution_05pvtuDisplay.GaussianRadius = 0.2
solution_05pvtuDisplay.SetScaleArray = ['POINTS', 'du_11']
solution_05pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution_05pvtuDisplay.OpacityArray = ['POINTS', 'du_11']
solution_05pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution_05pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution_05pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
solution_05pvtuDisplay.ScalarOpacityUnitDistance = 4.330127018922194
solution_05pvtuDisplay.OpacityArrayName = ['POINTS', 'du_11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution_05pvtuDisplay.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution_05pvtuDisplay.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=solution_05pvtu)
mergeVectorComponents1.XArray = 'du_11'
mergeVectorComponents1.YArray = 'du_11'
mergeVectorComponents1.ZArray = 'du_11'

# Properties modified on mergeVectorComponents1
mergeVectorComponents1.XArray = 'u_11'
mergeVectorComponents1.YArray = 'u_12'
mergeVectorComponents1.ZArray = 'u_13'
mergeVectorComponents1.OutputVectorName = 'm'

# show data in view
mergeVectorComponents1Display = Show(mergeVectorComponents1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents1Display.Representation = 'Surface'
mergeVectorComponents1Display.ColorArrayName = [None, '']
mergeVectorComponents1Display.SelectTCoordArray = 'None'
mergeVectorComponents1Display.SelectNormalArray = 'None'
mergeVectorComponents1Display.SelectTangentArray = 'None'
mergeVectorComponents1Display.OSPRayScaleArray = 'du_11'
mergeVectorComponents1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.SelectOrientationVectors = 'None'
mergeVectorComponents1Display.ScaleFactor = 4.0
mergeVectorComponents1Display.SelectScaleArray = 'None'
mergeVectorComponents1Display.GlyphType = 'Arrow'
mergeVectorComponents1Display.GlyphTableIndexArray = 'None'
mergeVectorComponents1Display.GaussianRadius = 0.2
mergeVectorComponents1Display.SetScaleArray = ['POINTS', 'du_11']
mergeVectorComponents1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.OpacityArray = ['POINTS', 'du_11']
mergeVectorComponents1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents1Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents1Display.ScalarOpacityUnitDistance = 4.330127018922194
mergeVectorComponents1Display.OpacityArrayName = ['POINTS', 'du_11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents1Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents1Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# hide data in view
Hide(solution_05pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(solution_05pvtu)

# create a new 'Merge Vector Components'
mergeVectorComponents2 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=solution_05pvtu)
mergeVectorComponents2.XArray = 'du_11'
mergeVectorComponents2.YArray = 'du_11'
mergeVectorComponents2.ZArray = 'du_11'

# Properties modified on mergeVectorComponents2
mergeVectorComponents2.XArray = 'v_11'
mergeVectorComponents2.YArray = 'v_12'
mergeVectorComponents2.ZArray = 'v_13'
mergeVectorComponents2.OutputVectorName = 'n'

# show data in view
mergeVectorComponents2Display = Show(mergeVectorComponents2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents2Display.Representation = 'Surface'
mergeVectorComponents2Display.ColorArrayName = [None, '']
mergeVectorComponents2Display.SelectTCoordArray = 'None'
mergeVectorComponents2Display.SelectNormalArray = 'None'
mergeVectorComponents2Display.SelectTangentArray = 'None'
mergeVectorComponents2Display.OSPRayScaleArray = 'du_11'
mergeVectorComponents2Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.SelectOrientationVectors = 'None'
mergeVectorComponents2Display.ScaleFactor = 4.0
mergeVectorComponents2Display.SelectScaleArray = 'None'
mergeVectorComponents2Display.GlyphType = 'Arrow'
mergeVectorComponents2Display.GlyphTableIndexArray = 'None'
mergeVectorComponents2Display.GaussianRadius = 0.2
mergeVectorComponents2Display.SetScaleArray = ['POINTS', 'du_11']
mergeVectorComponents2Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.OpacityArray = ['POINTS', 'du_11']
mergeVectorComponents2Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents2Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents2Display.ScalarOpacityUnitDistance = 4.330127018922194
mergeVectorComponents2Display.OpacityArrayName = ['POINTS', 'du_11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents2Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents2Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# hide data in view
Hide(solution_05pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mergeVectorComponents1)

# set active source
SetActiveSource(mergeVectorComponents2)

# set active source
SetActiveSource(mergeVectorComponents1)

# set active source
SetActiveSource(mergeVectorComponents2)

# set active source
SetActiveSource(mergeVectorComponents1)

# set active source
SetActiveSource(mergeVectorComponents2)

# set active source
SetActiveSource(mergeVectorComponents1)

# set active source
SetActiveSource(mergeVectorComponents2)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[mergeVectorComponents1, mergeVectorComponents2])

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Surface'
appendAttributes1Display.ColorArrayName = [None, '']
appendAttributes1Display.SelectTCoordArray = 'None'
appendAttributes1Display.SelectNormalArray = 'None'
appendAttributes1Display.SelectTangentArray = 'None'
appendAttributes1Display.OSPRayScaleArray = 'du_11'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'None'
appendAttributes1Display.ScaleFactor = 4.0
appendAttributes1Display.SelectScaleArray = 'None'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'None'
appendAttributes1Display.GaussianRadius = 0.2
appendAttributes1Display.SetScaleArray = ['POINTS', 'du_11']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'du_11']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityUnitDistance = 4.330127018922194
appendAttributes1Display.OpacityArrayName = ['POINTS', 'du_11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# hide data in view
Hide(mergeVectorComponents2, renderView1)

# hide data in view
Hide(mergeVectorComponents1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=appendAttributes1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'l'
calculator1.Function = 'cross(m,n)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'du_11'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'l'
calculator1Display.ScaleFactor = 4.0
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.GaussianRadius = 0.2
calculator1Display.SetScaleArray = ['POINTS', 'du_11']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'du_11']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 4.330127018922194
calculator1Display.OpacityArrayName = ['POINTS', 'du_11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]

# hide data in view
Hide(appendAttributes1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculator1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'l']
streamTracer1.MaximumStreamlineLength = 40.0

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-20.0, -20.0, -20.0]
streamTracer1.SeedType.Point2 = [20.0, 20.0, 20.0]

streamTracer1.Radius = 40
streamTracer1.NumberOfPoints = 4000

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer1.SeedType)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1.SeedType)

# Properties modified on streamTracer1
streamTracer1.SeedType = 'Point Cloud'

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 3.999578666687012
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.1999789333343506
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-0.03466842463004143, 0.0, 0.5, 0.0, 0.03743072679768799, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-0.03466842463004143, 0.0, 0.5, 0.0, 0.03743072679768799, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on streamTracer1Display.DataAxesGrid
streamTracer1Display.DataAxesGrid.GridAxesVisibility = 1

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.3999578666687012

# Properties modified on tube1
tube1.Vectors = ['POINTS', 'l']
tube1.Radius = 0.18

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.ScaleFactor = 4.0022422790527346
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.GaussianRadius = 0.20011211395263673
tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-0.03466842463004143, 0.0, 0.5, 0.0, 0.03743072679768799, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-0.03466842463004143, 0.0, 0.5, 0.0, 0.03743072679768799, 1.0, 0.5, 0.0]

# hide data in view
Hide(streamTracer1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on tube1Display.DataAxesGrid
tube1Display.DataAxesGrid.GridAxesVisibility = 1

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'l', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'l'
lLUT = GetColorTransferFunction('l')
lLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.5877108876896935, 0.865003, 0.865003, 0.865003, 3.175421775379387, 0.705882, 0.0156863, 0.14902]
lLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'l'
lPWF = GetOpacityTransferFunction('l')
lPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.175421775379387, 1.0, 0.5, 0.0]
lPWF.ScalarRangeInitialized = 1

# Properties modified on tube1Display.DataAxesGrid
tube1Display.DataAxesGrid.XTitle = '$x/\\xi^GL_{0}$'
tube1Display.DataAxesGrid.YTitle = '$y/\\xi^GL_{0}$'
tube1Display.DataAxesGrid.ZTitle = '$z/\\xi^GL_{0}$'
tube1Display.DataAxesGrid.XTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.XTitleBold = 1
tube1Display.DataAxesGrid.XTitleFontSize = 22
tube1Display.DataAxesGrid.YTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.YTitleBold = 1
tube1Display.DataAxesGrid.YTitleFontSize = 22
tube1Display.DataAxesGrid.ZTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.ZTitleBold = 1
tube1Display.DataAxesGrid.ZTitleFontSize = 22
tube1Display.DataAxesGrid.XLabelFontFamily = 'Times'
tube1Display.DataAxesGrid.XLabelBold = 1
tube1Display.DataAxesGrid.XLabelFontSize = 18
tube1Display.DataAxesGrid.YLabelFontFamily = 'Times'
tube1Display.DataAxesGrid.YLabelBold = 1
tube1Display.DataAxesGrid.YLabelFontSize = 18
tube1Display.DataAxesGrid.ZLabelFontFamily = 'Times'
tube1Display.DataAxesGrid.ZLabelBold = 1
tube1Display.DataAxesGrid.ZLabelFontSize = 17

# Properties modified on tube1Display.DataAxesGrid
tube1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1859, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 133.84260859804928]
renderView1.CameraParallelScale = 34.64101615137755

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).