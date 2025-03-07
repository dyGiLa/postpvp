# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XDMF Reader'
hdf5readerxmf2 = XDMFReader(registrationName='hdf5reader.xmf2', FileNames=['/scratch/project_2006478/dyGiLa-Langevin/thermal-bath-UniT-quench-II-7-C-d-2-C/dyGiLa-sim-data.cycle_000053/hdf5reader.xmf2'])
hdf5readerxmf2.PointArrayStatus = ['feDensity', 'gapA', 'u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33']
hdf5readerxmf2.CellArrayStatus = ['vtkGhostType']
hdf5readerxmf2.GridStatus = ['dyGiLa-sim-data', 'dyGiLa-sim-data[100]', 'dyGiLa-sim-data[101]', 'dyGiLa-sim-data[102]', 'dyGiLa-sim-data[103]', 'dyGiLa-sim-data[104]', 'dyGiLa-sim-data[105]', 'dyGiLa-sim-data[106]', 'dyGiLa-sim-data[107]', 'dyGiLa-sim-data[108]', 'dyGiLa-sim-data[109]', 'dyGiLa-sim-data[10]', 'dyGiLa-sim-data[110]', 'dyGiLa-sim-data[111]', 'dyGiLa-sim-data[112]', 'dyGiLa-sim-data[113]', 'dyGiLa-sim-data[114]', 'dyGiLa-sim-data[115]', 'dyGiLa-sim-data[116]', 'dyGiLa-sim-data[117]', 'dyGiLa-sim-data[118]', 'dyGiLa-sim-data[119]', 'dyGiLa-sim-data[11]', 'dyGiLa-sim-data[120]', 'dyGiLa-sim-data[121]', 'dyGiLa-sim-data[122]', 'dyGiLa-sim-data[123]', 'dyGiLa-sim-data[124]', 'dyGiLa-sim-data[125]', 'dyGiLa-sim-data[126]', 'dyGiLa-sim-data[127]', 'dyGiLa-sim-data[128]', 'dyGiLa-sim-data[129]', 'dyGiLa-sim-data[12]', 'dyGiLa-sim-data[130]', 'dyGiLa-sim-data[131]', 'dyGiLa-sim-data[132]', 'dyGiLa-sim-data[133]', 'dyGiLa-sim-data[134]', 'dyGiLa-sim-data[135]', 'dyGiLa-sim-data[136]', 'dyGiLa-sim-data[137]', 'dyGiLa-sim-data[138]', 'dyGiLa-sim-data[139]', 'dyGiLa-sim-data[13]', 'dyGiLa-sim-data[140]', 'dyGiLa-sim-data[141]', 'dyGiLa-sim-data[142]', 'dyGiLa-sim-data[143]', 'dyGiLa-sim-data[144]', 'dyGiLa-sim-data[145]', 'dyGiLa-sim-data[146]', 'dyGiLa-sim-data[147]', 'dyGiLa-sim-data[148]', 'dyGiLa-sim-data[149]', 'dyGiLa-sim-data[14]', 'dyGiLa-sim-data[150]', 'dyGiLa-sim-data[151]', 'dyGiLa-sim-data[152]', 'dyGiLa-sim-data[153]', 'dyGiLa-sim-data[154]', 'dyGiLa-sim-data[155]', 'dyGiLa-sim-data[156]', 'dyGiLa-sim-data[157]', 'dyGiLa-sim-data[158]', 'dyGiLa-sim-data[159]', 'dyGiLa-sim-data[15]', 'dyGiLa-sim-data[160]', 'dyGiLa-sim-data[161]', 'dyGiLa-sim-data[162]', 'dyGiLa-sim-data[163]', 'dyGiLa-sim-data[164]', 'dyGiLa-sim-data[165]', 'dyGiLa-sim-data[166]', 'dyGiLa-sim-data[167]', 'dyGiLa-sim-data[168]', 'dyGiLa-sim-data[169]', 'dyGiLa-sim-data[16]', 'dyGiLa-sim-data[170]', 'dyGiLa-sim-data[171]', 'dyGiLa-sim-data[172]', 'dyGiLa-sim-data[173]', 'dyGiLa-sim-data[174]', 'dyGiLa-sim-data[175]', 'dyGiLa-sim-data[176]', 'dyGiLa-sim-data[177]', 'dyGiLa-sim-data[178]', 'dyGiLa-sim-data[179]', 'dyGiLa-sim-data[17]', 'dyGiLa-sim-data[180]', 'dyGiLa-sim-data[181]', 'dyGiLa-sim-data[182]', 'dyGiLa-sim-data[183]', 'dyGiLa-sim-data[184]', 'dyGiLa-sim-data[185]', 'dyGiLa-sim-data[186]', 'dyGiLa-sim-data[187]', 'dyGiLa-sim-data[188]', 'dyGiLa-sim-data[189]', 'dyGiLa-sim-data[18]', 'dyGiLa-sim-data[190]', 'dyGiLa-sim-data[191]', 'dyGiLa-sim-data[192]', 'dyGiLa-sim-data[193]', 'dyGiLa-sim-data[194]', 'dyGiLa-sim-data[195]', 'dyGiLa-sim-data[196]', 'dyGiLa-sim-data[197]', 'dyGiLa-sim-data[198]', 'dyGiLa-sim-data[199]', 'dyGiLa-sim-data[19]', 'dyGiLa-sim-data[1]', 'dyGiLa-sim-data[200]', 'dyGiLa-sim-data[201]', 'dyGiLa-sim-data[202]', 'dyGiLa-sim-data[203]', 'dyGiLa-sim-data[204]', 'dyGiLa-sim-data[205]', 'dyGiLa-sim-data[206]', 'dyGiLa-sim-data[207]', 'dyGiLa-sim-data[208]', 'dyGiLa-sim-data[209]', 'dyGiLa-sim-data[20]', 'dyGiLa-sim-data[210]', 'dyGiLa-sim-data[211]', 'dyGiLa-sim-data[212]', 'dyGiLa-sim-data[213]', 'dyGiLa-sim-data[214]', 'dyGiLa-sim-data[215]', 'dyGiLa-sim-data[216]', 'dyGiLa-sim-data[217]', 'dyGiLa-sim-data[218]', 'dyGiLa-sim-data[219]', 'dyGiLa-sim-data[21]', 'dyGiLa-sim-data[220]', 'dyGiLa-sim-data[221]', 'dyGiLa-sim-data[222]', 'dyGiLa-sim-data[223]', 'dyGiLa-sim-data[224]', 'dyGiLa-sim-data[225]', 'dyGiLa-sim-data[226]', 'dyGiLa-sim-data[227]', 'dyGiLa-sim-data[228]', 'dyGiLa-sim-data[229]', 'dyGiLa-sim-data[22]', 'dyGiLa-sim-data[230]', 'dyGiLa-sim-data[231]', 'dyGiLa-sim-data[232]', 'dyGiLa-sim-data[233]', 'dyGiLa-sim-data[234]', 'dyGiLa-sim-data[235]', 'dyGiLa-sim-data[236]', 'dyGiLa-sim-data[237]', 'dyGiLa-sim-data[238]', 'dyGiLa-sim-data[239]', 'dyGiLa-sim-data[23]', 'dyGiLa-sim-data[240]', 'dyGiLa-sim-data[241]', 'dyGiLa-sim-data[242]', 'dyGiLa-sim-data[243]', 'dyGiLa-sim-data[244]', 'dyGiLa-sim-data[245]', 'dyGiLa-sim-data[246]', 'dyGiLa-sim-data[247]', 'dyGiLa-sim-data[248]', 'dyGiLa-sim-data[249]', 'dyGiLa-sim-data[24]', 'dyGiLa-sim-data[250]', 'dyGiLa-sim-data[251]', 'dyGiLa-sim-data[252]', 'dyGiLa-sim-data[253]', 'dyGiLa-sim-data[254]', 'dyGiLa-sim-data[255]', 'dyGiLa-sim-data[25]', 'dyGiLa-sim-data[26]', 'dyGiLa-sim-data[27]', 'dyGiLa-sim-data[28]', 'dyGiLa-sim-data[29]', 'dyGiLa-sim-data[2]', 'dyGiLa-sim-data[30]', 'dyGiLa-sim-data[31]', 'dyGiLa-sim-data[32]', 'dyGiLa-sim-data[33]', 'dyGiLa-sim-data[34]', 'dyGiLa-sim-data[35]', 'dyGiLa-sim-data[36]', 'dyGiLa-sim-data[37]', 'dyGiLa-sim-data[38]', 'dyGiLa-sim-data[39]', 'dyGiLa-sim-data[3]', 'dyGiLa-sim-data[40]', 'dyGiLa-sim-data[41]', 'dyGiLa-sim-data[42]', 'dyGiLa-sim-data[43]', 'dyGiLa-sim-data[44]', 'dyGiLa-sim-data[45]', 'dyGiLa-sim-data[46]', 'dyGiLa-sim-data[47]', 'dyGiLa-sim-data[48]', 'dyGiLa-sim-data[49]', 'dyGiLa-sim-data[4]', 'dyGiLa-sim-data[50]', 'dyGiLa-sim-data[51]', 'dyGiLa-sim-data[52]', 'dyGiLa-sim-data[53]', 'dyGiLa-sim-data[54]', 'dyGiLa-sim-data[55]', 'dyGiLa-sim-data[56]', 'dyGiLa-sim-data[57]', 'dyGiLa-sim-data[58]', 'dyGiLa-sim-data[59]', 'dyGiLa-sim-data[5]', 'dyGiLa-sim-data[60]', 'dyGiLa-sim-data[61]', 'dyGiLa-sim-data[62]', 'dyGiLa-sim-data[63]', 'dyGiLa-sim-data[64]', 'dyGiLa-sim-data[65]', 'dyGiLa-sim-data[66]', 'dyGiLa-sim-data[67]', 'dyGiLa-sim-data[68]', 'dyGiLa-sim-data[69]', 'dyGiLa-sim-data[6]', 'dyGiLa-sim-data[70]', 'dyGiLa-sim-data[71]', 'dyGiLa-sim-data[72]', 'dyGiLa-sim-data[73]', 'dyGiLa-sim-data[74]', 'dyGiLa-sim-data[75]', 'dyGiLa-sim-data[76]', 'dyGiLa-sim-data[77]', 'dyGiLa-sim-data[78]', 'dyGiLa-sim-data[79]', 'dyGiLa-sim-data[7]', 'dyGiLa-sim-data[80]', 'dyGiLa-sim-data[81]', 'dyGiLa-sim-data[82]', 'dyGiLa-sim-data[83]', 'dyGiLa-sim-data[84]', 'dyGiLa-sim-data[85]', 'dyGiLa-sim-data[86]', 'dyGiLa-sim-data[87]', 'dyGiLa-sim-data[88]', 'dyGiLa-sim-data[89]', 'dyGiLa-sim-data[8]', 'dyGiLa-sim-data[90]', 'dyGiLa-sim-data[91]', 'dyGiLa-sim-data[92]', 'dyGiLa-sim-data[93]', 'dyGiLa-sim-data[94]', 'dyGiLa-sim-data[95]', 'dyGiLa-sim-data[96]', 'dyGiLa-sim-data[97]', 'dyGiLa-sim-data[98]', 'dyGiLa-sim-data[99]', 'dyGiLa-sim-data[9]']

# Properties modified on hdf5readerxmf2
hdf5readerxmf2.PointArrayStatus = ['u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33']
hdf5readerxmf2.CellArrayStatus = []

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
hdf5readerxmf2Display = Show(hdf5readerxmf2, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
hdf5readerxmf2Display.Representation = 'Outline'
hdf5readerxmf2Display.ColorArrayName = ['POINTS', '']
hdf5readerxmf2Display.SelectTCoordArray = 'None'
hdf5readerxmf2Display.SelectNormalArray = 'None'
hdf5readerxmf2Display.SelectTangentArray = 'None'
hdf5readerxmf2Display.OSPRayScaleArray = 'u11'
hdf5readerxmf2Display.OSPRayScaleFunction = 'PiecewiseFunction'
hdf5readerxmf2Display.SelectOrientationVectors = 'None'
hdf5readerxmf2Display.ScaleFactor = 25.650000000000002
hdf5readerxmf2Display.SelectScaleArray = 'u11'
hdf5readerxmf2Display.GlyphType = 'Arrow'
hdf5readerxmf2Display.GlyphTableIndexArray = 'u11'
hdf5readerxmf2Display.GaussianRadius = 1.2825
hdf5readerxmf2Display.SetScaleArray = ['POINTS', 'u11']
hdf5readerxmf2Display.ScaleTransferFunction = 'PiecewiseFunction'
hdf5readerxmf2Display.OpacityArray = ['POINTS', 'u11']
hdf5readerxmf2Display.OpacityTransferFunction = 'PiecewiseFunction'
hdf5readerxmf2Display.DataAxesGrid = 'GridAxesRepresentation'
hdf5readerxmf2Display.PolarAxes = 'PolarAxesRepresentation'
hdf5readerxmf2Display.ScalarOpacityUnitDistance = 0.954747237136223
hdf5readerxmf2Display.OpacityArrayName = ['POINTS', 'u11']
hdf5readerxmf2Display.IsosurfaceValues = [-0.009296774864196777]
hdf5readerxmf2Display.SliceFunction = 'Plane'
hdf5readerxmf2Display.Slice = 16

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
hdf5readerxmf2Display.ScaleTransferFunction.Points = [-2.3707852363586426, 0.0, 0.5, 0.0, 2.352191686630249, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
hdf5readerxmf2Display.OpacityTransferFunction.Points = [-2.3707852363586426, 0.0, 0.5, 0.0, 2.352191686630249, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
hdf5readerxmf2Display.SliceFunction.Origin = [63.75, 127.75, 63.75]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(hdf5readerxmf2Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
hdf5readerxmf2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=hdf5readerxmf2)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'gap'
calculator1.Function = 'sqrt(u11^2+u12^2+u13^2+u21^2+u22^2+u23^2+u31^2+u32^2+u33^2+v11^2+v12^2+v13^2+v21^2+v22^2+v23^2+v31^2+v32^2+v33^2)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Outline'
calculator1Display.ColorArrayName = ['POINTS', '']
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'gap'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 25.650000000000002
calculator1Display.SelectScaleArray = 'gap'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'gap'
calculator1Display.GaussianRadius = 1.2825
calculator1Display.SetScaleArray = ['POINTS', 'gap']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'gap']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 0.954747237136223
calculator1Display.OpacityArrayName = ['POINTS', 'gap']
calculator1Display.IsosurfaceValues = [1.719412204587161]
calculator1Display.SliceFunction = 'Plane'
calculator1Display.Slice = 16

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
calculator1Display.SliceFunction.Origin = [63.75, 127.75, 63.75]

# hide data in view
Hide(hdf5readerxmf2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(calculator1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(calculator1Display, ('POINTS', 'gap'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
calculator1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'gap'
gapLUT = GetColorTransferFunction('gap')
gapLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.719412204587161, 0.865003, 0.865003, 0.865003, 3.438824409174322, 0.705882, 0.0156863, 0.14902]
gapLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'gap'
gapPWF = GetOpacityTransferFunction('gap')
gapPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]
gapPWF.ScalarRangeInitialized = 1

# change representation type
calculator1Display.SetRepresentationType('Surface')

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=calculator1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [63.75, 127.75, 63.75]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [63.75, 127.75, 63.75]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [5.0, 127.75, 63.75]
slice1.SliceType.Normal = [-1.0, 0.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'gap']
slice1Display.LookupTable = gapLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'gap'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 25.650000000000002
slice1Display.SelectScaleArray = 'gap'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'gap'
slice1Display.GaussianRadius = 1.2825
slice1Display.SetScaleArray = ['POINTS', 'gap']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'gap']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.421997220690779, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.421997220690779, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(calculator1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=calculator1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=calculator1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=calculator1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=calculator1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# hide data in view
Hide(slice1, renderView1)

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UniformGridRepresentation')

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# destroy slice1
Delete(slice1)
del slice1

# Properties modified on calculator1Display.DataAxesGrid
calculator1Display.DataAxesGrid.GridAxesVisibility = 1

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=calculator1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'gap']
clip1.Value = 1.719412204587161

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [63.75, 127.75, 63.75]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [63.75, 127.75, 63.75]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [5.0, 127.75, 63.75]
clip1.ClipType.Normal = [-1.0, 0.0, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

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
clip1Display.ScaleFactor = 25.650000000000002
clip1Display.SelectScaleArray = 'gap'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'gap'
clip1Display.GaussianRadius = 1.2825
clip1Display.SetScaleArray = ['POINTS', 'gap']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'gap']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = gapPWF
clip1Display.ScalarOpacityUnitDistance = 0.9618011216937712
clip1Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=clip1)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'gap']
clip2.Value = 1.719412204587161

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [66.5, 127.75, 63.75]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [66.5, 127.75, 63.75]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [123.0, 127.75, 63.75]

# show data in view
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', 'gap']
clip2Display.LookupTable = gapLUT
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'None'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleArray = 'gap'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 25.650000000000002
clip2Display.SelectScaleArray = 'gap'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'gap'
clip2Display.GaussianRadius = 1.2825
clip2Display.SetScaleArray = ['POINTS', 'gap']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'gap']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = gapPWF
clip2Display.ScalarOpacityUnitDistance = 0.9689844349108222
clip2Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=clip2)
clip3.ClipType = 'Plane'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['POINTS', 'gap']
clip3.Value = 1.719412204587161

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [64.0, 127.75, 63.75]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [64.0, 127.75, 63.75]

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [64.0, 127.75, 5.0]
clip3.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.ColorArrayName = ['POINTS', 'gap']
clip3Display.LookupTable = gapLUT
clip3Display.SelectTCoordArray = 'None'
clip3Display.SelectNormalArray = 'None'
clip3Display.SelectTangentArray = 'None'
clip3Display.OSPRayScaleArray = 'gap'
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.ScaleFactor = 25.650000000000002
clip3Display.SelectScaleArray = 'gap'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'gap'
clip3Display.GaussianRadius = 1.2825
clip3Display.SetScaleArray = ['POINTS', 'gap']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = ['POINTS', 'gap']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityFunction = gapPWF
clip3Display.ScalarOpacityUnitDistance = 0.975739464911818
clip3Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip2, renderView1)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip4 = Clip(registrationName='Clip4', Input=clip3)
clip4.ClipType = 'Plane'
clip4.HyperTreeGridClipper = 'Plane'
clip4.Scalars = ['POINTS', 'gap']
clip4.Value = 1.719412204587161

# init the 'Plane' selected for 'ClipType'
clip4.ClipType.Origin = [64.0, 127.75, 66.5]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip4.HyperTreeGridClipper.Origin = [64.0, 127.75, 66.5]

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [64.0, 127.75, 123.0]
clip4.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip4Display = Show(clip4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip4Display.Representation = 'Surface'
clip4Display.ColorArrayName = ['POINTS', 'gap']
clip4Display.LookupTable = gapLUT
clip4Display.SelectTCoordArray = 'None'
clip4Display.SelectNormalArray = 'None'
clip4Display.SelectTangentArray = 'None'
clip4Display.OSPRayScaleArray = 'gap'
clip4Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip4Display.SelectOrientationVectors = 'None'
clip4Display.ScaleFactor = 25.650000000000002
clip4Display.SelectScaleArray = 'gap'
clip4Display.GlyphType = 'Arrow'
clip4Display.GlyphTableIndexArray = 'gap'
clip4Display.GaussianRadius = 1.2825
clip4Display.SetScaleArray = ['POINTS', 'gap']
clip4Display.ScaleTransferFunction = 'PiecewiseFunction'
clip4Display.OpacityArray = ['POINTS', 'gap']
clip4Display.OpacityTransferFunction = 'PiecewiseFunction'
clip4Display.DataAxesGrid = 'GridAxesRepresentation'
clip4Display.PolarAxes = 'PolarAxesRepresentation'
clip4Display.ScalarOpacityFunction = gapPWF
clip4Display.ScalarOpacityUnitDistance = 0.9826422717048692
clip4Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip3, renderView1)

# show color bar/color legend
clip4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip5 = Clip(registrationName='Clip5', Input=clip4)
clip5.ClipType = 'Plane'
clip5.HyperTreeGridClipper = 'Plane'
clip5.Scalars = ['POINTS', 'gap']
clip5.Value = 1.719412204587161

# init the 'Plane' selected for 'ClipType'
clip5.ClipType.Origin = [64.0, 127.75, 64.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip5.HyperTreeGridClipper.Origin = [64.0, 127.75, 64.0]

# Properties modified on clip5.ClipType
clip5.ClipType.Normal = [-1.0, 0.0, 1.0]

# show data in view
clip5Display = Show(clip5, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip5Display.Representation = 'Surface'
clip5Display.ColorArrayName = ['POINTS', 'gap']
clip5Display.LookupTable = gapLUT
clip5Display.SelectTCoordArray = 'None'
clip5Display.SelectNormalArray = 'None'
clip5Display.SelectTangentArray = 'None'
clip5Display.OSPRayScaleArray = 'gap'
clip5Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip5Display.SelectOrientationVectors = 'None'
clip5Display.ScaleFactor = 25.650000000000002
clip5Display.SelectScaleArray = 'gap'
clip5Display.GlyphType = 'Arrow'
clip5Display.GlyphTableIndexArray = 'gap'
clip5Display.GaussianRadius = 1.2825
clip5Display.SetScaleArray = ['POINTS', 'gap']
clip5Display.ScaleTransferFunction = 'PiecewiseFunction'
clip5Display.OpacityArray = ['POINTS', 'gap']
clip5Display.OpacityTransferFunction = 'PiecewiseFunction'
clip5Display.DataAxesGrid = 'GridAxesRepresentation'
clip5Display.PolarAxes = 'PolarAxesRepresentation'
clip5Display.ScalarOpacityFunction = gapPWF
clip5Display.ScalarOpacityUnitDistance = 1.2328166547909185
clip5Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip5Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip5Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.438824409174322, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip4, renderView1)

# show color bar/color legend
clip5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on clip5Display.DataAxesGrid
clip5Display.DataAxesGrid.GridAxesVisibility = 1

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=clip5)
plotOverLine1.Point1 = [5.0, -0.5, 5.0]
plotOverLine1.Point2 = [123.0, 256.0, 123.0]

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [116.0, -0.5, 116.0]
plotOverLine1.Point2 = [116.0, 256.0, 116.0]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'gap']
plotOverLine1Display.LookupTable = gapLUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'gap'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 25.650000000000002
plotOverLine1Display.SelectScaleArray = 'gap'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'gap'
plotOverLine1Display.GaussianRadius = 1.2825
plotOverLine1Display.SetScaleArray = ['POINTS', 'gap']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'gap']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.3460673447422176, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.3460673447422176, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['gap', 'u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'u31', 'u32', 'u33', 'v11', 'v12', 'v13', 'v21', 'v22', 'v23', 'v31', 'v32', 'v33']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'gap', 'gap', 'u11', 'u11', 'u12', 'u12', 'u13', 'u13', 'u21', 'u21', 'u22', 'u22', 'u23', 'u23', 'u31', 'u31', 'u32', 'u32', 'u33', 'u33', 'v11', 'v11', 'v12', 'v12', 'v13', 'v13', 'v21', 'v21', 'v22', 'v22', 'v23', 'v23', 'v31', 'v31', 'v32', 'v32', 'v33', 'v33', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'gap', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u11', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u12', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u13', '0.6', '0.3100022888532845', '0.6399938963912413', 'u21', '1', '0.5000076295109483', '0', 'u22', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u23', '0', '0', '0', 'u31', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u32', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u33', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'v11', '0.6', '0.3100022888532845', '0.6399938963912413', 'v12', '1', '0.5000076295109483', '0', 'v13', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'v21', '0', '0', '0', 'v22', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'v23', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'v31', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'v32', '0.6', '0.3100022888532845', '0.6399938963912413', 'v33', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'gap', '0', 'u11', '0', 'u12', '0', 'u13', '0', 'u21', '0', 'u22', '0', 'u23', '0', 'u31', '0', 'u32', '0', 'u33', '0', 'v11', '0', 'v12', '0', 'v13', '0', 'v21', '0', 'v22', '0', 'v23', '0', 'v31', '0', 'v32', '0', 'v33', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'gap', '1', 'u11', '1', 'u12', '1', 'u13', '1', 'u21', '1', 'u22', '1', 'u23', '1', 'u31', '1', 'u32', '1', 'u33', '1', 'v11', '1', 'v12', '1', 'v13', '1', 'v21', '1', 'v22', '1', 'v23', '1', 'v31', '1', 'v32', '1', 'v33', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'gap', '2', 'u11', '2', 'u12', '2', 'u13', '2', 'u21', '2', 'u22', '2', 'u23', '2', 'u31', '2', 'u32', '2', 'u33', '2', 'v11', '2', 'v12', '2', 'v13', '2', 'v21', '2', 'v22', '2', 'v23', '2', 'v31', '2', 'v32', '2', 'v33', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'gap', '0', 'u11', '0', 'u12', '0', 'u13', '0', 'u21', '0', 'u22', '0', 'u23', '0', 'u31', '0', 'u32', '0', 'u33', '0', 'v11', '0', 'v12', '0', 'v13', '0', 'v21', '0', 'v22', '0', 'v23', '0', 'v31', '0', 'v32', '0', 'v33', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'gap', '4', 'u11', '4', 'u12', '4', 'u13', '4', 'u21', '4', 'u22', '4', 'u23', '4', 'u31', '4', 'u32', '4', 'u33', '4', 'v11', '4', 'v12', '4', 'v13', '4', 'v21', '4', 'v22', '4', 'v23', '4', 'v31', '4', 'v32', '4', 'v33', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'gap', '0', 'u11', '0', 'u12', '0', 'u13', '0', 'u21', '0', 'u22', '0', 'u23', '0', 'u31', '0', 'u32', '0', 'u33', '0', 'v11', '0', 'v12', '0', 'v13', '0', 'v21', '0', 'v22', '0', 'v23', '0', 'v31', '0', 'v32', '0', 'v33', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'gap', '1', 'u11', '1', 'u12', '1', 'u13', '1', 'u21', '1', 'u22', '1', 'u23', '1', 'u31', '1', 'u32', '1', 'u33', '1', 'v11', '1', 'v12', '1', 'v13', '1', 'v21', '1', 'v22', '1', 'v23', '1', 'v31', '1', 'v32', '1', 'v33', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'gap', '2', 'u11', '2', 'u12', '2', 'u13', '2', 'u21', '2', 'u22', '2', 'u23', '2', 'u31', '2', 'u32', '2', 'u33', '2', 'v11', '2', 'v12', '2', 'v13', '2', 'v21', '2', 'v22', '2', 'v23', '2', 'v31', '2', 'v32', '2', 'v33', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'gap', '0', 'u11', '0', 'u12', '0', 'u13', '0', 'u21', '0', 'u22', '0', 'u23', '0', 'u31', '0', 'u32', '0', 'u33', '0', 'v11', '0', 'v12', '0', 'v13', '0', 'v21', '0', 'v22', '0', 'v23', '0', 'v31', '0', 'v32', '0', 'v33', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'gap', '4', 'u11', '4', 'u12', '4', 'u13', '4', 'u21', '4', 'u22', '4', 'u23', '4', 'u31', '4', 'u32', '4', 'u33', '4', 'v11', '4', 'v12', '4', 'v13', '4', 'v21', '4', 'v22', '4', 'v23', '4', 'v31', '4', 'v32', '4', 'v33', '4', 'vtkValidPointMask', '4']

# set active view
SetActiveView(renderView1)

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [116.0, 10.0, 116.0]
plotOverLine1.Point2 = [116.0, 240, 116.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# set active view
SetActiveView(lineChartView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1940, 874)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-133.65407942901476, 209.68517522056828, 421.34750361980866]
renderView1.CameraFocalPoint = [64.69776489551631, 127.74999713897706, 63.30223510448368]
renderView1.CameraViewUp = [-0.09791419070158078, 0.9569519270637041, -0.27323217334039873]
renderView1.CameraParallelScale = 191.4003708062851

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
