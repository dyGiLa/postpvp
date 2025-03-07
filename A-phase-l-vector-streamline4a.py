# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
solution_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='solution_00.pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/xyzAdGR/VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-monople-config-run-4/refine-cycle_2/solution_09.pvtu'])
solution_00pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# Properties modified on solution_00pvtu
solution_00pvtu.PointArrayStatus = ['subdomain', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33']
solution_00pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solution_00pvtuDisplay = Show(solution_00pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
solution_00pvtuDisplay.Representation = 'Surface'
solution_00pvtuDisplay.ColorArrayName = [None, '']
solution_00pvtuDisplay.SelectTCoordArray = 'None'
solution_00pvtuDisplay.SelectNormalArray = 'None'
solution_00pvtuDisplay.SelectTangentArray = 'None'
solution_00pvtuDisplay.OSPRayScaleArray = 'subdomain'
solution_00pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution_00pvtuDisplay.SelectOrientationVectors = 'None'
solution_00pvtuDisplay.ScaleFactor = 3.6
solution_00pvtuDisplay.SelectScaleArray = 'None'
solution_00pvtuDisplay.GlyphType = 'Arrow'
solution_00pvtuDisplay.GlyphTableIndexArray = 'None'
solution_00pvtuDisplay.GaussianRadius = 0.18
solution_00pvtuDisplay.SetScaleArray = ['POINTS', 'subdomain']
solution_00pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution_00pvtuDisplay.OpacityArray = ['POINTS', 'subdomain']
solution_00pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution_00pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution_00pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
solution_00pvtuDisplay.ScalarOpacityUnitDistance = 0.8694017339527222
solution_00pvtuDisplay.OpacityArrayName = ['POINTS', 'subdomain']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution_00pvtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution_00pvtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=solution_00pvtu)
mergeVectorComponents1.XArray = 'subdomain'
mergeVectorComponents1.YArray = 'subdomain'
mergeVectorComponents1.ZArray = 'subdomain'

# Properties modified on mergeVectorComponents1
mergeVectorComponents1.XArray = 'u_11'
mergeVectorComponents1.YArray = 'u_12'
mergeVectorComponents1.ZArray = 'u_13'
mergeVectorComponents1.OutputVectorName = 'M'

# show data in view
mergeVectorComponents1Display = Show(mergeVectorComponents1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents1Display.Representation = 'Surface'
mergeVectorComponents1Display.ColorArrayName = [None, '']
mergeVectorComponents1Display.SelectTCoordArray = 'None'
mergeVectorComponents1Display.SelectNormalArray = 'None'
mergeVectorComponents1Display.SelectTangentArray = 'None'
mergeVectorComponents1Display.OSPRayScaleArray = 'M'
mergeVectorComponents1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.SelectOrientationVectors = 'M'
mergeVectorComponents1Display.ScaleFactor = 3.6
mergeVectorComponents1Display.SelectScaleArray = 'M'
mergeVectorComponents1Display.GlyphType = 'Arrow'
mergeVectorComponents1Display.GlyphTableIndexArray = 'M'
mergeVectorComponents1Display.GaussianRadius = 0.18
mergeVectorComponents1Display.SetScaleArray = ['POINTS', 'M']
mergeVectorComponents1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.OpacityArray = ['POINTS', 'M']
mergeVectorComponents1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents1Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents1Display.ScalarOpacityUnitDistance = 0.8694017339527222
mergeVectorComponents1Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# hide data in view
Hide(solution_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(solution_00pvtu)

# create a new 'Merge Vector Components'
mergeVectorComponents2 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=solution_00pvtu)
mergeVectorComponents2.XArray = 'subdomain'
mergeVectorComponents2.YArray = 'subdomain'
mergeVectorComponents2.ZArray = 'subdomain'

# Properties modified on mergeVectorComponents2
mergeVectorComponents2.XArray = 'v_11'
mergeVectorComponents2.YArray = 'v_12'
mergeVectorComponents2.ZArray = 'v_13'
mergeVectorComponents2.OutputVectorName = 'N'

# show data in view
mergeVectorComponents2Display = Show(mergeVectorComponents2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents2Display.Representation = 'Surface'
mergeVectorComponents2Display.ColorArrayName = [None, '']
mergeVectorComponents2Display.SelectTCoordArray = 'None'
mergeVectorComponents2Display.SelectNormalArray = 'None'
mergeVectorComponents2Display.SelectTangentArray = 'None'
mergeVectorComponents2Display.OSPRayScaleArray = 'N'
mergeVectorComponents2Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.SelectOrientationVectors = 'N'
mergeVectorComponents2Display.ScaleFactor = 3.6
mergeVectorComponents2Display.SelectScaleArray = 'N'
mergeVectorComponents2Display.GlyphType = 'Arrow'
mergeVectorComponents2Display.GlyphTableIndexArray = 'N'
mergeVectorComponents2Display.GaussianRadius = 0.18
mergeVectorComponents2Display.SetScaleArray = ['POINTS', 'N']
mergeVectorComponents2Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.OpacityArray = ['POINTS', 'N']
mergeVectorComponents2Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents2Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents2Display.ScalarOpacityUnitDistance = 0.8694017339527222
mergeVectorComponents2Display.OpacityArrayName = ['POINTS', 'N']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents2Display.ScaleTransferFunction.Points = [-1.4717285633087158, 0.0, 0.5, 0.0, 1.5255942344665527, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents2Display.OpacityTransferFunction.Points = [-1.4717285633087158, 0.0, 0.5, 0.0, 1.5255942344665527, 1.0, 0.5, 0.0]

# hide data in view
Hide(solution_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

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
appendAttributes1Display.OSPRayScaleArray = 'M'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'M'
appendAttributes1Display.ScaleFactor = 3.6
appendAttributes1Display.SelectScaleArray = 'M'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'M'
appendAttributes1Display.GaussianRadius = 0.18
appendAttributes1Display.SetScaleArray = ['POINTS', 'M']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'M']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityUnitDistance = 0.8694017339527222
appendAttributes1Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

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
calculator1.Function = 'cross(m,n)/((2.49733/sqrt(2))^2)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'M'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'M'
calculator1Display.ScaleFactor = 3.6
calculator1Display.SelectScaleArray = 'M'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'M'
calculator1Display.GaussianRadius = 0.18
calculator1Display.SetScaleArray = ['POINTS', 'M']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'M']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 0.8694017339527222
calculator1Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# hide data in view
Hide(appendAttributes1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator1
calculator1.Function = 'cross(m,n)/((2.49733/1.414213562)^2)'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculator1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'M']
streamTracer1.MaximumStreamlineLength = 36.0

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-15.0, -15.0, -18.0]
streamTracer1.SeedType.Point2 = [15.0, 15.0, 18.0]

# set active source
SetActiveSource(calculator1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1.SeedType)

# set active source
SetActiveSource(streamTracer1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer1.SeedType)

# set active source
SetActiveSource(calculator1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1.SeedType)

# destroy streamTracer1
Delete(streamTracer1)
del streamTracer1

# set active source
SetActiveSource(calculator1)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculator1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'M']
streamTracer1.MaximumStreamlineLength = 36.0

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-15.0, -15.0, -18.0]
streamTracer1.SeedType.Point2 = [15.0, 15.0, 18.0]

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
renderView1.CameraPosition = [1.4531126335591424, -1.2060234122020774, 107.47494252818495]
renderView1.CameraViewUp = [0.00013272156044969255, 0.9999370569344592, 0.011218937304376403]
renderView1.CameraParallelScale = 27.820855486487112

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
