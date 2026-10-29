from paraview.simple import *
from paraview import servermanager as sm
from vtk.numpy_interface import dataset_adapter as dsa
from vtkmodules.util import numpy_support

import os
import csv
import numpy as np
import pandas as pd
import vtk

# ============ settings: edit these ============
iso_gapA       = 'Contour1'        # gapA isosurface, with Normals; This picks bubble shell
GShape_ellipse = 'Ellipse1'        # Geometrical shape ellipse, providing start points for samping lines
pvtiDataSet_Amatrix = 'pio.pvti'      # Raw data of ReA, ImA, all its arrays get resampled

extra_behind = 25.0        # how far to go behind gapA bubble shell
Num_samp     = 300        # samples per line

# resampling csv files output pathes
output_dir   = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/RelaxingCriticalBubbleConf-p27-T0.9275-Aali-cycle_001116'
os.makedirs(output_dir, exist_ok=True)
# ==============================================

iso   = FindSource(iso_gapA)
shape = FindSource(GShape_ellipse)
AMatrix_Data = FindSource(pvtiDataSet_Amatrix)

# ---- 1. isosurface points and normals vector array ----
iso.UpdatePipeline()
iso_data = dsa.WrapDataObject(sm.Fetch(iso))
pts_iso = np.array(iso_data.Points)

Normal_iso = np.array(iso_data.PointData['Normals'])
Normal_iso /= np.linalg.norm(Normal_iso, axis=1)[:, None]

# ---- 2. gother start points from ellipse ----
shape.UpdatePipeline()
S_pts = np.array(dsa.WrapDataObject(sm.Fetch(shape)).Points)   # (n_lines, 3)
n_lines = len(S_pts)
print('ellipse min/max :', S_pts.min(axis=0), S_pts.max(axis=0))
print('gapA isosurf min/max :', pts_iso.min(axis=0), pts_iso.max(axis=0))

# ---- 3. normal veector of the nearest gapA isosurface point for each start point ----

# fetch isosurface points data into vtkpolydata object
polyData_ = vtk.vtkPolyData()
polyData_.SetPoints(vtk.vtkPoints())
polyData_.GetPoints().SetData(numpy_support.numpy_to_vtk(pts_iso, deep=True))

# fetch isosurface vtk point data into vtkLocator object
loc = vtk.vtkPointLocator()
loc.SetDataSet(polyData_)
loc.BuildLocator()

# find closest isosuf point for each S point,
# idx is array of idices of found pints in polyData packed pts_iso data
idx  = np.array([loc.FindClosestPoint(s) for s in S_pts])
Normals_Closest_arr    = Normal_iso[idx].copy()

# calculare distance between each group of closest isosurf pts and S_pts
dist = np.linalg.norm(pts_iso[idx] - S_pts, axis=1)   # start point -> isosurface

# Orient each line so it points toward the isosurface.
# for doing this, np.einsum multiply the two arrays element by element,
# then add up along j (x, y, z)
toward = np.einsum('ij,ij->i', pts_iso[idx] - S_pts, Normals_Closest_arr)
Normals_Closest_arr[toward < 0] *= -1

# ---- 4. build the sample points: S + t*N, t = 0 at the ellipse point ----
s_max = dist.max() + extra_behind
t = np.linspace(0.0, s_max, Num_samp)

# vectorized form of the formula S + t*N;
# None inside the brackets adds a new axis of length 1. It doesn’t change any numbers, only the shape:
# S_pts[:, None, :] turns (n_lines, 3) into (n_lines, 1, 3)
# Normals_Closest_arr[:, None, :] also becomes (n_lines, 1, 3)
# t[None, :, None] turns (n_samp,) into (1, n_samp, 1)

# When numpy combines two arrays, any axis of length 1 is stretched to match the other array. So:
# t[None, :, None] * Normals_Closest_arr[:, None, :] multiplies shapes (1, n_samp, 1) and (n_lines, 1, 3).
# Each axis is matched or stretched, giving (n_lines, n_samp, 3). Entry [i, j, :] equals t[j] * Normals[i],
# which is how far to walk times the direction of line i.
# Adding S_pts[:, None, :], shape (n_lines, 1, 3), stretches the start point along the sample axis.
# So entry [i, j, :] equals S_pts[i] + t[j] * Normals[i].
# point = start + t × direction
pts = S_pts[:, None, :] + t[None, :, None] * Normals_Closest_arr[:, None, :]   # (n_lines, n_samp, 3)

# ---- 5. Re-Sample on the all MPI ranks), fetch only the result ----
AMatrixRSPolyLine = PolyLineSource(registrationName='AMatrixSamplePolyline')
AMatrixRSPolyLine.Points = pts.reshape(-1).tolist()          # x0,y0,z0,x1,y1,z1,...
AMatrixRSPolyLine.UpdatePipeline()

ReSamp = ResampleWithDataset(registrationName='AMatrixSamplePolyline', SourceDataArrays=AMatrix_Data, DestinationMesh=AMatrixRSPolyLine)
ReSamp.UpdatePipeline()

out = sm.Fetch(ReSamp)
print('sampled points:', out.GetNumberOfPoints(), '| expected:', n_lines * Num_samp)

# ---- 6. collect everything into one table ----
ReSampOut = dsa.WrapDataObject(out)

line_id = np.repeat(np.arange(n_lines), Num_samp)

cols = {'line_id': line_id,
        't': np.tile(t, n_lines),
        'x': pts[..., 0].ravel(),
        'y': pts[..., 1].ravel(),
        'z': pts[..., 2].ravel()}
cols['signed_dist'] = cols['t'] - dist[line_id]   # 0 = isosurface crossing, isosurface is centerized

skip_item_list = {'vtkValidPointMask', 'vtkGhostType'}
for name in ReSampOut.PointData.keys():
    if name in skip_item_list:
        continue
    a = np.array(ReSampOut.PointData[name])
    if a.ndim == 1:
        cols[name] = a
    else:
        for i in range(a.shape[1]):
            cols[f'{name}_{i}'] = a[:, i]

df = pd.DataFrame(cols)
df['line_id'] = df['line_id'].astype(int)

# samples that fell outside the volume -> NaN in the data columns
valid = np.array(ReSampOut.PointData['vtkValidPointMask']).astype(bool)
geom_cols = ['line_id', 't', 'signed_dist', 'x', 'y', 'z']
data_cols = df.columns.difference(geom_cols)
df.loc[~valid, data_cols] = np.nan
if valid.sum() == 0:
    raise RuntimeError('No sample point is inside the volume - check the bounds printout above.')

# df.to_csv(out_csv, index=False)
print('lines:', n_lines, '| table:', df.shape, '| invalid samples:', (~valid).sum())

# ----  one CSV per line ----
# for i, g in df.groupby('line_id'):
#     g.to_csv(f'/home/heidi/Documents/B-phase-critical-Bubble/p27-T0.9275/pio/dyGiLa-sim-Amatrix.cycle_001116/line_{int(i):05d}.csv', index=False)
# for i, g in df.groupby('line_id'):
#     g.to_csv(os.path.join(output_dir, f'line_{int(i):05d}.csv'), index=False)
for i, g in df.groupby('line_id'):
    g.to_csv(os.path.join(output_dir, f'line_{int(i):05d}.csv'),
             index=False, quoting=csv.QUOTE_NONNUMERIC)
