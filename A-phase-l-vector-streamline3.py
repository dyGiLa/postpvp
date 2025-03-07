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
solution_05pvtu.CellArrayStatus = []
solution_05pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']
solution_05pvtu.TimeArray = 'TimeValue'

# Properties modified on solution_05pvtu
solution_05pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solution_05pvtuDisplay = Show(solution_05pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
solution_05pvtuDisplay.Selection = None
solution_05pvtuDisplay.Representation = 'Surface'
solution_05pvtuDisplay.ColorArrayName = [None, '']
solution_05pvtuDisplay.LookupTable = None
solution_05pvtuDisplay.MapScalars = 1
solution_05pvtuDisplay.MultiComponentsMapping = 0
solution_05pvtuDisplay.InterpolateScalarsBeforeMapping = 1
solution_05pvtuDisplay.Opacity = 1.0
solution_05pvtuDisplay.PointSize = 2.0
solution_05pvtuDisplay.LineWidth = 1.0
solution_05pvtuDisplay.RenderLinesAsTubes = 0
solution_05pvtuDisplay.RenderPointsAsSpheres = 0
solution_05pvtuDisplay.Interpolation = 'Gouraud'
solution_05pvtuDisplay.Specular = 0.0
solution_05pvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.SpecularPower = 100.0
solution_05pvtuDisplay.Luminosity = 0.0
solution_05pvtuDisplay.Ambient = 0.0
solution_05pvtuDisplay.Diffuse = 1.0
solution_05pvtuDisplay.Roughness = 0.3
solution_05pvtuDisplay.Metallic = 0.0
solution_05pvtuDisplay.EdgeTint = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.Anisotropy = 0.0
solution_05pvtuDisplay.AnisotropyRotation = 0.0
solution_05pvtuDisplay.BaseIOR = 1.5
solution_05pvtuDisplay.CoatStrength = 0.0
solution_05pvtuDisplay.CoatIOR = 2.0
solution_05pvtuDisplay.CoatRoughness = 0.0
solution_05pvtuDisplay.CoatColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.SelectTCoordArray = 'None'
solution_05pvtuDisplay.SelectNormalArray = 'None'
solution_05pvtuDisplay.SelectTangentArray = 'None'
solution_05pvtuDisplay.Texture = None
solution_05pvtuDisplay.RepeatTextures = 1
solution_05pvtuDisplay.InterpolateTextures = 0
solution_05pvtuDisplay.SeamlessU = 0
solution_05pvtuDisplay.SeamlessV = 0
solution_05pvtuDisplay.UseMipmapTextures = 0
solution_05pvtuDisplay.ShowTexturesOnBackface = 1
solution_05pvtuDisplay.BaseColorTexture = None
solution_05pvtuDisplay.NormalTexture = None
solution_05pvtuDisplay.NormalScale = 1.0
solution_05pvtuDisplay.CoatNormalTexture = None
solution_05pvtuDisplay.CoatNormalScale = 1.0
solution_05pvtuDisplay.MaterialTexture = None
solution_05pvtuDisplay.OcclusionStrength = 1.0
solution_05pvtuDisplay.AnisotropyTexture = None
solution_05pvtuDisplay.EmissiveTexture = None
solution_05pvtuDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.FlipTextures = 0
solution_05pvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
solution_05pvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.BackfaceOpacity = 1.0
solution_05pvtuDisplay.Position = [0.0, 0.0, 0.0]
solution_05pvtuDisplay.Scale = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.Orientation = [0.0, 0.0, 0.0]
solution_05pvtuDisplay.Origin = [0.0, 0.0, 0.0]
solution_05pvtuDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
solution_05pvtuDisplay.Pickable = 1
solution_05pvtuDisplay.Triangulate = 0
solution_05pvtuDisplay.UseShaderReplacements = 0
solution_05pvtuDisplay.ShaderReplacements = ''
solution_05pvtuDisplay.NonlinearSubdivisionLevel = 1
solution_05pvtuDisplay.UseDataPartitions = 0
solution_05pvtuDisplay.OSPRayUseScaleArray = 'All Approximate'
solution_05pvtuDisplay.OSPRayScaleArray = 'du_11'
solution_05pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution_05pvtuDisplay.OSPRayMaterial = 'None'
solution_05pvtuDisplay.BlockSelectors = ['/']
solution_05pvtuDisplay.BlockColors = []
solution_05pvtuDisplay.BlockOpacities = []
solution_05pvtuDisplay.Orient = 0
solution_05pvtuDisplay.OrientationMode = 'Direction'
solution_05pvtuDisplay.SelectOrientationVectors = 'None'
solution_05pvtuDisplay.Scaling = 0
solution_05pvtuDisplay.ScaleMode = 'No Data Scaling Off'
solution_05pvtuDisplay.ScaleFactor = 4.0
solution_05pvtuDisplay.SelectScaleArray = 'None'
solution_05pvtuDisplay.GlyphType = 'Arrow'
solution_05pvtuDisplay.UseGlyphTable = 0
solution_05pvtuDisplay.GlyphTableIndexArray = 'None'
solution_05pvtuDisplay.UseCompositeGlyphTable = 0
solution_05pvtuDisplay.UseGlyphCullingAndLOD = 0
solution_05pvtuDisplay.LODValues = []
solution_05pvtuDisplay.ColorByLODIndex = 0
solution_05pvtuDisplay.GaussianRadius = 0.2
solution_05pvtuDisplay.ShaderPreset = 'Sphere'
solution_05pvtuDisplay.CustomTriangleScale = 3
solution_05pvtuDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
solution_05pvtuDisplay.Emissive = 0
solution_05pvtuDisplay.ScaleByArray = 0
solution_05pvtuDisplay.SetScaleArray = ['POINTS', 'du_11']
solution_05pvtuDisplay.ScaleArrayComponent = ''
solution_05pvtuDisplay.UseScaleFunction = 1
solution_05pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution_05pvtuDisplay.OpacityByArray = 0
solution_05pvtuDisplay.OpacityArray = ['POINTS', 'du_11']
solution_05pvtuDisplay.OpacityArrayComponent = ''
solution_05pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution_05pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution_05pvtuDisplay.SelectionCellLabelBold = 0
solution_05pvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
solution_05pvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
solution_05pvtuDisplay.SelectionCellLabelFontFile = ''
solution_05pvtuDisplay.SelectionCellLabelFontSize = 18
solution_05pvtuDisplay.SelectionCellLabelItalic = 0
solution_05pvtuDisplay.SelectionCellLabelJustification = 'Left'
solution_05pvtuDisplay.SelectionCellLabelOpacity = 1.0
solution_05pvtuDisplay.SelectionCellLabelShadow = 0
solution_05pvtuDisplay.SelectionPointLabelBold = 0
solution_05pvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
solution_05pvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
solution_05pvtuDisplay.SelectionPointLabelFontFile = ''
solution_05pvtuDisplay.SelectionPointLabelFontSize = 18
solution_05pvtuDisplay.SelectionPointLabelItalic = 0
solution_05pvtuDisplay.SelectionPointLabelJustification = 'Left'
solution_05pvtuDisplay.SelectionPointLabelOpacity = 1.0
solution_05pvtuDisplay.SelectionPointLabelShadow = 0
solution_05pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
solution_05pvtuDisplay.ScalarOpacityFunction = None
solution_05pvtuDisplay.ScalarOpacityUnitDistance = 4.330127018922194
solution_05pvtuDisplay.UseSeparateOpacityArray = 0
solution_05pvtuDisplay.OpacityArrayName = ['POINTS', 'du_11']
solution_05pvtuDisplay.OpacityComponent = ''
solution_05pvtuDisplay.SelectMapper = 'Projected tetra'
solution_05pvtuDisplay.SamplingDimensions = [128, 128, 128]
solution_05pvtuDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
solution_05pvtuDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
solution_05pvtuDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
solution_05pvtuDisplay.GlyphType.TipResolution = 6
solution_05pvtuDisplay.GlyphType.TipRadius = 0.1
solution_05pvtuDisplay.GlyphType.TipLength = 0.35
solution_05pvtuDisplay.GlyphType.ShaftResolution = 6
solution_05pvtuDisplay.GlyphType.ShaftRadius = 0.03
solution_05pvtuDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution_05pvtuDisplay.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
solution_05pvtuDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution_05pvtuDisplay.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
solution_05pvtuDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
solution_05pvtuDisplay.DataAxesGrid.XTitle = 'X Axis'
solution_05pvtuDisplay.DataAxesGrid.YTitle = 'Y Axis'
solution_05pvtuDisplay.DataAxesGrid.ZTitle = 'Z Axis'
solution_05pvtuDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
solution_05pvtuDisplay.DataAxesGrid.XTitleFontFile = ''
solution_05pvtuDisplay.DataAxesGrid.XTitleBold = 0
solution_05pvtuDisplay.DataAxesGrid.XTitleItalic = 0
solution_05pvtuDisplay.DataAxesGrid.XTitleFontSize = 12
solution_05pvtuDisplay.DataAxesGrid.XTitleShadow = 0
solution_05pvtuDisplay.DataAxesGrid.XTitleOpacity = 1.0
solution_05pvtuDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
solution_05pvtuDisplay.DataAxesGrid.YTitleFontFile = ''
solution_05pvtuDisplay.DataAxesGrid.YTitleBold = 0
solution_05pvtuDisplay.DataAxesGrid.YTitleItalic = 0
solution_05pvtuDisplay.DataAxesGrid.YTitleFontSize = 12
solution_05pvtuDisplay.DataAxesGrid.YTitleShadow = 0
solution_05pvtuDisplay.DataAxesGrid.YTitleOpacity = 1.0
solution_05pvtuDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
solution_05pvtuDisplay.DataAxesGrid.ZTitleFontFile = ''
solution_05pvtuDisplay.DataAxesGrid.ZTitleBold = 0
solution_05pvtuDisplay.DataAxesGrid.ZTitleItalic = 0
solution_05pvtuDisplay.DataAxesGrid.ZTitleFontSize = 12
solution_05pvtuDisplay.DataAxesGrid.ZTitleShadow = 0
solution_05pvtuDisplay.DataAxesGrid.ZTitleOpacity = 1.0
solution_05pvtuDisplay.DataAxesGrid.FacesToRender = 63
solution_05pvtuDisplay.DataAxesGrid.CullBackface = 0
solution_05pvtuDisplay.DataAxesGrid.CullFrontface = 1
solution_05pvtuDisplay.DataAxesGrid.ShowGrid = 0
solution_05pvtuDisplay.DataAxesGrid.ShowEdges = 1
solution_05pvtuDisplay.DataAxesGrid.ShowTicks = 1
solution_05pvtuDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
solution_05pvtuDisplay.DataAxesGrid.AxesToLabel = 63
solution_05pvtuDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
solution_05pvtuDisplay.DataAxesGrid.XLabelFontFile = ''
solution_05pvtuDisplay.DataAxesGrid.XLabelBold = 0
solution_05pvtuDisplay.DataAxesGrid.XLabelItalic = 0
solution_05pvtuDisplay.DataAxesGrid.XLabelFontSize = 12
solution_05pvtuDisplay.DataAxesGrid.XLabelShadow = 0
solution_05pvtuDisplay.DataAxesGrid.XLabelOpacity = 1.0
solution_05pvtuDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
solution_05pvtuDisplay.DataAxesGrid.YLabelFontFile = ''
solution_05pvtuDisplay.DataAxesGrid.YLabelBold = 0
solution_05pvtuDisplay.DataAxesGrid.YLabelItalic = 0
solution_05pvtuDisplay.DataAxesGrid.YLabelFontSize = 12
solution_05pvtuDisplay.DataAxesGrid.YLabelShadow = 0
solution_05pvtuDisplay.DataAxesGrid.YLabelOpacity = 1.0
solution_05pvtuDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
solution_05pvtuDisplay.DataAxesGrid.ZLabelFontFile = ''
solution_05pvtuDisplay.DataAxesGrid.ZLabelBold = 0
solution_05pvtuDisplay.DataAxesGrid.ZLabelItalic = 0
solution_05pvtuDisplay.DataAxesGrid.ZLabelFontSize = 12
solution_05pvtuDisplay.DataAxesGrid.ZLabelShadow = 0
solution_05pvtuDisplay.DataAxesGrid.ZLabelOpacity = 1.0
solution_05pvtuDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
solution_05pvtuDisplay.DataAxesGrid.XAxisPrecision = 2
solution_05pvtuDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
solution_05pvtuDisplay.DataAxesGrid.XAxisLabels = []
solution_05pvtuDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
solution_05pvtuDisplay.DataAxesGrid.YAxisPrecision = 2
solution_05pvtuDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
solution_05pvtuDisplay.DataAxesGrid.YAxisLabels = []
solution_05pvtuDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
solution_05pvtuDisplay.DataAxesGrid.ZAxisPrecision = 2
solution_05pvtuDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
solution_05pvtuDisplay.DataAxesGrid.ZAxisLabels = []
solution_05pvtuDisplay.DataAxesGrid.UseCustomBounds = 0
solution_05pvtuDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
solution_05pvtuDisplay.PolarAxes.Visibility = 0
solution_05pvtuDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
solution_05pvtuDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
solution_05pvtuDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
solution_05pvtuDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
solution_05pvtuDisplay.PolarAxes.EnableCustomRange = 0
solution_05pvtuDisplay.PolarAxes.CustomRange = [0.0, 1.0]
solution_05pvtuDisplay.PolarAxes.PolarAxisVisibility = 1
solution_05pvtuDisplay.PolarAxes.RadialAxesVisibility = 1
solution_05pvtuDisplay.PolarAxes.DrawRadialGridlines = 1
solution_05pvtuDisplay.PolarAxes.PolarArcsVisibility = 1
solution_05pvtuDisplay.PolarAxes.DrawPolarArcsGridlines = 1
solution_05pvtuDisplay.PolarAxes.NumberOfRadialAxes = 0
solution_05pvtuDisplay.PolarAxes.AutoSubdividePolarAxis = 1
solution_05pvtuDisplay.PolarAxes.NumberOfPolarAxis = 0
solution_05pvtuDisplay.PolarAxes.MinimumRadius = 0.0
solution_05pvtuDisplay.PolarAxes.MinimumAngle = 0.0
solution_05pvtuDisplay.PolarAxes.MaximumAngle = 90.0
solution_05pvtuDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
solution_05pvtuDisplay.PolarAxes.Ratio = 1.0
solution_05pvtuDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleVisibility = 1
solution_05pvtuDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
solution_05pvtuDisplay.PolarAxes.PolarLabelVisibility = 1
solution_05pvtuDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
solution_05pvtuDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
solution_05pvtuDisplay.PolarAxes.RadialLabelVisibility = 1
solution_05pvtuDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
solution_05pvtuDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
solution_05pvtuDisplay.PolarAxes.RadialUnitsVisibility = 1
solution_05pvtuDisplay.PolarAxes.ScreenSize = 10.0
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleBold = 0
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleItalic = 0
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleShadow = 0
solution_05pvtuDisplay.PolarAxes.PolarAxisTitleFontSize = 12
solution_05pvtuDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
solution_05pvtuDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
solution_05pvtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
solution_05pvtuDisplay.PolarAxes.PolarAxisLabelBold = 0
solution_05pvtuDisplay.PolarAxes.PolarAxisLabelItalic = 0
solution_05pvtuDisplay.PolarAxes.PolarAxisLabelShadow = 0
solution_05pvtuDisplay.PolarAxes.PolarAxisLabelFontSize = 12
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTextBold = 0
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTextItalic = 0
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTextShadow = 0
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
solution_05pvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
solution_05pvtuDisplay.PolarAxes.EnableDistanceLOD = 1
solution_05pvtuDisplay.PolarAxes.DistanceLODThreshold = 0.7
solution_05pvtuDisplay.PolarAxes.EnableViewAngleLOD = 1
solution_05pvtuDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
solution_05pvtuDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
solution_05pvtuDisplay.PolarAxes.PolarTicksVisibility = 1
solution_05pvtuDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
solution_05pvtuDisplay.PolarAxes.TickLocation = 'Both'
solution_05pvtuDisplay.PolarAxes.AxisTickVisibility = 1
solution_05pvtuDisplay.PolarAxes.AxisMinorTickVisibility = 0
solution_05pvtuDisplay.PolarAxes.ArcTickVisibility = 1
solution_05pvtuDisplay.PolarAxes.ArcMinorTickVisibility = 0
solution_05pvtuDisplay.PolarAxes.DeltaAngleMajor = 10.0
solution_05pvtuDisplay.PolarAxes.DeltaAngleMinor = 5.0
solution_05pvtuDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
solution_05pvtuDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
solution_05pvtuDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
solution_05pvtuDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
solution_05pvtuDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
solution_05pvtuDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
solution_05pvtuDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
solution_05pvtuDisplay.PolarAxes.ArcMajorTickSize = 0.0
solution_05pvtuDisplay.PolarAxes.ArcTickRatioSize = 0.3
solution_05pvtuDisplay.PolarAxes.ArcMajorTickThickness = 1.0
solution_05pvtuDisplay.PolarAxes.ArcTickRatioThickness = 0.5
solution_05pvtuDisplay.PolarAxes.Use2DMode = 0
solution_05pvtuDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=solution_05pvtu)
mergeVectorComponents1.AttributeType = 'Point Data'
mergeVectorComponents1.XArray = 'du_11'
mergeVectorComponents1.YArray = 'du_11'
mergeVectorComponents1.ZArray = 'du_11'
mergeVectorComponents1.OutputVectorName = 'Vector'

# Properties modified on mergeVectorComponents1
mergeVectorComponents1.XArray = 'u_11'
mergeVectorComponents1.YArray = 'u_12'
mergeVectorComponents1.ZArray = 'u_13'
mergeVectorComponents1.OutputVectorName = 'm'

# show data in view
mergeVectorComponents1Display = Show(mergeVectorComponents1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents1Display.Selection = None
mergeVectorComponents1Display.Representation = 'Surface'
mergeVectorComponents1Display.ColorArrayName = [None, '']
mergeVectorComponents1Display.LookupTable = None
mergeVectorComponents1Display.MapScalars = 1
mergeVectorComponents1Display.MultiComponentsMapping = 0
mergeVectorComponents1Display.InterpolateScalarsBeforeMapping = 1
mergeVectorComponents1Display.Opacity = 1.0
mergeVectorComponents1Display.PointSize = 2.0
mergeVectorComponents1Display.LineWidth = 1.0
mergeVectorComponents1Display.RenderLinesAsTubes = 0
mergeVectorComponents1Display.RenderPointsAsSpheres = 0
mergeVectorComponents1Display.Interpolation = 'Gouraud'
mergeVectorComponents1Display.Specular = 0.0
mergeVectorComponents1Display.SpecularColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.SpecularPower = 100.0
mergeVectorComponents1Display.Luminosity = 0.0
mergeVectorComponents1Display.Ambient = 0.0
mergeVectorComponents1Display.Diffuse = 1.0
mergeVectorComponents1Display.Roughness = 0.3
mergeVectorComponents1Display.Metallic = 0.0
mergeVectorComponents1Display.EdgeTint = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.Anisotropy = 0.0
mergeVectorComponents1Display.AnisotropyRotation = 0.0
mergeVectorComponents1Display.BaseIOR = 1.5
mergeVectorComponents1Display.CoatStrength = 0.0
mergeVectorComponents1Display.CoatIOR = 2.0
mergeVectorComponents1Display.CoatRoughness = 0.0
mergeVectorComponents1Display.CoatColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.SelectTCoordArray = 'None'
mergeVectorComponents1Display.SelectNormalArray = 'None'
mergeVectorComponents1Display.SelectTangentArray = 'None'
mergeVectorComponents1Display.Texture = None
mergeVectorComponents1Display.RepeatTextures = 1
mergeVectorComponents1Display.InterpolateTextures = 0
mergeVectorComponents1Display.SeamlessU = 0
mergeVectorComponents1Display.SeamlessV = 0
mergeVectorComponents1Display.UseMipmapTextures = 0
mergeVectorComponents1Display.ShowTexturesOnBackface = 1
mergeVectorComponents1Display.BaseColorTexture = None
mergeVectorComponents1Display.NormalTexture = None
mergeVectorComponents1Display.NormalScale = 1.0
mergeVectorComponents1Display.CoatNormalTexture = None
mergeVectorComponents1Display.CoatNormalScale = 1.0
mergeVectorComponents1Display.MaterialTexture = None
mergeVectorComponents1Display.OcclusionStrength = 1.0
mergeVectorComponents1Display.AnisotropyTexture = None
mergeVectorComponents1Display.EmissiveTexture = None
mergeVectorComponents1Display.EmissiveFactor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.FlipTextures = 0
mergeVectorComponents1Display.BackfaceRepresentation = 'Follow Frontface'
mergeVectorComponents1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.BackfaceOpacity = 1.0
mergeVectorComponents1Display.Position = [0.0, 0.0, 0.0]
mergeVectorComponents1Display.Scale = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.Orientation = [0.0, 0.0, 0.0]
mergeVectorComponents1Display.Origin = [0.0, 0.0, 0.0]
mergeVectorComponents1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
mergeVectorComponents1Display.Pickable = 1
mergeVectorComponents1Display.Triangulate = 0
mergeVectorComponents1Display.UseShaderReplacements = 0
mergeVectorComponents1Display.ShaderReplacements = ''
mergeVectorComponents1Display.NonlinearSubdivisionLevel = 1
mergeVectorComponents1Display.UseDataPartitions = 0
mergeVectorComponents1Display.OSPRayUseScaleArray = 'All Approximate'
mergeVectorComponents1Display.OSPRayScaleArray = 'du_11'
mergeVectorComponents1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.OSPRayMaterial = 'None'
mergeVectorComponents1Display.BlockSelectors = ['/']
mergeVectorComponents1Display.BlockColors = []
mergeVectorComponents1Display.BlockOpacities = []
mergeVectorComponents1Display.Orient = 0
mergeVectorComponents1Display.OrientationMode = 'Direction'
mergeVectorComponents1Display.SelectOrientationVectors = 'None'
mergeVectorComponents1Display.Scaling = 0
mergeVectorComponents1Display.ScaleMode = 'No Data Scaling Off'
mergeVectorComponents1Display.ScaleFactor = 4.0
mergeVectorComponents1Display.SelectScaleArray = 'None'
mergeVectorComponents1Display.GlyphType = 'Arrow'
mergeVectorComponents1Display.UseGlyphTable = 0
mergeVectorComponents1Display.GlyphTableIndexArray = 'None'
mergeVectorComponents1Display.UseCompositeGlyphTable = 0
mergeVectorComponents1Display.UseGlyphCullingAndLOD = 0
mergeVectorComponents1Display.LODValues = []
mergeVectorComponents1Display.ColorByLODIndex = 0
mergeVectorComponents1Display.GaussianRadius = 0.2
mergeVectorComponents1Display.ShaderPreset = 'Sphere'
mergeVectorComponents1Display.CustomTriangleScale = 3
mergeVectorComponents1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
mergeVectorComponents1Display.Emissive = 0
mergeVectorComponents1Display.ScaleByArray = 0
mergeVectorComponents1Display.SetScaleArray = ['POINTS', 'du_11']
mergeVectorComponents1Display.ScaleArrayComponent = ''
mergeVectorComponents1Display.UseScaleFunction = 1
mergeVectorComponents1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.OpacityByArray = 0
mergeVectorComponents1Display.OpacityArray = ['POINTS', 'du_11']
mergeVectorComponents1Display.OpacityArrayComponent = ''
mergeVectorComponents1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents1Display.SelectionCellLabelBold = 0
mergeVectorComponents1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
mergeVectorComponents1Display.SelectionCellLabelFontFamily = 'Arial'
mergeVectorComponents1Display.SelectionCellLabelFontFile = ''
mergeVectorComponents1Display.SelectionCellLabelFontSize = 18
mergeVectorComponents1Display.SelectionCellLabelItalic = 0
mergeVectorComponents1Display.SelectionCellLabelJustification = 'Left'
mergeVectorComponents1Display.SelectionCellLabelOpacity = 1.0
mergeVectorComponents1Display.SelectionCellLabelShadow = 0
mergeVectorComponents1Display.SelectionPointLabelBold = 0
mergeVectorComponents1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
mergeVectorComponents1Display.SelectionPointLabelFontFamily = 'Arial'
mergeVectorComponents1Display.SelectionPointLabelFontFile = ''
mergeVectorComponents1Display.SelectionPointLabelFontSize = 18
mergeVectorComponents1Display.SelectionPointLabelItalic = 0
mergeVectorComponents1Display.SelectionPointLabelJustification = 'Left'
mergeVectorComponents1Display.SelectionPointLabelOpacity = 1.0
mergeVectorComponents1Display.SelectionPointLabelShadow = 0
mergeVectorComponents1Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents1Display.ScalarOpacityFunction = None
mergeVectorComponents1Display.ScalarOpacityUnitDistance = 4.330127018922194
mergeVectorComponents1Display.UseSeparateOpacityArray = 0
mergeVectorComponents1Display.OpacityArrayName = ['POINTS', 'du_11']
mergeVectorComponents1Display.OpacityComponent = ''
mergeVectorComponents1Display.SelectMapper = 'Projected tetra'
mergeVectorComponents1Display.SamplingDimensions = [128, 128, 128]
mergeVectorComponents1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
mergeVectorComponents1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
mergeVectorComponents1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
mergeVectorComponents1Display.GlyphType.TipResolution = 6
mergeVectorComponents1Display.GlyphType.TipRadius = 0.1
mergeVectorComponents1Display.GlyphType.TipLength = 0.35
mergeVectorComponents1Display.GlyphType.ShaftResolution = 6
mergeVectorComponents1Display.GlyphType.ShaftRadius = 0.03
mergeVectorComponents1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents1Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
mergeVectorComponents1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents1Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
mergeVectorComponents1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mergeVectorComponents1Display.DataAxesGrid.XTitle = 'X Axis'
mergeVectorComponents1Display.DataAxesGrid.YTitle = 'Y Axis'
mergeVectorComponents1Display.DataAxesGrid.ZTitle = 'Z Axis'
mergeVectorComponents1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
mergeVectorComponents1Display.DataAxesGrid.XTitleFontFile = ''
mergeVectorComponents1Display.DataAxesGrid.XTitleBold = 0
mergeVectorComponents1Display.DataAxesGrid.XTitleItalic = 0
mergeVectorComponents1Display.DataAxesGrid.XTitleFontSize = 12
mergeVectorComponents1Display.DataAxesGrid.XTitleShadow = 0
mergeVectorComponents1Display.DataAxesGrid.XTitleOpacity = 1.0
mergeVectorComponents1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
mergeVectorComponents1Display.DataAxesGrid.YTitleFontFile = ''
mergeVectorComponents1Display.DataAxesGrid.YTitleBold = 0
mergeVectorComponents1Display.DataAxesGrid.YTitleItalic = 0
mergeVectorComponents1Display.DataAxesGrid.YTitleFontSize = 12
mergeVectorComponents1Display.DataAxesGrid.YTitleShadow = 0
mergeVectorComponents1Display.DataAxesGrid.YTitleOpacity = 1.0
mergeVectorComponents1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
mergeVectorComponents1Display.DataAxesGrid.ZTitleFontFile = ''
mergeVectorComponents1Display.DataAxesGrid.ZTitleBold = 0
mergeVectorComponents1Display.DataAxesGrid.ZTitleItalic = 0
mergeVectorComponents1Display.DataAxesGrid.ZTitleFontSize = 12
mergeVectorComponents1Display.DataAxesGrid.ZTitleShadow = 0
mergeVectorComponents1Display.DataAxesGrid.ZTitleOpacity = 1.0
mergeVectorComponents1Display.DataAxesGrid.FacesToRender = 63
mergeVectorComponents1Display.DataAxesGrid.CullBackface = 0
mergeVectorComponents1Display.DataAxesGrid.CullFrontface = 1
mergeVectorComponents1Display.DataAxesGrid.ShowGrid = 0
mergeVectorComponents1Display.DataAxesGrid.ShowEdges = 1
mergeVectorComponents1Display.DataAxesGrid.ShowTicks = 1
mergeVectorComponents1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
mergeVectorComponents1Display.DataAxesGrid.AxesToLabel = 63
mergeVectorComponents1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
mergeVectorComponents1Display.DataAxesGrid.XLabelFontFile = ''
mergeVectorComponents1Display.DataAxesGrid.XLabelBold = 0
mergeVectorComponents1Display.DataAxesGrid.XLabelItalic = 0
mergeVectorComponents1Display.DataAxesGrid.XLabelFontSize = 12
mergeVectorComponents1Display.DataAxesGrid.XLabelShadow = 0
mergeVectorComponents1Display.DataAxesGrid.XLabelOpacity = 1.0
mergeVectorComponents1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
mergeVectorComponents1Display.DataAxesGrid.YLabelFontFile = ''
mergeVectorComponents1Display.DataAxesGrid.YLabelBold = 0
mergeVectorComponents1Display.DataAxesGrid.YLabelItalic = 0
mergeVectorComponents1Display.DataAxesGrid.YLabelFontSize = 12
mergeVectorComponents1Display.DataAxesGrid.YLabelShadow = 0
mergeVectorComponents1Display.DataAxesGrid.YLabelOpacity = 1.0
mergeVectorComponents1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
mergeVectorComponents1Display.DataAxesGrid.ZLabelFontFile = ''
mergeVectorComponents1Display.DataAxesGrid.ZLabelBold = 0
mergeVectorComponents1Display.DataAxesGrid.ZLabelItalic = 0
mergeVectorComponents1Display.DataAxesGrid.ZLabelFontSize = 12
mergeVectorComponents1Display.DataAxesGrid.ZLabelShadow = 0
mergeVectorComponents1Display.DataAxesGrid.ZLabelOpacity = 1.0
mergeVectorComponents1Display.DataAxesGrid.XAxisNotation = 'Mixed'
mergeVectorComponents1Display.DataAxesGrid.XAxisPrecision = 2
mergeVectorComponents1Display.DataAxesGrid.XAxisUseCustomLabels = 0
mergeVectorComponents1Display.DataAxesGrid.XAxisLabels = []
mergeVectorComponents1Display.DataAxesGrid.YAxisNotation = 'Mixed'
mergeVectorComponents1Display.DataAxesGrid.YAxisPrecision = 2
mergeVectorComponents1Display.DataAxesGrid.YAxisUseCustomLabels = 0
mergeVectorComponents1Display.DataAxesGrid.YAxisLabels = []
mergeVectorComponents1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
mergeVectorComponents1Display.DataAxesGrid.ZAxisPrecision = 2
mergeVectorComponents1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
mergeVectorComponents1Display.DataAxesGrid.ZAxisLabels = []
mergeVectorComponents1Display.DataAxesGrid.UseCustomBounds = 0
mergeVectorComponents1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
mergeVectorComponents1Display.PolarAxes.Visibility = 0
mergeVectorComponents1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
mergeVectorComponents1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
mergeVectorComponents1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
mergeVectorComponents1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
mergeVectorComponents1Display.PolarAxes.EnableCustomRange = 0
mergeVectorComponents1Display.PolarAxes.CustomRange = [0.0, 1.0]
mergeVectorComponents1Display.PolarAxes.PolarAxisVisibility = 1
mergeVectorComponents1Display.PolarAxes.RadialAxesVisibility = 1
mergeVectorComponents1Display.PolarAxes.DrawRadialGridlines = 1
mergeVectorComponents1Display.PolarAxes.PolarArcsVisibility = 1
mergeVectorComponents1Display.PolarAxes.DrawPolarArcsGridlines = 1
mergeVectorComponents1Display.PolarAxes.NumberOfRadialAxes = 0
mergeVectorComponents1Display.PolarAxes.AutoSubdividePolarAxis = 1
mergeVectorComponents1Display.PolarAxes.NumberOfPolarAxis = 0
mergeVectorComponents1Display.PolarAxes.MinimumRadius = 0.0
mergeVectorComponents1Display.PolarAxes.MinimumAngle = 0.0
mergeVectorComponents1Display.PolarAxes.MaximumAngle = 90.0
mergeVectorComponents1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
mergeVectorComponents1Display.PolarAxes.Ratio = 1.0
mergeVectorComponents1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleVisibility = 1
mergeVectorComponents1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
mergeVectorComponents1Display.PolarAxes.PolarLabelVisibility = 1
mergeVectorComponents1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
mergeVectorComponents1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
mergeVectorComponents1Display.PolarAxes.RadialLabelVisibility = 1
mergeVectorComponents1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
mergeVectorComponents1Display.PolarAxes.RadialLabelLocation = 'Bottom'
mergeVectorComponents1Display.PolarAxes.RadialUnitsVisibility = 1
mergeVectorComponents1Display.PolarAxes.ScreenSize = 10.0
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleFontFile = ''
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleBold = 0
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleItalic = 0
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleShadow = 0
mergeVectorComponents1Display.PolarAxes.PolarAxisTitleFontSize = 12
mergeVectorComponents1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
mergeVectorComponents1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
mergeVectorComponents1Display.PolarAxes.PolarAxisLabelFontFile = ''
mergeVectorComponents1Display.PolarAxes.PolarAxisLabelBold = 0
mergeVectorComponents1Display.PolarAxes.PolarAxisLabelItalic = 0
mergeVectorComponents1Display.PolarAxes.PolarAxisLabelShadow = 0
mergeVectorComponents1Display.PolarAxes.PolarAxisLabelFontSize = 12
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTextFontFile = ''
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTextBold = 0
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTextItalic = 0
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTextShadow = 0
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTextFontSize = 12
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
mergeVectorComponents1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
mergeVectorComponents1Display.PolarAxes.EnableDistanceLOD = 1
mergeVectorComponents1Display.PolarAxes.DistanceLODThreshold = 0.7
mergeVectorComponents1Display.PolarAxes.EnableViewAngleLOD = 1
mergeVectorComponents1Display.PolarAxes.ViewAngleLODThreshold = 0.7
mergeVectorComponents1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
mergeVectorComponents1Display.PolarAxes.PolarTicksVisibility = 1
mergeVectorComponents1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
mergeVectorComponents1Display.PolarAxes.TickLocation = 'Both'
mergeVectorComponents1Display.PolarAxes.AxisTickVisibility = 1
mergeVectorComponents1Display.PolarAxes.AxisMinorTickVisibility = 0
mergeVectorComponents1Display.PolarAxes.ArcTickVisibility = 1
mergeVectorComponents1Display.PolarAxes.ArcMinorTickVisibility = 0
mergeVectorComponents1Display.PolarAxes.DeltaAngleMajor = 10.0
mergeVectorComponents1Display.PolarAxes.DeltaAngleMinor = 5.0
mergeVectorComponents1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
mergeVectorComponents1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
mergeVectorComponents1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
mergeVectorComponents1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
mergeVectorComponents1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
mergeVectorComponents1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
mergeVectorComponents1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
mergeVectorComponents1Display.PolarAxes.ArcMajorTickSize = 0.0
mergeVectorComponents1Display.PolarAxes.ArcTickRatioSize = 0.3
mergeVectorComponents1Display.PolarAxes.ArcMajorTickThickness = 1.0
mergeVectorComponents1Display.PolarAxes.ArcTickRatioThickness = 0.5
mergeVectorComponents1Display.PolarAxes.Use2DMode = 0
mergeVectorComponents1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(solution_05pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(solution_05pvtu)

# create a new 'Merge Vector Components'
mergeVectorComponents2 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=solution_05pvtu)
mergeVectorComponents2.AttributeType = 'Point Data'
mergeVectorComponents2.XArray = 'du_11'
mergeVectorComponents2.YArray = 'du_11'
mergeVectorComponents2.ZArray = 'du_11'
mergeVectorComponents2.OutputVectorName = 'Vector'

# Properties modified on mergeVectorComponents2
mergeVectorComponents2.XArray = 'v_11'
mergeVectorComponents2.YArray = 'v_12'
mergeVectorComponents2.ZArray = 'v_13'
mergeVectorComponents2.OutputVectorName = 'n'

# show data in view
mergeVectorComponents2Display = Show(mergeVectorComponents2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents2Display.Selection = None
mergeVectorComponents2Display.Representation = 'Surface'
mergeVectorComponents2Display.ColorArrayName = [None, '']
mergeVectorComponents2Display.LookupTable = None
mergeVectorComponents2Display.MapScalars = 1
mergeVectorComponents2Display.MultiComponentsMapping = 0
mergeVectorComponents2Display.InterpolateScalarsBeforeMapping = 1
mergeVectorComponents2Display.Opacity = 1.0
mergeVectorComponents2Display.PointSize = 2.0
mergeVectorComponents2Display.LineWidth = 1.0
mergeVectorComponents2Display.RenderLinesAsTubes = 0
mergeVectorComponents2Display.RenderPointsAsSpheres = 0
mergeVectorComponents2Display.Interpolation = 'Gouraud'
mergeVectorComponents2Display.Specular = 0.0
mergeVectorComponents2Display.SpecularColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.SpecularPower = 100.0
mergeVectorComponents2Display.Luminosity = 0.0
mergeVectorComponents2Display.Ambient = 0.0
mergeVectorComponents2Display.Diffuse = 1.0
mergeVectorComponents2Display.Roughness = 0.3
mergeVectorComponents2Display.Metallic = 0.0
mergeVectorComponents2Display.EdgeTint = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.Anisotropy = 0.0
mergeVectorComponents2Display.AnisotropyRotation = 0.0
mergeVectorComponents2Display.BaseIOR = 1.5
mergeVectorComponents2Display.CoatStrength = 0.0
mergeVectorComponents2Display.CoatIOR = 2.0
mergeVectorComponents2Display.CoatRoughness = 0.0
mergeVectorComponents2Display.CoatColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.SelectTCoordArray = 'None'
mergeVectorComponents2Display.SelectNormalArray = 'None'
mergeVectorComponents2Display.SelectTangentArray = 'None'
mergeVectorComponents2Display.Texture = None
mergeVectorComponents2Display.RepeatTextures = 1
mergeVectorComponents2Display.InterpolateTextures = 0
mergeVectorComponents2Display.SeamlessU = 0
mergeVectorComponents2Display.SeamlessV = 0
mergeVectorComponents2Display.UseMipmapTextures = 0
mergeVectorComponents2Display.ShowTexturesOnBackface = 1
mergeVectorComponents2Display.BaseColorTexture = None
mergeVectorComponents2Display.NormalTexture = None
mergeVectorComponents2Display.NormalScale = 1.0
mergeVectorComponents2Display.CoatNormalTexture = None
mergeVectorComponents2Display.CoatNormalScale = 1.0
mergeVectorComponents2Display.MaterialTexture = None
mergeVectorComponents2Display.OcclusionStrength = 1.0
mergeVectorComponents2Display.AnisotropyTexture = None
mergeVectorComponents2Display.EmissiveTexture = None
mergeVectorComponents2Display.EmissiveFactor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.FlipTextures = 0
mergeVectorComponents2Display.BackfaceRepresentation = 'Follow Frontface'
mergeVectorComponents2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.BackfaceOpacity = 1.0
mergeVectorComponents2Display.Position = [0.0, 0.0, 0.0]
mergeVectorComponents2Display.Scale = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.Orientation = [0.0, 0.0, 0.0]
mergeVectorComponents2Display.Origin = [0.0, 0.0, 0.0]
mergeVectorComponents2Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
mergeVectorComponents2Display.Pickable = 1
mergeVectorComponents2Display.Triangulate = 0
mergeVectorComponents2Display.UseShaderReplacements = 0
mergeVectorComponents2Display.ShaderReplacements = ''
mergeVectorComponents2Display.NonlinearSubdivisionLevel = 1
mergeVectorComponents2Display.UseDataPartitions = 0
mergeVectorComponents2Display.OSPRayUseScaleArray = 'All Approximate'
mergeVectorComponents2Display.OSPRayScaleArray = 'du_11'
mergeVectorComponents2Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.OSPRayMaterial = 'None'
mergeVectorComponents2Display.BlockSelectors = ['/']
mergeVectorComponents2Display.BlockColors = []
mergeVectorComponents2Display.BlockOpacities = []
mergeVectorComponents2Display.Orient = 0
mergeVectorComponents2Display.OrientationMode = 'Direction'
mergeVectorComponents2Display.SelectOrientationVectors = 'None'
mergeVectorComponents2Display.Scaling = 0
mergeVectorComponents2Display.ScaleMode = 'No Data Scaling Off'
mergeVectorComponents2Display.ScaleFactor = 4.0
mergeVectorComponents2Display.SelectScaleArray = 'None'
mergeVectorComponents2Display.GlyphType = 'Arrow'
mergeVectorComponents2Display.UseGlyphTable = 0
mergeVectorComponents2Display.GlyphTableIndexArray = 'None'
mergeVectorComponents2Display.UseCompositeGlyphTable = 0
mergeVectorComponents2Display.UseGlyphCullingAndLOD = 0
mergeVectorComponents2Display.LODValues = []
mergeVectorComponents2Display.ColorByLODIndex = 0
mergeVectorComponents2Display.GaussianRadius = 0.2
mergeVectorComponents2Display.ShaderPreset = 'Sphere'
mergeVectorComponents2Display.CustomTriangleScale = 3
mergeVectorComponents2Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
mergeVectorComponents2Display.Emissive = 0
mergeVectorComponents2Display.ScaleByArray = 0
mergeVectorComponents2Display.SetScaleArray = ['POINTS', 'du_11']
mergeVectorComponents2Display.ScaleArrayComponent = ''
mergeVectorComponents2Display.UseScaleFunction = 1
mergeVectorComponents2Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.OpacityByArray = 0
mergeVectorComponents2Display.OpacityArray = ['POINTS', 'du_11']
mergeVectorComponents2Display.OpacityArrayComponent = ''
mergeVectorComponents2Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents2Display.SelectionCellLabelBold = 0
mergeVectorComponents2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
mergeVectorComponents2Display.SelectionCellLabelFontFamily = 'Arial'
mergeVectorComponents2Display.SelectionCellLabelFontFile = ''
mergeVectorComponents2Display.SelectionCellLabelFontSize = 18
mergeVectorComponents2Display.SelectionCellLabelItalic = 0
mergeVectorComponents2Display.SelectionCellLabelJustification = 'Left'
mergeVectorComponents2Display.SelectionCellLabelOpacity = 1.0
mergeVectorComponents2Display.SelectionCellLabelShadow = 0
mergeVectorComponents2Display.SelectionPointLabelBold = 0
mergeVectorComponents2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
mergeVectorComponents2Display.SelectionPointLabelFontFamily = 'Arial'
mergeVectorComponents2Display.SelectionPointLabelFontFile = ''
mergeVectorComponents2Display.SelectionPointLabelFontSize = 18
mergeVectorComponents2Display.SelectionPointLabelItalic = 0
mergeVectorComponents2Display.SelectionPointLabelJustification = 'Left'
mergeVectorComponents2Display.SelectionPointLabelOpacity = 1.0
mergeVectorComponents2Display.SelectionPointLabelShadow = 0
mergeVectorComponents2Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents2Display.ScalarOpacityFunction = None
mergeVectorComponents2Display.ScalarOpacityUnitDistance = 4.330127018922194
mergeVectorComponents2Display.UseSeparateOpacityArray = 0
mergeVectorComponents2Display.OpacityArrayName = ['POINTS', 'du_11']
mergeVectorComponents2Display.OpacityComponent = ''
mergeVectorComponents2Display.SelectMapper = 'Projected tetra'
mergeVectorComponents2Display.SamplingDimensions = [128, 128, 128]
mergeVectorComponents2Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
mergeVectorComponents2Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
mergeVectorComponents2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
mergeVectorComponents2Display.GlyphType.TipResolution = 6
mergeVectorComponents2Display.GlyphType.TipRadius = 0.1
mergeVectorComponents2Display.GlyphType.TipLength = 0.35
mergeVectorComponents2Display.GlyphType.ShaftResolution = 6
mergeVectorComponents2Display.GlyphType.ShaftRadius = 0.03
mergeVectorComponents2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents2Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
mergeVectorComponents2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents2Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
mergeVectorComponents2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mergeVectorComponents2Display.DataAxesGrid.XTitle = 'X Axis'
mergeVectorComponents2Display.DataAxesGrid.YTitle = 'Y Axis'
mergeVectorComponents2Display.DataAxesGrid.ZTitle = 'Z Axis'
mergeVectorComponents2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
mergeVectorComponents2Display.DataAxesGrid.XTitleFontFile = ''
mergeVectorComponents2Display.DataAxesGrid.XTitleBold = 0
mergeVectorComponents2Display.DataAxesGrid.XTitleItalic = 0
mergeVectorComponents2Display.DataAxesGrid.XTitleFontSize = 12
mergeVectorComponents2Display.DataAxesGrid.XTitleShadow = 0
mergeVectorComponents2Display.DataAxesGrid.XTitleOpacity = 1.0
mergeVectorComponents2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
mergeVectorComponents2Display.DataAxesGrid.YTitleFontFile = ''
mergeVectorComponents2Display.DataAxesGrid.YTitleBold = 0
mergeVectorComponents2Display.DataAxesGrid.YTitleItalic = 0
mergeVectorComponents2Display.DataAxesGrid.YTitleFontSize = 12
mergeVectorComponents2Display.DataAxesGrid.YTitleShadow = 0
mergeVectorComponents2Display.DataAxesGrid.YTitleOpacity = 1.0
mergeVectorComponents2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
mergeVectorComponents2Display.DataAxesGrid.ZTitleFontFile = ''
mergeVectorComponents2Display.DataAxesGrid.ZTitleBold = 0
mergeVectorComponents2Display.DataAxesGrid.ZTitleItalic = 0
mergeVectorComponents2Display.DataAxesGrid.ZTitleFontSize = 12
mergeVectorComponents2Display.DataAxesGrid.ZTitleShadow = 0
mergeVectorComponents2Display.DataAxesGrid.ZTitleOpacity = 1.0
mergeVectorComponents2Display.DataAxesGrid.FacesToRender = 63
mergeVectorComponents2Display.DataAxesGrid.CullBackface = 0
mergeVectorComponents2Display.DataAxesGrid.CullFrontface = 1
mergeVectorComponents2Display.DataAxesGrid.ShowGrid = 0
mergeVectorComponents2Display.DataAxesGrid.ShowEdges = 1
mergeVectorComponents2Display.DataAxesGrid.ShowTicks = 1
mergeVectorComponents2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
mergeVectorComponents2Display.DataAxesGrid.AxesToLabel = 63
mergeVectorComponents2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
mergeVectorComponents2Display.DataAxesGrid.XLabelFontFile = ''
mergeVectorComponents2Display.DataAxesGrid.XLabelBold = 0
mergeVectorComponents2Display.DataAxesGrid.XLabelItalic = 0
mergeVectorComponents2Display.DataAxesGrid.XLabelFontSize = 12
mergeVectorComponents2Display.DataAxesGrid.XLabelShadow = 0
mergeVectorComponents2Display.DataAxesGrid.XLabelOpacity = 1.0
mergeVectorComponents2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
mergeVectorComponents2Display.DataAxesGrid.YLabelFontFile = ''
mergeVectorComponents2Display.DataAxesGrid.YLabelBold = 0
mergeVectorComponents2Display.DataAxesGrid.YLabelItalic = 0
mergeVectorComponents2Display.DataAxesGrid.YLabelFontSize = 12
mergeVectorComponents2Display.DataAxesGrid.YLabelShadow = 0
mergeVectorComponents2Display.DataAxesGrid.YLabelOpacity = 1.0
mergeVectorComponents2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
mergeVectorComponents2Display.DataAxesGrid.ZLabelFontFile = ''
mergeVectorComponents2Display.DataAxesGrid.ZLabelBold = 0
mergeVectorComponents2Display.DataAxesGrid.ZLabelItalic = 0
mergeVectorComponents2Display.DataAxesGrid.ZLabelFontSize = 12
mergeVectorComponents2Display.DataAxesGrid.ZLabelShadow = 0
mergeVectorComponents2Display.DataAxesGrid.ZLabelOpacity = 1.0
mergeVectorComponents2Display.DataAxesGrid.XAxisNotation = 'Mixed'
mergeVectorComponents2Display.DataAxesGrid.XAxisPrecision = 2
mergeVectorComponents2Display.DataAxesGrid.XAxisUseCustomLabels = 0
mergeVectorComponents2Display.DataAxesGrid.XAxisLabels = []
mergeVectorComponents2Display.DataAxesGrid.YAxisNotation = 'Mixed'
mergeVectorComponents2Display.DataAxesGrid.YAxisPrecision = 2
mergeVectorComponents2Display.DataAxesGrid.YAxisUseCustomLabels = 0
mergeVectorComponents2Display.DataAxesGrid.YAxisLabels = []
mergeVectorComponents2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
mergeVectorComponents2Display.DataAxesGrid.ZAxisPrecision = 2
mergeVectorComponents2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
mergeVectorComponents2Display.DataAxesGrid.ZAxisLabels = []
mergeVectorComponents2Display.DataAxesGrid.UseCustomBounds = 0
mergeVectorComponents2Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
mergeVectorComponents2Display.PolarAxes.Visibility = 0
mergeVectorComponents2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
mergeVectorComponents2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
mergeVectorComponents2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
mergeVectorComponents2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
mergeVectorComponents2Display.PolarAxes.EnableCustomRange = 0
mergeVectorComponents2Display.PolarAxes.CustomRange = [0.0, 1.0]
mergeVectorComponents2Display.PolarAxes.PolarAxisVisibility = 1
mergeVectorComponents2Display.PolarAxes.RadialAxesVisibility = 1
mergeVectorComponents2Display.PolarAxes.DrawRadialGridlines = 1
mergeVectorComponents2Display.PolarAxes.PolarArcsVisibility = 1
mergeVectorComponents2Display.PolarAxes.DrawPolarArcsGridlines = 1
mergeVectorComponents2Display.PolarAxes.NumberOfRadialAxes = 0
mergeVectorComponents2Display.PolarAxes.AutoSubdividePolarAxis = 1
mergeVectorComponents2Display.PolarAxes.NumberOfPolarAxis = 0
mergeVectorComponents2Display.PolarAxes.MinimumRadius = 0.0
mergeVectorComponents2Display.PolarAxes.MinimumAngle = 0.0
mergeVectorComponents2Display.PolarAxes.MaximumAngle = 90.0
mergeVectorComponents2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
mergeVectorComponents2Display.PolarAxes.Ratio = 1.0
mergeVectorComponents2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleVisibility = 1
mergeVectorComponents2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
mergeVectorComponents2Display.PolarAxes.PolarLabelVisibility = 1
mergeVectorComponents2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
mergeVectorComponents2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
mergeVectorComponents2Display.PolarAxes.RadialLabelVisibility = 1
mergeVectorComponents2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
mergeVectorComponents2Display.PolarAxes.RadialLabelLocation = 'Bottom'
mergeVectorComponents2Display.PolarAxes.RadialUnitsVisibility = 1
mergeVectorComponents2Display.PolarAxes.ScreenSize = 10.0
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleFontFile = ''
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleBold = 0
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleItalic = 0
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleShadow = 0
mergeVectorComponents2Display.PolarAxes.PolarAxisTitleFontSize = 12
mergeVectorComponents2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
mergeVectorComponents2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
mergeVectorComponents2Display.PolarAxes.PolarAxisLabelFontFile = ''
mergeVectorComponents2Display.PolarAxes.PolarAxisLabelBold = 0
mergeVectorComponents2Display.PolarAxes.PolarAxisLabelItalic = 0
mergeVectorComponents2Display.PolarAxes.PolarAxisLabelShadow = 0
mergeVectorComponents2Display.PolarAxes.PolarAxisLabelFontSize = 12
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTextFontFile = ''
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTextBold = 0
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTextItalic = 0
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTextShadow = 0
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTextFontSize = 12
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
mergeVectorComponents2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
mergeVectorComponents2Display.PolarAxes.EnableDistanceLOD = 1
mergeVectorComponents2Display.PolarAxes.DistanceLODThreshold = 0.7
mergeVectorComponents2Display.PolarAxes.EnableViewAngleLOD = 1
mergeVectorComponents2Display.PolarAxes.ViewAngleLODThreshold = 0.7
mergeVectorComponents2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
mergeVectorComponents2Display.PolarAxes.PolarTicksVisibility = 1
mergeVectorComponents2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
mergeVectorComponents2Display.PolarAxes.TickLocation = 'Both'
mergeVectorComponents2Display.PolarAxes.AxisTickVisibility = 1
mergeVectorComponents2Display.PolarAxes.AxisMinorTickVisibility = 0
mergeVectorComponents2Display.PolarAxes.ArcTickVisibility = 1
mergeVectorComponents2Display.PolarAxes.ArcMinorTickVisibility = 0
mergeVectorComponents2Display.PolarAxes.DeltaAngleMajor = 10.0
mergeVectorComponents2Display.PolarAxes.DeltaAngleMinor = 5.0
mergeVectorComponents2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
mergeVectorComponents2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
mergeVectorComponents2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
mergeVectorComponents2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
mergeVectorComponents2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
mergeVectorComponents2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
mergeVectorComponents2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
mergeVectorComponents2Display.PolarAxes.ArcMajorTickSize = 0.0
mergeVectorComponents2Display.PolarAxes.ArcTickRatioSize = 0.3
mergeVectorComponents2Display.PolarAxes.ArcMajorTickThickness = 1.0
mergeVectorComponents2Display.PolarAxes.ArcTickRatioThickness = 0.5
mergeVectorComponents2Display.PolarAxes.Use2DMode = 0
mergeVectorComponents2Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(solution_05pvtu, renderView1)

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
appendAttributes1Display.Selection = None
appendAttributes1Display.Representation = 'Surface'
appendAttributes1Display.ColorArrayName = [None, '']
appendAttributes1Display.LookupTable = None
appendAttributes1Display.MapScalars = 1
appendAttributes1Display.MultiComponentsMapping = 0
appendAttributes1Display.InterpolateScalarsBeforeMapping = 1
appendAttributes1Display.Opacity = 1.0
appendAttributes1Display.PointSize = 2.0
appendAttributes1Display.LineWidth = 1.0
appendAttributes1Display.RenderLinesAsTubes = 0
appendAttributes1Display.RenderPointsAsSpheres = 0
appendAttributes1Display.Interpolation = 'Gouraud'
appendAttributes1Display.Specular = 0.0
appendAttributes1Display.SpecularColor = [1.0, 1.0, 1.0]
appendAttributes1Display.SpecularPower = 100.0
appendAttributes1Display.Luminosity = 0.0
appendAttributes1Display.Ambient = 0.0
appendAttributes1Display.Diffuse = 1.0
appendAttributes1Display.Roughness = 0.3
appendAttributes1Display.Metallic = 0.0
appendAttributes1Display.EdgeTint = [1.0, 1.0, 1.0]
appendAttributes1Display.Anisotropy = 0.0
appendAttributes1Display.AnisotropyRotation = 0.0
appendAttributes1Display.BaseIOR = 1.5
appendAttributes1Display.CoatStrength = 0.0
appendAttributes1Display.CoatIOR = 2.0
appendAttributes1Display.CoatRoughness = 0.0
appendAttributes1Display.CoatColor = [1.0, 1.0, 1.0]
appendAttributes1Display.SelectTCoordArray = 'None'
appendAttributes1Display.SelectNormalArray = 'None'
appendAttributes1Display.SelectTangentArray = 'None'
appendAttributes1Display.Texture = None
appendAttributes1Display.RepeatTextures = 1
appendAttributes1Display.InterpolateTextures = 0
appendAttributes1Display.SeamlessU = 0
appendAttributes1Display.SeamlessV = 0
appendAttributes1Display.UseMipmapTextures = 0
appendAttributes1Display.ShowTexturesOnBackface = 1
appendAttributes1Display.BaseColorTexture = None
appendAttributes1Display.NormalTexture = None
appendAttributes1Display.NormalScale = 1.0
appendAttributes1Display.CoatNormalTexture = None
appendAttributes1Display.CoatNormalScale = 1.0
appendAttributes1Display.MaterialTexture = None
appendAttributes1Display.OcclusionStrength = 1.0
appendAttributes1Display.AnisotropyTexture = None
appendAttributes1Display.EmissiveTexture = None
appendAttributes1Display.EmissiveFactor = [1.0, 1.0, 1.0]
appendAttributes1Display.FlipTextures = 0
appendAttributes1Display.BackfaceRepresentation = 'Follow Frontface'
appendAttributes1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
appendAttributes1Display.BackfaceOpacity = 1.0
appendAttributes1Display.Position = [0.0, 0.0, 0.0]
appendAttributes1Display.Scale = [1.0, 1.0, 1.0]
appendAttributes1Display.Orientation = [0.0, 0.0, 0.0]
appendAttributes1Display.Origin = [0.0, 0.0, 0.0]
appendAttributes1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
appendAttributes1Display.Pickable = 1
appendAttributes1Display.Triangulate = 0
appendAttributes1Display.UseShaderReplacements = 0
appendAttributes1Display.ShaderReplacements = ''
appendAttributes1Display.NonlinearSubdivisionLevel = 1
appendAttributes1Display.UseDataPartitions = 0
appendAttributes1Display.OSPRayUseScaleArray = 'All Approximate'
appendAttributes1Display.OSPRayScaleArray = 'du_11'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.OSPRayMaterial = 'None'
appendAttributes1Display.BlockSelectors = ['/']
appendAttributes1Display.BlockColors = []
appendAttributes1Display.BlockOpacities = []
appendAttributes1Display.Orient = 0
appendAttributes1Display.OrientationMode = 'Direction'
appendAttributes1Display.SelectOrientationVectors = 'None'
appendAttributes1Display.Scaling = 0
appendAttributes1Display.ScaleMode = 'No Data Scaling Off'
appendAttributes1Display.ScaleFactor = 4.0
appendAttributes1Display.SelectScaleArray = 'None'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.UseGlyphTable = 0
appendAttributes1Display.GlyphTableIndexArray = 'None'
appendAttributes1Display.UseCompositeGlyphTable = 0
appendAttributes1Display.UseGlyphCullingAndLOD = 0
appendAttributes1Display.LODValues = []
appendAttributes1Display.ColorByLODIndex = 0
appendAttributes1Display.GaussianRadius = 0.2
appendAttributes1Display.ShaderPreset = 'Sphere'
appendAttributes1Display.CustomTriangleScale = 3
appendAttributes1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
appendAttributes1Display.Emissive = 0
appendAttributes1Display.ScaleByArray = 0
appendAttributes1Display.SetScaleArray = ['POINTS', 'du_11']
appendAttributes1Display.ScaleArrayComponent = ''
appendAttributes1Display.UseScaleFunction = 1
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityByArray = 0
appendAttributes1Display.OpacityArray = ['POINTS', 'du_11']
appendAttributes1Display.OpacityArrayComponent = ''
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.SelectionCellLabelBold = 0
appendAttributes1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
appendAttributes1Display.SelectionCellLabelFontFamily = 'Arial'
appendAttributes1Display.SelectionCellLabelFontFile = ''
appendAttributes1Display.SelectionCellLabelFontSize = 18
appendAttributes1Display.SelectionCellLabelItalic = 0
appendAttributes1Display.SelectionCellLabelJustification = 'Left'
appendAttributes1Display.SelectionCellLabelOpacity = 1.0
appendAttributes1Display.SelectionCellLabelShadow = 0
appendAttributes1Display.SelectionPointLabelBold = 0
appendAttributes1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
appendAttributes1Display.SelectionPointLabelFontFamily = 'Arial'
appendAttributes1Display.SelectionPointLabelFontFile = ''
appendAttributes1Display.SelectionPointLabelFontSize = 18
appendAttributes1Display.SelectionPointLabelItalic = 0
appendAttributes1Display.SelectionPointLabelJustification = 'Left'
appendAttributes1Display.SelectionPointLabelOpacity = 1.0
appendAttributes1Display.SelectionPointLabelShadow = 0
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityFunction = None
appendAttributes1Display.ScalarOpacityUnitDistance = 4.330127018922194
appendAttributes1Display.UseSeparateOpacityArray = 0
appendAttributes1Display.OpacityArrayName = ['POINTS', 'du_11']
appendAttributes1Display.OpacityComponent = ''
appendAttributes1Display.SelectMapper = 'Projected tetra'
appendAttributes1Display.SamplingDimensions = [128, 128, 128]
appendAttributes1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
appendAttributes1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
appendAttributes1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
appendAttributes1Display.GlyphType.TipResolution = 6
appendAttributes1Display.GlyphType.TipRadius = 0.1
appendAttributes1Display.GlyphType.TipLength = 0.35
appendAttributes1Display.GlyphType.ShaftResolution = 6
appendAttributes1Display.GlyphType.ShaftRadius = 0.03
appendAttributes1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
appendAttributes1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
appendAttributes1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
appendAttributes1Display.DataAxesGrid.XTitle = 'X Axis'
appendAttributes1Display.DataAxesGrid.YTitle = 'Y Axis'
appendAttributes1Display.DataAxesGrid.ZTitle = 'Z Axis'
appendAttributes1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.XTitleFontFile = ''
appendAttributes1Display.DataAxesGrid.XTitleBold = 0
appendAttributes1Display.DataAxesGrid.XTitleItalic = 0
appendAttributes1Display.DataAxesGrid.XTitleFontSize = 12
appendAttributes1Display.DataAxesGrid.XTitleShadow = 0
appendAttributes1Display.DataAxesGrid.XTitleOpacity = 1.0
appendAttributes1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.YTitleFontFile = ''
appendAttributes1Display.DataAxesGrid.YTitleBold = 0
appendAttributes1Display.DataAxesGrid.YTitleItalic = 0
appendAttributes1Display.DataAxesGrid.YTitleFontSize = 12
appendAttributes1Display.DataAxesGrid.YTitleShadow = 0
appendAttributes1Display.DataAxesGrid.YTitleOpacity = 1.0
appendAttributes1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.ZTitleFontFile = ''
appendAttributes1Display.DataAxesGrid.ZTitleBold = 0
appendAttributes1Display.DataAxesGrid.ZTitleItalic = 0
appendAttributes1Display.DataAxesGrid.ZTitleFontSize = 12
appendAttributes1Display.DataAxesGrid.ZTitleShadow = 0
appendAttributes1Display.DataAxesGrid.ZTitleOpacity = 1.0
appendAttributes1Display.DataAxesGrid.FacesToRender = 63
appendAttributes1Display.DataAxesGrid.CullBackface = 0
appendAttributes1Display.DataAxesGrid.CullFrontface = 1
appendAttributes1Display.DataAxesGrid.ShowGrid = 0
appendAttributes1Display.DataAxesGrid.ShowEdges = 1
appendAttributes1Display.DataAxesGrid.ShowTicks = 1
appendAttributes1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
appendAttributes1Display.DataAxesGrid.AxesToLabel = 63
appendAttributes1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.XLabelFontFile = ''
appendAttributes1Display.DataAxesGrid.XLabelBold = 0
appendAttributes1Display.DataAxesGrid.XLabelItalic = 0
appendAttributes1Display.DataAxesGrid.XLabelFontSize = 12
appendAttributes1Display.DataAxesGrid.XLabelShadow = 0
appendAttributes1Display.DataAxesGrid.XLabelOpacity = 1.0
appendAttributes1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.YLabelFontFile = ''
appendAttributes1Display.DataAxesGrid.YLabelBold = 0
appendAttributes1Display.DataAxesGrid.YLabelItalic = 0
appendAttributes1Display.DataAxesGrid.YLabelFontSize = 12
appendAttributes1Display.DataAxesGrid.YLabelShadow = 0
appendAttributes1Display.DataAxesGrid.YLabelOpacity = 1.0
appendAttributes1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.ZLabelFontFile = ''
appendAttributes1Display.DataAxesGrid.ZLabelBold = 0
appendAttributes1Display.DataAxesGrid.ZLabelItalic = 0
appendAttributes1Display.DataAxesGrid.ZLabelFontSize = 12
appendAttributes1Display.DataAxesGrid.ZLabelShadow = 0
appendAttributes1Display.DataAxesGrid.ZLabelOpacity = 1.0
appendAttributes1Display.DataAxesGrid.XAxisNotation = 'Mixed'
appendAttributes1Display.DataAxesGrid.XAxisPrecision = 2
appendAttributes1Display.DataAxesGrid.XAxisUseCustomLabels = 0
appendAttributes1Display.DataAxesGrid.XAxisLabels = []
appendAttributes1Display.DataAxesGrid.YAxisNotation = 'Mixed'
appendAttributes1Display.DataAxesGrid.YAxisPrecision = 2
appendAttributes1Display.DataAxesGrid.YAxisUseCustomLabels = 0
appendAttributes1Display.DataAxesGrid.YAxisLabels = []
appendAttributes1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
appendAttributes1Display.DataAxesGrid.ZAxisPrecision = 2
appendAttributes1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
appendAttributes1Display.DataAxesGrid.ZAxisLabels = []
appendAttributes1Display.DataAxesGrid.UseCustomBounds = 0
appendAttributes1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
appendAttributes1Display.PolarAxes.Visibility = 0
appendAttributes1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
appendAttributes1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
appendAttributes1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
appendAttributes1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
appendAttributes1Display.PolarAxes.EnableCustomRange = 0
appendAttributes1Display.PolarAxes.CustomRange = [0.0, 1.0]
appendAttributes1Display.PolarAxes.PolarAxisVisibility = 1
appendAttributes1Display.PolarAxes.RadialAxesVisibility = 1
appendAttributes1Display.PolarAxes.DrawRadialGridlines = 1
appendAttributes1Display.PolarAxes.PolarArcsVisibility = 1
appendAttributes1Display.PolarAxes.DrawPolarArcsGridlines = 1
appendAttributes1Display.PolarAxes.NumberOfRadialAxes = 0
appendAttributes1Display.PolarAxes.AutoSubdividePolarAxis = 1
appendAttributes1Display.PolarAxes.NumberOfPolarAxis = 0
appendAttributes1Display.PolarAxes.MinimumRadius = 0.0
appendAttributes1Display.PolarAxes.MinimumAngle = 0.0
appendAttributes1Display.PolarAxes.MaximumAngle = 90.0
appendAttributes1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
appendAttributes1Display.PolarAxes.Ratio = 1.0
appendAttributes1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.PolarAxisTitleVisibility = 1
appendAttributes1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
appendAttributes1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
appendAttributes1Display.PolarAxes.PolarLabelVisibility = 1
appendAttributes1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
appendAttributes1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
appendAttributes1Display.PolarAxes.RadialLabelVisibility = 1
appendAttributes1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
appendAttributes1Display.PolarAxes.RadialLabelLocation = 'Bottom'
appendAttributes1Display.PolarAxes.RadialUnitsVisibility = 1
appendAttributes1Display.PolarAxes.ScreenSize = 10.0
appendAttributes1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
appendAttributes1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.PolarAxisTitleFontFile = ''
appendAttributes1Display.PolarAxes.PolarAxisTitleBold = 0
appendAttributes1Display.PolarAxes.PolarAxisTitleItalic = 0
appendAttributes1Display.PolarAxes.PolarAxisTitleShadow = 0
appendAttributes1Display.PolarAxes.PolarAxisTitleFontSize = 12
appendAttributes1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
appendAttributes1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.PolarAxisLabelFontFile = ''
appendAttributes1Display.PolarAxes.PolarAxisLabelBold = 0
appendAttributes1Display.PolarAxes.PolarAxisLabelItalic = 0
appendAttributes1Display.PolarAxes.PolarAxisLabelShadow = 0
appendAttributes1Display.PolarAxes.PolarAxisLabelFontSize = 12
appendAttributes1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
appendAttributes1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.LastRadialAxisTextFontFile = ''
appendAttributes1Display.PolarAxes.LastRadialAxisTextBold = 0
appendAttributes1Display.PolarAxes.LastRadialAxisTextItalic = 0
appendAttributes1Display.PolarAxes.LastRadialAxisTextShadow = 0
appendAttributes1Display.PolarAxes.LastRadialAxisTextFontSize = 12
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
appendAttributes1Display.PolarAxes.EnableDistanceLOD = 1
appendAttributes1Display.PolarAxes.DistanceLODThreshold = 0.7
appendAttributes1Display.PolarAxes.EnableViewAngleLOD = 1
appendAttributes1Display.PolarAxes.ViewAngleLODThreshold = 0.7
appendAttributes1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
appendAttributes1Display.PolarAxes.PolarTicksVisibility = 1
appendAttributes1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
appendAttributes1Display.PolarAxes.TickLocation = 'Both'
appendAttributes1Display.PolarAxes.AxisTickVisibility = 1
appendAttributes1Display.PolarAxes.AxisMinorTickVisibility = 0
appendAttributes1Display.PolarAxes.ArcTickVisibility = 1
appendAttributes1Display.PolarAxes.ArcMinorTickVisibility = 0
appendAttributes1Display.PolarAxes.DeltaAngleMajor = 10.0
appendAttributes1Display.PolarAxes.DeltaAngleMinor = 5.0
appendAttributes1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
appendAttributes1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
appendAttributes1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
appendAttributes1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
appendAttributes1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
appendAttributes1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
appendAttributes1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
appendAttributes1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
appendAttributes1Display.PolarAxes.ArcMajorTickSize = 0.0
appendAttributes1Display.PolarAxes.ArcTickRatioSize = 0.3
appendAttributes1Display.PolarAxes.ArcMajorTickThickness = 1.0
appendAttributes1Display.PolarAxes.ArcTickRatioThickness = 0.5
appendAttributes1Display.PolarAxes.Use2DMode = 0
appendAttributes1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(mergeVectorComponents1, renderView1)

# hide data in view
Hide(mergeVectorComponents2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=appendAttributes1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'm']
streamTracer1.InterpolatorType = 'Interpolator with Point Locator'
streamTracer1.SurfaceStreamlines = 0
streamTracer1.IntegrationDirection = 'BOTH'
streamTracer1.IntegratorType = 'Runge-Kutta 4-5'
streamTracer1.IntegrationStepUnit = 'Cell Length'
streamTracer1.InitialStepLength = 0.2
streamTracer1.MinimumStepLength = 0.01
streamTracer1.MaximumStepLength = 0.5
streamTracer1.MaximumSteps = 2000
streamTracer1.MaximumStreamlineLength = 40.0
streamTracer1.TerminalSpeed = 1e-12
streamTracer1.MaximumError = 1e-06
streamTracer1.ComputeVorticity = 1

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-20.0, -20.0, -20.0]
streamTracer1.SeedType.Point2 = [20.0, 20.0, 20.0]
streamTracer1.SeedType.Resolution = 1000

# set active source
SetActiveSource(appendAttributes1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1.SeedType)

# destroy streamTracer1
Delete(streamTracer1)
del streamTracer1

# set active source
SetActiveSource(appendAttributes1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=appendAttributes1)
calculator1.AttributeType = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'Result'
calculator1.Function = ''
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0
calculator1.ResultArrayType = 'Double'

# Properties modified on calculator1
calculator1.ResultArrayName = 'l'
calculator1.Function = 'cross(m,n)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Selection = None
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.LookupTable = None
calculator1Display.MapScalars = 1
calculator1Display.MultiComponentsMapping = 0
calculator1Display.InterpolateScalarsBeforeMapping = 1
calculator1Display.Opacity = 1.0
calculator1Display.PointSize = 2.0
calculator1Display.LineWidth = 1.0
calculator1Display.RenderLinesAsTubes = 0
calculator1Display.RenderPointsAsSpheres = 0
calculator1Display.Interpolation = 'Gouraud'
calculator1Display.Specular = 0.0
calculator1Display.SpecularColor = [1.0, 1.0, 1.0]
calculator1Display.SpecularPower = 100.0
calculator1Display.Luminosity = 0.0
calculator1Display.Ambient = 0.0
calculator1Display.Diffuse = 1.0
calculator1Display.Roughness = 0.3
calculator1Display.Metallic = 0.0
calculator1Display.EdgeTint = [1.0, 1.0, 1.0]
calculator1Display.Anisotropy = 0.0
calculator1Display.AnisotropyRotation = 0.0
calculator1Display.BaseIOR = 1.5
calculator1Display.CoatStrength = 0.0
calculator1Display.CoatIOR = 2.0
calculator1Display.CoatRoughness = 0.0
calculator1Display.CoatColor = [1.0, 1.0, 1.0]
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.Texture = None
calculator1Display.RepeatTextures = 1
calculator1Display.InterpolateTextures = 0
calculator1Display.SeamlessU = 0
calculator1Display.SeamlessV = 0
calculator1Display.UseMipmapTextures = 0
calculator1Display.ShowTexturesOnBackface = 1
calculator1Display.BaseColorTexture = None
calculator1Display.NormalTexture = None
calculator1Display.NormalScale = 1.0
calculator1Display.CoatNormalTexture = None
calculator1Display.CoatNormalScale = 1.0
calculator1Display.MaterialTexture = None
calculator1Display.OcclusionStrength = 1.0
calculator1Display.AnisotropyTexture = None
calculator1Display.EmissiveTexture = None
calculator1Display.EmissiveFactor = [1.0, 1.0, 1.0]
calculator1Display.FlipTextures = 0
calculator1Display.BackfaceRepresentation = 'Follow Frontface'
calculator1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
calculator1Display.BackfaceOpacity = 1.0
calculator1Display.Position = [0.0, 0.0, 0.0]
calculator1Display.Scale = [1.0, 1.0, 1.0]
calculator1Display.Orientation = [0.0, 0.0, 0.0]
calculator1Display.Origin = [0.0, 0.0, 0.0]
calculator1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
calculator1Display.Pickable = 1
calculator1Display.Triangulate = 0
calculator1Display.UseShaderReplacements = 0
calculator1Display.ShaderReplacements = ''
calculator1Display.NonlinearSubdivisionLevel = 1
calculator1Display.UseDataPartitions = 0
calculator1Display.OSPRayUseScaleArray = 'All Approximate'
calculator1Display.OSPRayScaleArray = 'du_11'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.OSPRayMaterial = 'None'
calculator1Display.BlockSelectors = ['/']
calculator1Display.BlockColors = []
calculator1Display.BlockOpacities = []
calculator1Display.Orient = 0
calculator1Display.OrientationMode = 'Direction'
calculator1Display.SelectOrientationVectors = 'l'
calculator1Display.Scaling = 0
calculator1Display.ScaleMode = 'No Data Scaling Off'
calculator1Display.ScaleFactor = 4.0
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.UseGlyphTable = 0
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.UseCompositeGlyphTable = 0
calculator1Display.UseGlyphCullingAndLOD = 0
calculator1Display.LODValues = []
calculator1Display.ColorByLODIndex = 0
calculator1Display.GaussianRadius = 0.2
calculator1Display.ShaderPreset = 'Sphere'
calculator1Display.CustomTriangleScale = 3
calculator1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
calculator1Display.Emissive = 0
calculator1Display.ScaleByArray = 0
calculator1Display.SetScaleArray = ['POINTS', 'du_11']
calculator1Display.ScaleArrayComponent = ''
calculator1Display.UseScaleFunction = 1
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityByArray = 0
calculator1Display.OpacityArray = ['POINTS', 'du_11']
calculator1Display.OpacityArrayComponent = ''
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelBold = 0
calculator1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
calculator1Display.SelectionCellLabelFontFamily = 'Arial'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionCellLabelFontSize = 18
calculator1Display.SelectionCellLabelItalic = 0
calculator1Display.SelectionCellLabelJustification = 'Left'
calculator1Display.SelectionCellLabelOpacity = 1.0
calculator1Display.SelectionCellLabelShadow = 0
calculator1Display.SelectionPointLabelBold = 0
calculator1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
calculator1Display.SelectionPointLabelFontFamily = 'Arial'
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.SelectionPointLabelFontSize = 18
calculator1Display.SelectionPointLabelItalic = 0
calculator1Display.SelectionPointLabelJustification = 'Left'
calculator1Display.SelectionPointLabelOpacity = 1.0
calculator1Display.SelectionPointLabelShadow = 0
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = None
calculator1Display.ScalarOpacityUnitDistance = 4.330127018922194
calculator1Display.UseSeparateOpacityArray = 0
calculator1Display.OpacityArrayName = ['POINTS', 'du_11']
calculator1Display.OpacityComponent = ''
calculator1Display.SelectMapper = 'Projected tetra'
calculator1Display.SamplingDimensions = [128, 128, 128]
calculator1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
calculator1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
calculator1Display.GlyphType.TipResolution = 6
calculator1Display.GlyphType.TipRadius = 0.1
calculator1Display.GlyphType.TipLength = 0.35
calculator1Display.GlyphType.ShaftResolution = 6
calculator1Display.GlyphType.ShaftRadius = 0.03
calculator1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
calculator1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-0.00037579747731797397, 0.0, 0.5, 0.0, 0.000195453452761285, 1.0, 0.5, 0.0]
calculator1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitle = 'X Axis'
calculator1Display.DataAxesGrid.YTitle = 'Y Axis'
calculator1Display.DataAxesGrid.ZTitle = 'Z Axis'
calculator1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.XTitleBold = 0
calculator1Display.DataAxesGrid.XTitleItalic = 0
calculator1Display.DataAxesGrid.XTitleFontSize = 12
calculator1Display.DataAxesGrid.XTitleShadow = 0
calculator1Display.DataAxesGrid.XTitleOpacity = 1.0
calculator1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleBold = 0
calculator1Display.DataAxesGrid.YTitleItalic = 0
calculator1Display.DataAxesGrid.YTitleFontSize = 12
calculator1Display.DataAxesGrid.YTitleShadow = 0
calculator1Display.DataAxesGrid.YTitleOpacity = 1.0
calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleBold = 0
calculator1Display.DataAxesGrid.ZTitleItalic = 0
calculator1Display.DataAxesGrid.ZTitleFontSize = 12
calculator1Display.DataAxesGrid.ZTitleShadow = 0
calculator1Display.DataAxesGrid.ZTitleOpacity = 1.0
calculator1Display.DataAxesGrid.FacesToRender = 63
calculator1Display.DataAxesGrid.CullBackface = 0
calculator1Display.DataAxesGrid.CullFrontface = 1
calculator1Display.DataAxesGrid.ShowGrid = 0
calculator1Display.DataAxesGrid.ShowEdges = 1
calculator1Display.DataAxesGrid.ShowTicks = 1
calculator1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
calculator1Display.DataAxesGrid.AxesToLabel = 63
calculator1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.XLabelBold = 0
calculator1Display.DataAxesGrid.XLabelItalic = 0
calculator1Display.DataAxesGrid.XLabelFontSize = 12
calculator1Display.DataAxesGrid.XLabelShadow = 0
calculator1Display.DataAxesGrid.XLabelOpacity = 1.0
calculator1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelBold = 0
calculator1Display.DataAxesGrid.YLabelItalic = 0
calculator1Display.DataAxesGrid.YLabelFontSize = 12
calculator1Display.DataAxesGrid.YLabelShadow = 0
calculator1Display.DataAxesGrid.YLabelOpacity = 1.0
calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelBold = 0
calculator1Display.DataAxesGrid.ZLabelItalic = 0
calculator1Display.DataAxesGrid.ZLabelFontSize = 12
calculator1Display.DataAxesGrid.ZLabelShadow = 0
calculator1Display.DataAxesGrid.ZLabelOpacity = 1.0
calculator1Display.DataAxesGrid.XAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.XAxisPrecision = 2
calculator1Display.DataAxesGrid.XAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.XAxisLabels = []
calculator1Display.DataAxesGrid.YAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.YAxisPrecision = 2
calculator1Display.DataAxesGrid.YAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.YAxisLabels = []
calculator1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.ZAxisPrecision = 2
calculator1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.ZAxisLabels = []
calculator1Display.DataAxesGrid.UseCustomBounds = 0
calculator1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.Visibility = 0
calculator1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
calculator1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
calculator1Display.PolarAxes.EnableCustomRange = 0
calculator1Display.PolarAxes.CustomRange = [0.0, 1.0]
calculator1Display.PolarAxes.PolarAxisVisibility = 1
calculator1Display.PolarAxes.RadialAxesVisibility = 1
calculator1Display.PolarAxes.DrawRadialGridlines = 1
calculator1Display.PolarAxes.PolarArcsVisibility = 1
calculator1Display.PolarAxes.DrawPolarArcsGridlines = 1
calculator1Display.PolarAxes.NumberOfRadialAxes = 0
calculator1Display.PolarAxes.AutoSubdividePolarAxis = 1
calculator1Display.PolarAxes.NumberOfPolarAxis = 0
calculator1Display.PolarAxes.MinimumRadius = 0.0
calculator1Display.PolarAxes.MinimumAngle = 0.0
calculator1Display.PolarAxes.MaximumAngle = 90.0
calculator1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
calculator1Display.PolarAxes.Ratio = 1.0
calculator1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisTitleVisibility = 1
calculator1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
calculator1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
calculator1Display.PolarAxes.PolarLabelVisibility = 1
calculator1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
calculator1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
calculator1Display.PolarAxes.RadialLabelVisibility = 1
calculator1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
calculator1Display.PolarAxes.RadialLabelLocation = 'Bottom'
calculator1Display.PolarAxes.RadialUnitsVisibility = 1
calculator1Display.PolarAxes.ScreenSize = 10.0
calculator1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisTitleBold = 0
calculator1Display.PolarAxes.PolarAxisTitleItalic = 0
calculator1Display.PolarAxes.PolarAxisTitleShadow = 0
calculator1Display.PolarAxes.PolarAxisTitleFontSize = 12
calculator1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelBold = 0
calculator1Display.PolarAxes.PolarAxisLabelItalic = 0
calculator1Display.PolarAxes.PolarAxisLabelShadow = 0
calculator1Display.PolarAxes.PolarAxisLabelFontSize = 12
calculator1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
calculator1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextBold = 0
calculator1Display.PolarAxes.LastRadialAxisTextItalic = 0
calculator1Display.PolarAxes.LastRadialAxisTextShadow = 0
calculator1Display.PolarAxes.LastRadialAxisTextFontSize = 12
calculator1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
calculator1Display.PolarAxes.EnableDistanceLOD = 1
calculator1Display.PolarAxes.DistanceLODThreshold = 0.7
calculator1Display.PolarAxes.EnableViewAngleLOD = 1
calculator1Display.PolarAxes.ViewAngleLODThreshold = 0.7
calculator1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
calculator1Display.PolarAxes.PolarTicksVisibility = 1
calculator1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
calculator1Display.PolarAxes.TickLocation = 'Both'
calculator1Display.PolarAxes.AxisTickVisibility = 1
calculator1Display.PolarAxes.AxisMinorTickVisibility = 0
calculator1Display.PolarAxes.ArcTickVisibility = 1
calculator1Display.PolarAxes.ArcMinorTickVisibility = 0
calculator1Display.PolarAxes.DeltaAngleMajor = 10.0
calculator1Display.PolarAxes.DeltaAngleMinor = 5.0
calculator1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.ArcMajorTickSize = 0.0
calculator1Display.PolarAxes.ArcTickRatioSize = 0.3
calculator1Display.PolarAxes.ArcMajorTickThickness = 1.0
calculator1Display.PolarAxes.ArcTickRatioThickness = 0.5
calculator1Display.PolarAxes.Use2DMode = 0
calculator1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(appendAttributes1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculator1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'l']
streamTracer1.InterpolatorType = 'Interpolator with Point Locator'
streamTracer1.SurfaceStreamlines = 0
streamTracer1.IntegrationDirection = 'BOTH'
streamTracer1.IntegratorType = 'Runge-Kutta 4-5'
streamTracer1.IntegrationStepUnit = 'Cell Length'
streamTracer1.InitialStepLength = 0.2
streamTracer1.MinimumStepLength = 0.01
streamTracer1.MaximumStepLength = 0.5
streamTracer1.MaximumSteps = 2000
streamTracer1.MaximumStreamlineLength = 40.0
streamTracer1.TerminalSpeed = 1e-12
streamTracer1.MaximumError = 1e-06
streamTracer1.ComputeVorticity = 1

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-20.0, -20.0, -20.0]
streamTracer1.SeedType.Point2 = [20.0, 20.0, 20.0]
streamTracer1.SeedType.Resolution = 1000

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer1.SeedType)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1.SeedType)

# Properties modified on streamTracer1
streamTracer1.SeedType = 'Point Cloud'

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Selection = None
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.LookupTable = None
streamTracer1Display.MapScalars = 1
streamTracer1Display.MultiComponentsMapping = 0
streamTracer1Display.InterpolateScalarsBeforeMapping = 1
streamTracer1Display.Opacity = 1.0
streamTracer1Display.PointSize = 2.0
streamTracer1Display.LineWidth = 1.0
streamTracer1Display.RenderLinesAsTubes = 0
streamTracer1Display.RenderPointsAsSpheres = 0
streamTracer1Display.Interpolation = 'Gouraud'
streamTracer1Display.Specular = 0.0
streamTracer1Display.SpecularColor = [1.0, 1.0, 1.0]
streamTracer1Display.SpecularPower = 100.0
streamTracer1Display.Luminosity = 0.0
streamTracer1Display.Ambient = 0.0
streamTracer1Display.Diffuse = 1.0
streamTracer1Display.Roughness = 0.3
streamTracer1Display.Metallic = 0.0
streamTracer1Display.EdgeTint = [1.0, 1.0, 1.0]
streamTracer1Display.Anisotropy = 0.0
streamTracer1Display.AnisotropyRotation = 0.0
streamTracer1Display.BaseIOR = 1.5
streamTracer1Display.CoatStrength = 0.0
streamTracer1Display.CoatIOR = 2.0
streamTracer1Display.CoatRoughness = 0.0
streamTracer1Display.CoatColor = [1.0, 1.0, 1.0]
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.Texture = None
streamTracer1Display.RepeatTextures = 1
streamTracer1Display.InterpolateTextures = 0
streamTracer1Display.SeamlessU = 0
streamTracer1Display.SeamlessV = 0
streamTracer1Display.UseMipmapTextures = 0
streamTracer1Display.ShowTexturesOnBackface = 1
streamTracer1Display.BaseColorTexture = None
streamTracer1Display.NormalTexture = None
streamTracer1Display.NormalScale = 1.0
streamTracer1Display.CoatNormalTexture = None
streamTracer1Display.CoatNormalScale = 1.0
streamTracer1Display.MaterialTexture = None
streamTracer1Display.OcclusionStrength = 1.0
streamTracer1Display.AnisotropyTexture = None
streamTracer1Display.EmissiveTexture = None
streamTracer1Display.EmissiveFactor = [1.0, 1.0, 1.0]
streamTracer1Display.FlipTextures = 0
streamTracer1Display.BackfaceRepresentation = 'Follow Frontface'
streamTracer1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
streamTracer1Display.BackfaceOpacity = 1.0
streamTracer1Display.Position = [0.0, 0.0, 0.0]
streamTracer1Display.Scale = [1.0, 1.0, 1.0]
streamTracer1Display.Orientation = [0.0, 0.0, 0.0]
streamTracer1Display.Origin = [0.0, 0.0, 0.0]
streamTracer1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
streamTracer1Display.Pickable = 1
streamTracer1Display.Triangulate = 0
streamTracer1Display.UseShaderReplacements = 0
streamTracer1Display.ShaderReplacements = ''
streamTracer1Display.NonlinearSubdivisionLevel = 1
streamTracer1Display.UseDataPartitions = 0
streamTracer1Display.OSPRayUseScaleArray = 'All Approximate'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.OSPRayMaterial = 'None'
streamTracer1Display.BlockSelectors = ['/']
streamTracer1Display.BlockColors = []
streamTracer1Display.BlockOpacities = []
streamTracer1Display.Orient = 0
streamTracer1Display.OrientationMode = 'Direction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.Scaling = 0
streamTracer1Display.ScaleMode = 'No Data Scaling Off'
streamTracer1Display.ScaleFactor = 3.9993005752563477
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.UseGlyphTable = 0
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.UseCompositeGlyphTable = 0
streamTracer1Display.UseGlyphCullingAndLOD = 0
streamTracer1Display.LODValues = []
streamTracer1Display.ColorByLODIndex = 0
streamTracer1Display.GaussianRadius = 0.19996502876281738
streamTracer1Display.ShaderPreset = 'Sphere'
streamTracer1Display.CustomTriangleScale = 3
streamTracer1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
streamTracer1Display.Emissive = 0
streamTracer1Display.ScaleByArray = 0
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleArrayComponent = ''
streamTracer1Display.UseScaleFunction = 1
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityByArray = 0
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityArrayComponent = ''
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.SelectionCellLabelBold = 0
streamTracer1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
streamTracer1Display.SelectionCellLabelFontFamily = 'Arial'
streamTracer1Display.SelectionCellLabelFontFile = ''
streamTracer1Display.SelectionCellLabelFontSize = 18
streamTracer1Display.SelectionCellLabelItalic = 0
streamTracer1Display.SelectionCellLabelJustification = 'Left'
streamTracer1Display.SelectionCellLabelOpacity = 1.0
streamTracer1Display.SelectionCellLabelShadow = 0
streamTracer1Display.SelectionPointLabelBold = 0
streamTracer1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
streamTracer1Display.SelectionPointLabelFontFamily = 'Arial'
streamTracer1Display.SelectionPointLabelFontFile = ''
streamTracer1Display.SelectionPointLabelFontSize = 18
streamTracer1Display.SelectionPointLabelItalic = 0
streamTracer1Display.SelectionPointLabelJustification = 'Left'
streamTracer1Display.SelectionPointLabelOpacity = 1.0
streamTracer1Display.SelectionPointLabelShadow = 0
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
streamTracer1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
streamTracer1Display.GlyphType.TipResolution = 6
streamTracer1Display.GlyphType.TipRadius = 0.1
streamTracer1Display.GlyphType.TipLength = 0.35
streamTracer1Display.GlyphType.ShaftResolution = 6
streamTracer1Display.GlyphType.ShaftRadius = 0.03
streamTracer1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-0.033654804052246745, 0.0, 0.5, 0.0, 0.03305225048306748, 1.0, 0.5, 0.0]
streamTracer1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-0.033654804052246745, 0.0, 0.5, 0.0, 0.03305225048306748, 1.0, 0.5, 0.0]
streamTracer1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer1Display.DataAxesGrid.XTitle = 'X Axis'
streamTracer1Display.DataAxesGrid.YTitle = 'Y Axis'
streamTracer1Display.DataAxesGrid.ZTitle = 'Z Axis'
streamTracer1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.XTitleFontFile = ''
streamTracer1Display.DataAxesGrid.XTitleBold = 0
streamTracer1Display.DataAxesGrid.XTitleItalic = 0
streamTracer1Display.DataAxesGrid.XTitleFontSize = 12
streamTracer1Display.DataAxesGrid.XTitleShadow = 0
streamTracer1Display.DataAxesGrid.XTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.YTitleFontFile = ''
streamTracer1Display.DataAxesGrid.YTitleBold = 0
streamTracer1Display.DataAxesGrid.YTitleItalic = 0
streamTracer1Display.DataAxesGrid.YTitleFontSize = 12
streamTracer1Display.DataAxesGrid.YTitleShadow = 0
streamTracer1Display.DataAxesGrid.YTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.ZTitleFontFile = ''
streamTracer1Display.DataAxesGrid.ZTitleBold = 0
streamTracer1Display.DataAxesGrid.ZTitleItalic = 0
streamTracer1Display.DataAxesGrid.ZTitleFontSize = 12
streamTracer1Display.DataAxesGrid.ZTitleShadow = 0
streamTracer1Display.DataAxesGrid.ZTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.FacesToRender = 63
streamTracer1Display.DataAxesGrid.CullBackface = 0
streamTracer1Display.DataAxesGrid.CullFrontface = 1
streamTracer1Display.DataAxesGrid.ShowGrid = 0
streamTracer1Display.DataAxesGrid.ShowEdges = 1
streamTracer1Display.DataAxesGrid.ShowTicks = 1
streamTracer1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
streamTracer1Display.DataAxesGrid.AxesToLabel = 63
streamTracer1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.XLabelFontFile = ''
streamTracer1Display.DataAxesGrid.XLabelBold = 0
streamTracer1Display.DataAxesGrid.XLabelItalic = 0
streamTracer1Display.DataAxesGrid.XLabelFontSize = 12
streamTracer1Display.DataAxesGrid.XLabelShadow = 0
streamTracer1Display.DataAxesGrid.XLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.YLabelFontFile = ''
streamTracer1Display.DataAxesGrid.YLabelBold = 0
streamTracer1Display.DataAxesGrid.YLabelItalic = 0
streamTracer1Display.DataAxesGrid.YLabelFontSize = 12
streamTracer1Display.DataAxesGrid.YLabelShadow = 0
streamTracer1Display.DataAxesGrid.YLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.ZLabelFontFile = ''
streamTracer1Display.DataAxesGrid.ZLabelBold = 0
streamTracer1Display.DataAxesGrid.ZLabelItalic = 0
streamTracer1Display.DataAxesGrid.ZLabelFontSize = 12
streamTracer1Display.DataAxesGrid.ZLabelShadow = 0
streamTracer1Display.DataAxesGrid.ZLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.XAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.XAxisPrecision = 2
streamTracer1Display.DataAxesGrid.XAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.XAxisLabels = []
streamTracer1Display.DataAxesGrid.YAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.YAxisPrecision = 2
streamTracer1Display.DataAxesGrid.YAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.YAxisLabels = []
streamTracer1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.ZAxisPrecision = 2
streamTracer1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.ZAxisLabels = []
streamTracer1Display.DataAxesGrid.UseCustomBounds = 0
streamTracer1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer1Display.PolarAxes.Visibility = 0
streamTracer1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
streamTracer1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
streamTracer1Display.PolarAxes.EnableCustomRange = 0
streamTracer1Display.PolarAxes.CustomRange = [0.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisVisibility = 1
streamTracer1Display.PolarAxes.RadialAxesVisibility = 1
streamTracer1Display.PolarAxes.DrawRadialGridlines = 1
streamTracer1Display.PolarAxes.PolarArcsVisibility = 1
streamTracer1Display.PolarAxes.DrawPolarArcsGridlines = 1
streamTracer1Display.PolarAxes.NumberOfRadialAxes = 0
streamTracer1Display.PolarAxes.AutoSubdividePolarAxis = 1
streamTracer1Display.PolarAxes.NumberOfPolarAxis = 0
streamTracer1Display.PolarAxes.MinimumRadius = 0.0
streamTracer1Display.PolarAxes.MinimumAngle = 0.0
streamTracer1Display.PolarAxes.MaximumAngle = 90.0
streamTracer1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
streamTracer1Display.PolarAxes.Ratio = 1.0
streamTracer1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisTitleVisibility = 1
streamTracer1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
streamTracer1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
streamTracer1Display.PolarAxes.PolarLabelVisibility = 1
streamTracer1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
streamTracer1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
streamTracer1Display.PolarAxes.RadialLabelVisibility = 1
streamTracer1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
streamTracer1Display.PolarAxes.RadialLabelLocation = 'Bottom'
streamTracer1Display.PolarAxes.RadialUnitsVisibility = 1
streamTracer1Display.PolarAxes.ScreenSize = 10.0
streamTracer1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
streamTracer1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
streamTracer1Display.PolarAxes.PolarAxisTitleFontFile = ''
streamTracer1Display.PolarAxes.PolarAxisTitleBold = 0
streamTracer1Display.PolarAxes.PolarAxisTitleItalic = 0
streamTracer1Display.PolarAxes.PolarAxisTitleShadow = 0
streamTracer1Display.PolarAxes.PolarAxisTitleFontSize = 12
streamTracer1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
streamTracer1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
streamTracer1Display.PolarAxes.PolarAxisLabelFontFile = ''
streamTracer1Display.PolarAxes.PolarAxisLabelBold = 0
streamTracer1Display.PolarAxes.PolarAxisLabelItalic = 0
streamTracer1Display.PolarAxes.PolarAxisLabelShadow = 0
streamTracer1Display.PolarAxes.PolarAxisLabelFontSize = 12
streamTracer1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
streamTracer1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
streamTracer1Display.PolarAxes.LastRadialAxisTextFontFile = ''
streamTracer1Display.PolarAxes.LastRadialAxisTextBold = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextItalic = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextShadow = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextFontSize = 12
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
streamTracer1Display.PolarAxes.EnableDistanceLOD = 1
streamTracer1Display.PolarAxes.DistanceLODThreshold = 0.7
streamTracer1Display.PolarAxes.EnableViewAngleLOD = 1
streamTracer1Display.PolarAxes.ViewAngleLODThreshold = 0.7
streamTracer1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
streamTracer1Display.PolarAxes.PolarTicksVisibility = 1
streamTracer1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
streamTracer1Display.PolarAxes.TickLocation = 'Both'
streamTracer1Display.PolarAxes.AxisTickVisibility = 1
streamTracer1Display.PolarAxes.AxisMinorTickVisibility = 0
streamTracer1Display.PolarAxes.ArcTickVisibility = 1
streamTracer1Display.PolarAxes.ArcMinorTickVisibility = 0
streamTracer1Display.PolarAxes.DeltaAngleMajor = 10.0
streamTracer1Display.PolarAxes.DeltaAngleMinor = 5.0
streamTracer1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
streamTracer1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
streamTracer1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
streamTracer1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
streamTracer1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.ArcMajorTickSize = 0.0
streamTracer1Display.PolarAxes.ArcTickRatioSize = 0.3
streamTracer1Display.PolarAxes.ArcMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.ArcTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.Use2DMode = 0
streamTracer1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.NumberofSides = 6
tube1.Capping = 1
tube1.Radius = 0.39993005752563476
tube1.VaryRadius = 'Off'
tube1.RadiusFactor = 10.0
tube1.UseDefaultNormal = 0
tube1.DefaultNormal = [0.0, 0.0, 1.0]

# Properties modified on tube1
tube1.Vectors = ['POINTS', 'l']
tube1.Radius = 0.183967826461792

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Selection = None
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.LookupTable = None
tube1Display.MapScalars = 1
tube1Display.MultiComponentsMapping = 0
tube1Display.InterpolateScalarsBeforeMapping = 1
tube1Display.Opacity = 1.0
tube1Display.PointSize = 2.0
tube1Display.LineWidth = 1.0
tube1Display.RenderLinesAsTubes = 0
tube1Display.RenderPointsAsSpheres = 0
tube1Display.Interpolation = 'Gouraud'
tube1Display.Specular = 0.0
tube1Display.SpecularColor = [1.0, 1.0, 1.0]
tube1Display.SpecularPower = 100.0
tube1Display.Luminosity = 0.0
tube1Display.Ambient = 0.0
tube1Display.Diffuse = 1.0
tube1Display.Roughness = 0.3
tube1Display.Metallic = 0.0
tube1Display.EdgeTint = [1.0, 1.0, 1.0]
tube1Display.Anisotropy = 0.0
tube1Display.AnisotropyRotation = 0.0
tube1Display.BaseIOR = 1.5
tube1Display.CoatStrength = 0.0
tube1Display.CoatIOR = 2.0
tube1Display.CoatRoughness = 0.0
tube1Display.CoatColor = [1.0, 1.0, 1.0]
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.Texture = None
tube1Display.RepeatTextures = 1
tube1Display.InterpolateTextures = 0
tube1Display.SeamlessU = 0
tube1Display.SeamlessV = 0
tube1Display.UseMipmapTextures = 0
tube1Display.ShowTexturesOnBackface = 1
tube1Display.BaseColorTexture = None
tube1Display.NormalTexture = None
tube1Display.NormalScale = 1.0
tube1Display.CoatNormalTexture = None
tube1Display.CoatNormalScale = 1.0
tube1Display.MaterialTexture = None
tube1Display.OcclusionStrength = 1.0
tube1Display.AnisotropyTexture = None
tube1Display.EmissiveTexture = None
tube1Display.EmissiveFactor = [1.0, 1.0, 1.0]
tube1Display.FlipTextures = 0
tube1Display.BackfaceRepresentation = 'Follow Frontface'
tube1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
tube1Display.BackfaceOpacity = 1.0
tube1Display.Position = [0.0, 0.0, 0.0]
tube1Display.Scale = [1.0, 1.0, 1.0]
tube1Display.Orientation = [0.0, 0.0, 0.0]
tube1Display.Origin = [0.0, 0.0, 0.0]
tube1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
tube1Display.Pickable = 1
tube1Display.Triangulate = 0
tube1Display.UseShaderReplacements = 0
tube1Display.ShaderReplacements = ''
tube1Display.NonlinearSubdivisionLevel = 1
tube1Display.UseDataPartitions = 0
tube1Display.OSPRayUseScaleArray = 'All Approximate'
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.OSPRayMaterial = 'None'
tube1Display.BlockSelectors = ['/']
tube1Display.BlockColors = []
tube1Display.BlockOpacities = []
tube1Display.Orient = 0
tube1Display.OrientationMode = 'Direction'
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.Scaling = 0
tube1Display.ScaleMode = 'No Data Scaling Off'
tube1Display.ScaleFactor = 4.004527282714844
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.UseGlyphTable = 0
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.UseCompositeGlyphTable = 0
tube1Display.UseGlyphCullingAndLOD = 0
tube1Display.LODValues = []
tube1Display.ColorByLODIndex = 0
tube1Display.GaussianRadius = 0.20022636413574219
tube1Display.ShaderPreset = 'Sphere'
tube1Display.CustomTriangleScale = 3
tube1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
tube1Display.Emissive = 0
tube1Display.ScaleByArray = 0
tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display.ScaleArrayComponent = ''
tube1Display.UseScaleFunction = 1
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityByArray = 0
tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display.OpacityArrayComponent = ''
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelBold = 0
tube1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
tube1Display.SelectionCellLabelFontFamily = 'Arial'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionCellLabelFontSize = 18
tube1Display.SelectionCellLabelItalic = 0
tube1Display.SelectionCellLabelJustification = 'Left'
tube1Display.SelectionCellLabelOpacity = 1.0
tube1Display.SelectionCellLabelShadow = 0
tube1Display.SelectionPointLabelBold = 0
tube1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
tube1Display.SelectionPointLabelFontFamily = 'Arial'
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.SelectionPointLabelFontSize = 18
tube1Display.SelectionPointLabelItalic = 0
tube1Display.SelectionPointLabelJustification = 'Left'
tube1Display.SelectionPointLabelOpacity = 1.0
tube1Display.SelectionPointLabelShadow = 0
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
tube1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
tube1Display.GlyphType.TipResolution = 6
tube1Display.GlyphType.TipRadius = 0.1
tube1Display.GlyphType.TipLength = 0.35
tube1Display.GlyphType.ShaftResolution = 6
tube1Display.GlyphType.ShaftRadius = 0.03
tube1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-0.033654804052246745, 0.0, 0.5, 0.0, 0.03305225048306748, 1.0, 0.5, 0.0]
tube1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-0.033654804052246745, 0.0, 0.5, 0.0, 0.03305225048306748, 1.0, 0.5, 0.0]
tube1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display.DataAxesGrid.XTitle = 'X Axis'
tube1Display.DataAxesGrid.YTitle = 'Y Axis'
tube1Display.DataAxesGrid.ZTitle = 'Z Axis'
tube1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
tube1Display.DataAxesGrid.XTitleFontFile = ''
tube1Display.DataAxesGrid.XTitleBold = 0
tube1Display.DataAxesGrid.XTitleItalic = 0
tube1Display.DataAxesGrid.XTitleFontSize = 12
tube1Display.DataAxesGrid.XTitleShadow = 0
tube1Display.DataAxesGrid.XTitleOpacity = 1.0
tube1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
tube1Display.DataAxesGrid.YTitleFontFile = ''
tube1Display.DataAxesGrid.YTitleBold = 0
tube1Display.DataAxesGrid.YTitleItalic = 0
tube1Display.DataAxesGrid.YTitleFontSize = 12
tube1Display.DataAxesGrid.YTitleShadow = 0
tube1Display.DataAxesGrid.YTitleOpacity = 1.0
tube1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
tube1Display.DataAxesGrid.ZTitleFontFile = ''
tube1Display.DataAxesGrid.ZTitleBold = 0
tube1Display.DataAxesGrid.ZTitleItalic = 0
tube1Display.DataAxesGrid.ZTitleFontSize = 12
tube1Display.DataAxesGrid.ZTitleShadow = 0
tube1Display.DataAxesGrid.ZTitleOpacity = 1.0
tube1Display.DataAxesGrid.FacesToRender = 63
tube1Display.DataAxesGrid.CullBackface = 0
tube1Display.DataAxesGrid.CullFrontface = 1
tube1Display.DataAxesGrid.ShowGrid = 0
tube1Display.DataAxesGrid.ShowEdges = 1
tube1Display.DataAxesGrid.ShowTicks = 1
tube1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
tube1Display.DataAxesGrid.AxesToLabel = 63
tube1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
tube1Display.DataAxesGrid.XLabelFontFile = ''
tube1Display.DataAxesGrid.XLabelBold = 0
tube1Display.DataAxesGrid.XLabelItalic = 0
tube1Display.DataAxesGrid.XLabelFontSize = 12
tube1Display.DataAxesGrid.XLabelShadow = 0
tube1Display.DataAxesGrid.XLabelOpacity = 1.0
tube1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
tube1Display.DataAxesGrid.YLabelFontFile = ''
tube1Display.DataAxesGrid.YLabelBold = 0
tube1Display.DataAxesGrid.YLabelItalic = 0
tube1Display.DataAxesGrid.YLabelFontSize = 12
tube1Display.DataAxesGrid.YLabelShadow = 0
tube1Display.DataAxesGrid.YLabelOpacity = 1.0
tube1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
tube1Display.DataAxesGrid.ZLabelFontFile = ''
tube1Display.DataAxesGrid.ZLabelBold = 0
tube1Display.DataAxesGrid.ZLabelItalic = 0
tube1Display.DataAxesGrid.ZLabelFontSize = 12
tube1Display.DataAxesGrid.ZLabelShadow = 0
tube1Display.DataAxesGrid.ZLabelOpacity = 1.0
tube1Display.DataAxesGrid.XAxisNotation = 'Mixed'
tube1Display.DataAxesGrid.XAxisPrecision = 2
tube1Display.DataAxesGrid.XAxisUseCustomLabels = 0
tube1Display.DataAxesGrid.XAxisLabels = []
tube1Display.DataAxesGrid.YAxisNotation = 'Mixed'
tube1Display.DataAxesGrid.YAxisPrecision = 2
tube1Display.DataAxesGrid.YAxisUseCustomLabels = 0
tube1Display.DataAxesGrid.YAxisLabels = []
tube1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
tube1Display.DataAxesGrid.ZAxisPrecision = 2
tube1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
tube1Display.DataAxesGrid.ZAxisLabels = []
tube1Display.DataAxesGrid.UseCustomBounds = 0
tube1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display.PolarAxes.Visibility = 0
tube1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
tube1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
tube1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
tube1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
tube1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
tube1Display.PolarAxes.EnableCustomRange = 0
tube1Display.PolarAxes.CustomRange = [0.0, 1.0]
tube1Display.PolarAxes.PolarAxisVisibility = 1
tube1Display.PolarAxes.RadialAxesVisibility = 1
tube1Display.PolarAxes.DrawRadialGridlines = 1
tube1Display.PolarAxes.PolarArcsVisibility = 1
tube1Display.PolarAxes.DrawPolarArcsGridlines = 1
tube1Display.PolarAxes.NumberOfRadialAxes = 0
tube1Display.PolarAxes.AutoSubdividePolarAxis = 1
tube1Display.PolarAxes.NumberOfPolarAxis = 0
tube1Display.PolarAxes.MinimumRadius = 0.0
tube1Display.PolarAxes.MinimumAngle = 0.0
tube1Display.PolarAxes.MaximumAngle = 90.0
tube1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
tube1Display.PolarAxes.Ratio = 1.0
tube1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
tube1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
tube1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
tube1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
tube1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
tube1Display.PolarAxes.PolarAxisTitleVisibility = 1
tube1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
tube1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
tube1Display.PolarAxes.PolarLabelVisibility = 1
tube1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
tube1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
tube1Display.PolarAxes.RadialLabelVisibility = 1
tube1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
tube1Display.PolarAxes.RadialLabelLocation = 'Bottom'
tube1Display.PolarAxes.RadialUnitsVisibility = 1
tube1Display.PolarAxes.ScreenSize = 10.0
tube1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
tube1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
tube1Display.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display.PolarAxes.PolarAxisTitleBold = 0
tube1Display.PolarAxes.PolarAxisTitleItalic = 0
tube1Display.PolarAxes.PolarAxisTitleShadow = 0
tube1Display.PolarAxes.PolarAxisTitleFontSize = 12
tube1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
tube1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
tube1Display.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display.PolarAxes.PolarAxisLabelBold = 0
tube1Display.PolarAxes.PolarAxisLabelItalic = 0
tube1Display.PolarAxes.PolarAxisLabelShadow = 0
tube1Display.PolarAxes.PolarAxisLabelFontSize = 12
tube1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
tube1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
tube1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display.PolarAxes.LastRadialAxisTextBold = 0
tube1Display.PolarAxes.LastRadialAxisTextItalic = 0
tube1Display.PolarAxes.LastRadialAxisTextShadow = 0
tube1Display.PolarAxes.LastRadialAxisTextFontSize = 12
tube1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
tube1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
tube1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
tube1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
tube1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
tube1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
tube1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
tube1Display.PolarAxes.EnableDistanceLOD = 1
tube1Display.PolarAxes.DistanceLODThreshold = 0.7
tube1Display.PolarAxes.EnableViewAngleLOD = 1
tube1Display.PolarAxes.ViewAngleLODThreshold = 0.7
tube1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
tube1Display.PolarAxes.PolarTicksVisibility = 1
tube1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
tube1Display.PolarAxes.TickLocation = 'Both'
tube1Display.PolarAxes.AxisTickVisibility = 1
tube1Display.PolarAxes.AxisMinorTickVisibility = 0
tube1Display.PolarAxes.ArcTickVisibility = 1
tube1Display.PolarAxes.ArcMinorTickVisibility = 0
tube1Display.PolarAxes.DeltaAngleMajor = 10.0
tube1Display.PolarAxes.DeltaAngleMinor = 5.0
tube1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
tube1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
tube1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
tube1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
tube1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
tube1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
tube1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
tube1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
tube1Display.PolarAxes.ArcMajorTickSize = 0.0
tube1Display.PolarAxes.ArcTickRatioSize = 0.3
tube1Display.PolarAxes.ArcMajorTickThickness = 1.0
tube1Display.PolarAxes.ArcTickRatioThickness = 0.5
tube1Display.PolarAxes.Use2DMode = 0
tube1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(streamTracer1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'l', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'l'
lLUT = GetColorTransferFunction('l')
lLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
lLUT.InterpretValuesAsCategories = 0
lLUT.AnnotationsInitialized = 0
lLUT.ShowCategoricalColorsinDataRangeOnly = 0
lLUT.RescaleOnVisibilityChange = 0
lLUT.EnableOpacityMapping = 0
lLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.5877108876896935, 0.865003, 0.865003, 0.865003, 3.175421775379387, 0.705882, 0.0156863, 0.14902]
lLUT.UseLogScale = 0
lLUT.UseOpacityControlPointsFreehandDrawing = 0
lLUT.ShowDataHistogram = 0
lLUT.AutomaticDataHistogramComputation = 0
lLUT.DataHistogramNumberOfBins = 10
lLUT.ColorSpace = 'Diverging'
lLUT.UseBelowRangeColor = 0
lLUT.BelowRangeColor = [0.0, 0.0, 0.0]
lLUT.UseAboveRangeColor = 0
lLUT.AboveRangeColor = [0.5, 0.5, 0.5]
lLUT.NanColor = [1.0, 1.0, 0.0]
lLUT.NanOpacity = 1.0
lLUT.Discretize = 1
lLUT.NumberOfTableValues = 256
lLUT.ScalarRangeInitialized = 1.0
lLUT.HSVWrap = 0
lLUT.VectorComponent = 0
lLUT.VectorMode = 'Magnitude'
lLUT.AllowDuplicateScalars = 1
lLUT.Annotations = []
lLUT.ActiveAnnotatedValues = []
lLUT.IndexedColors = []
lLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'l'
lPWF = GetOpacityTransferFunction('l')
lPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.175421775379387, 1.0, 0.5, 0.0]
lPWF.AllowDuplicateScalars = 1
lPWF.UseLogScale = 0
lPWF.ScalarRangeInitialized = 1

# Properties modified on tube1Display.DataAxesGrid
tube1Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on tube1Display.DataAxesGrid
tube1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.XTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.XTitleBold = 1
tube1Display.DataAxesGrid.XTitleFontSize = 22
tube1Display.DataAxesGrid.YTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.YTitleBold = 1
tube1Display.DataAxesGrid.YTitleFontSize = 22
tube1Display.DataAxesGrid.ZTitleFontFamily = 'File'
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
tube1Display.DataAxesGrid.ZLabelFontSize = 18

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