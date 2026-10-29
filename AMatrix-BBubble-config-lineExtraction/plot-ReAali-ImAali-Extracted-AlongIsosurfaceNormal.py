import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

# ===================== edit these =====================
data_load_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble'
gapA_isoValue = 3.95        # the isovalue of your Contour1 (needed only if shift='auto')
# B-Bubble line profile data
# x    : column used as the x axis
# sign : +1 or -1, flips the direction of the axis
# shift: number subtracted from the coordinate before plotting,
#        or 'auto' = the position where gapA crosses gapA_iso (this becomes r = 0)
extra = {
    'Line-Data-x_axis-A_al_i-l_Vector-parallel-w-AB_Wall.csv': dict(x='Points:0', sign=+1, shift='auto', marker='o', ms=6, every=10, fc='gold', label=r'$\hat{\mathbf{l}} \perp \hat{\mathbf{n}}$'),
    'Line-Data-z_axis-A_al_i-l_Vector-perpendicular-w-AB_Wall.csv': dict(x='Points:2', sign=+1, shift='auto', marker='s', ms=6, every=10, fc='lightskyblue', label=r'$\hat{\mathbf{l}} \parallel \hat{\mathbf{n}}$'),
}
r_max = 25.0        # cutoff of plot where r <= r_max (None = no cutoff)

# ******************************************************

out_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/RelaxingCriticalBubbleConf-p27-T0.9275-Aali-cycle_001116'

xi0   = 1.0         # x axis = signed_dist / xi0. Keep 1.0 if your data are already in xi_GL^0
ylim  = (-0.5, 3)      # set to None for automatic y range
alpha = 1.0         # transparency of each curve (lower it if the plot is crowded)
LineWidth = 2.2
axisFontSize = 26

first_idx = 0       # first file to consider (0 = line_00000.csv)
last_idx  = 24      # last file to consider, inclusive (24 = line_00024.csv). Use None for "up to the end"
PlotStep = 5        # use every `step`-th file: 1 = all files, 2 = every 2nd, 3 = every 3rd, ...
# ======================================================

# ======================================================
#  AMatrix Bubble line extracted data plots
# ======================================================

all_files = sorted(glob.glob(os.path.join(out_dir, 'line_*.csv')))

if last_idx is None or last_idx >= len(all_files):
    last_idx = len(all_files) - 1          # clip to the real last file

subset = all_files[first_idx:last_idx + 1]  # pick out the range of csv
files  = subset[::PlotStep]                     # first of the range, then every `step`-th
if subset[-1] not in files:                 # always keep the last file of the range
    files.append(subset[-1])

print('found', len(all_files), 'files | range', first_idx, '-', last_idx,
      '| using', len(files))
print('using:', [os.path.basename(f) for f in files])
dfs = [pd.read_csv(f) for f in files]

comps  = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
cols_u = [f'u{c}' for c in comps if f'u{c}' in dfs[0].columns]
cols_v = [f'v{c}' for c in comps if f'v{c}' in dfs[0].columns]

def label(col):
    name = r'\mathrm{Re}A' if col[0] == 'u' else r'\mathrm{Im}A'
    return rf'${name}_{{{col[1:]}}}$'          # u12 -> $\mathrm{Re}A_{12}$

colors   = cm.tab10(range(len(comps)))          # one color per component pair
color_of = {c: colors[k] for k, c in enumerate(comps)}

fig, ax = plt.subplots(figsize=(8, 5.5))

for n, d in enumerate(dfs):
    x = d['signed_dist'] / xi0
    for col in cols_u:                          # ReA: solid
        ax.plot(x, d[col], color=color_of[col[1:]], ls='-', lw=LineWidth, alpha=alpha,
                label=label(col) if n == 0 else None)   # label only once per element
    for col in cols_v:                          # ImA: dashed
        ax.plot(x, d[col], color=color_of[col[1:]], ls='--', lw=LineWidth, alpha=alpha,
                label=label(col) if n == 0 else None)

ax.axvline(0, color='k', ls=':', lw=1)          # the isosurface position

# ======================================================
#  plot 3rd path loaded data
# ======================================================

# plot extra curves same ax from other csv files: all uxx (ReA) and vxx (ImA)
from matplotlib.lines import Line2D
import numpy as np

def crossing(coord, gap, level):
    """coordinate where gap first crosses `level` (linear interpolation)"""
    g = np.asarray(gap) - level
    k = np.where(g[:-1] * g[1:] < 0)[0]
    if len(k) == 0:
        raise ValueError('gapA never crosses the isovalue; check gapA_isoValue')
    k = k[0]
    return coord[k] + (coord[k+1] - coord[k]) * (0 - g[k]) / (g[k+1] - g[k])

proxy_handles = []
for fname, s in extra.items():
    e = pd.read_csv(os.path.join(data_load_dir, fname))
    if 'vtkValidPointMask' in e.columns:
        e = e[e['vtkValidPointMask'] == 1]          # drop points outside the volume

    coord = e[s['x']].to_numpy()
    shift = crossing(coord, e['gapA'], gapA_isoValue) if s['shift'] == 'auto' else s['shift']
    xe = s['sign'] * (coord - shift) / xi0
    if s['shift'] == 'auto':
        print(fname, ': isosurface crossing at', s['x'], '=', shift)

    keep = (xe <= r_max) if r_max is not None else np.ones(len(xe), dtype=bool)
    xk = xe[keep] # x values that are kept        

    for col in cols_u + cols_v:
        if col not in e.columns:
            continue
        c = color_of[col[1:]]
        filled = col[0] == 'u'                      # ReA: filled, ImA: hollow
#        ax.plot(xe, e[col], ls='none', color=c,
        ax.plot(xk, e[col].to_numpy()[keep], ls='none', color=c,
                marker=s['marker'], ms=s['ms'], markevery=s['every'],
#                markerfacecolor=c if filled else 'none',
                markerfacecolor=s['fc'] if filled else 'none',
                markeredgecolor=c, markeredgewidth=1.5, zorder=5)

#    proxy_handles.append(Line2D([], [], ls='none', color='k', marker=s['marker'],
#                                ms=s['ms'], markerfacecolor='none', label=s['label']))
    proxy_handles.append(Line2D([], [], ls='none', marker=s['marker'], ms=s['ms'] + 2,
                                markerfacecolor=s['fc'], markeredgecolor='k',
                                markeredgewidth=1.5, label=s['label']))

# ======================================================
#  plot property controling and setting
# ======================================================

ax.set_xlabel(r'$r/\xi^{0}_{\mathrm{GL}}$', fontsize=axisFontSize)
ax.set_ylabel(r'$ReA_{\alpha j},\,\,ImA_{\alpha j}$', fontsize=axisFontSize)
if ylim is not None:
    ax.set_ylim(ylim)
ax.tick_params(labelsize=18)
ax.grid(alpha=0.25)
ax.set_title(f'all {len(dfs)} lines', fontsize=12)

# ax.legend(ncol=3, fontsize=16, frameon=True, framealpha=0.85, loc='right')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles + proxy_handles, labels + [h.get_label() for h in proxy_handles],
          ncol=3, fontsize=16, frameon=True, framealpha=0.85, loc='right')

plt.tight_layout()
plt.show()
