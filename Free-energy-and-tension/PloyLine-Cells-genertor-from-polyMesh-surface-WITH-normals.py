import vtk
import numpy as np

# This script is for programmble filter, which
# generates polyline cells along normal vectors
# of ploygon mesh surface. This surface is created by 
# a python script, which uses trimesh + open3D to smoothen 
# croud surfaces of Unstructured Grid (through Extract Surface in ParaView).
# the smoothen polygon mesh is saved as *.ply, but can be saved to vtk(pvd)
# file after necessary clipsin paraview.

# Input has to be polygon mesh surface
PolyMesh_surface = self.GetInput()
output = self.GetPolyDataOutput()

# ploy line cell length L
# Number of points N on polyline cell
L = 10.0
N = 91 # N should be odd number to make p0 on surface

# Access Normals array of PolyMesh data
normals = PolyMesh_surface.GetPointData().GetArray("Normals")

# allocate points and Cell Array for saving + passing output
pts = vtk.vtkPoints()
poly_lines = vtk.vtkCellArray()

# initialize cell counter
pt_counter = 0

for i in range(PolyMesh_surface.GetNumberOfPoints()):

    # access vertice of poly mesh
    p0 = np.array(PolyMesh_surface.GetPoint(i))
    # load normal vector at vortex i
    n = np.array(normals.GetTuple(i))

    # normalise n-vector
    norm = np.linalg.norm(n)
    if norm > 0:
        n /= norm

    # initialize vtk poly line; set segment number to N for line cell
    polyline = vtk.vtkPolyLine()
    polyline.GetPointIds().SetNumberOfIds(N)

    # loop over all segments in one cell
    for k in range(N):        
        # segment coordinate s;
        # L * k / (N - 1) is for one side polyline
        s = L * k / (N - 1)
        # s = L * (k/(N-1) - 0.5) is for polyline extends ot both side of surface;
        # s < 0 for k < 1/2 N-1
        
        # calculate p & add to segement
        p = p0 + s * n
        pts.InsertNextPoint(float(p[0]), float(p[1]), float(p[2]))

        # set segment point id & cell counter
        polyline.GetPointIds().SetId(k, pt_counter)

        pt_counter += 1
    # add polyline cell into cell array
    poly_lines.InsertNextCell(polyline)

output.SetPoints(pts)
output.SetLines(poly_lines)