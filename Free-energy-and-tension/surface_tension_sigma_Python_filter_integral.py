import numpy as np
from vtkmodules.util import numpy_support as ns

# Input dataset: polyline glyphs with sampled f_v
# Polygon Mesh pipeline object should be clicked first, 
# then resampled cells polylines should be clicked 2nd.
# this can match following code
input0 = self.GetInputDataObject(0, 1)
polygon_surface = self.GetInputDataObject(0, 0)  # Input 1 is surface mesh

output = self.GetOutput()

# Copy the geometry and topology
# output.ShallowCopy(input0)

# now output is the surface, this makes integrated value can attach to poly mesh surface
output.ShallowCopy(polygon_surface)  

# Get point data array f_v
PData = input0.GetPointData()
fv_array = PData.GetArray("f_GL_nfB")

if fv_array is None:
    raise RuntimeError("No array named 'f_xxx' found in point data")

# vtk to np.array
fv_np = ns.vtk_to_numpy(fv_array)

# Prepare output array: one value per polyline (cell)
n_cells = input0.GetNumberOfCells()
fs_np = np.zeros(n_cells, dtype=np.float32)
polylineLen_np = np.zeros(n_cells, dtype=np.float32)

for i in range(n_cells):
    cell = input0.GetCell(i)
    pts_id = cell.GetPointIds()
    n_pts = pts_id.GetNumberOfIds()

    # Compute arc length along line
    arc_len = 0.0
    integral = 0.0
#    for j in range(n_pts - 1):
#        p0 = np.array(input0.GetPoint(pts_id.GetId(j)))
#        p1 = np.array(input0.GetPoint(pts_id.GetId(j+1)))
#        ds = np.linalg.norm(p1 - p0)
#        fval = fv_np[pts_id.GetId(j)]
#        integral += fval * ds
#        arc_len += ds
    # Add last point? optional: use trapezoid rule
    #f_last = fv_np[pts_id.GetId(n_pts-1)]
    #integral += 0.5 * f_last * ds  # simple trapezoid for last segment
    
    for j in range(n_pts - 1):
        p0 = np.array(input0.GetPoint(pts_id.GetId(j)))
        p1 = np.array(input0.GetPoint(pts_id.GetId(j+1)))
        ds = np.linalg.norm(p1 - p0)

        f0 = fv_np[pts_id.GetId(j)]
        f1 = fv_np[pts_id.GetId(j+1)]

        integral += 0.5 * (f0 + f1) * ds

    fs_np[i] = integral
    polylineLen_np[i] = arc_len

# Convert to VTK array and add to output PointData
fs_vtkPoint = ns.numpy_to_vtk(fs_np, deep=True)
fs_vtkPoint.SetName("fs_TensionPoint")  # choose a name you like
output.GetPointData().AddArray(fs_vtkPoint)