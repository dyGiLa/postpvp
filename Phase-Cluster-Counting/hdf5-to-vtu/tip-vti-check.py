import vtk

reader = vtk.vtkXMLImageDataReader()
reader.SetFileName("domain_000000.vti")
reader.Update()

image = reader.GetOutput()
gapA = image.GetPointData().GetArray("gapA")

print("GapA array size:", gapA.GetNumberOfTuples(), "components:", gapA.GetNumberOfComponents())
