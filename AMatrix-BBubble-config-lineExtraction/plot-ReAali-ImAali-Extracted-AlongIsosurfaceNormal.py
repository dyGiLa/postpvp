import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.lines import Line2D

# ===================== edit these =====================
RelaxingBubble_xyzAxis_PlotSwitch = 'OFF'
data_load_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble'
gapA_isoValue = 3.907 #4.0, 3.95, 3.905, 3.907  # the isovalue gapA, which is used by shift='auto' to locate the center of Wall)
PlotDataDensity = 10
# B-Bubble line profile data
# x    : column used as the x axis
# sign : +1 or -1, flips the direction of the axis
# shift: number subtracted from the coordinate before plotting,
#        or 'auto' = the position where gapA crosses gapA_iso (this becomes r = 0)
extra = {
    # 'Line-Data-x_axis-A_al_i-l_Vector-parallel-w-AB_Wall.csv': dict(x='Points:0', sign=+1, shift='auto', marker='o', ms=4, every=PlotDataDensity, fc='gold', label=r'$\hat{\mathbf{l}} \parallel \hat{\mathbf{n}}$')
    'Line-Data-z_axis-A_al_i-l_Vector-perpendicular-w-AB_Wall.csv': dict(x='Points:2', sign=+1, shift='auto', marker='s', ms=4, every=PlotDataDensity, fc='lightskyblue', label=r'$\hat{\mathbf{l}} \perp \hat{\mathbf{n}}$'),
}
r_max = 25.0        # cutoff of plot where r <= r_max (None = no cutoff)
gapA_color_line = 'k'          # sqrt(A†A) from the extra line data
gapA_color_mark = 'magenta'    # sqrt(A†A) from Mark's flat-wall data
gapA_color_bubble = 'teal'     # ||A|| from the line_xxxx (relaxing bubble) data

# ******************************************************
FlatABWalls_PlotSwitch = 'OFF'
Flat_ABWalls_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/flat-ABWall-Sol-Mark-27bar-0.4Tc/sph_sym_AB_bubble_sol_axis-{:}.csv'
# header='r,A11,A12,A13,A21,A22,A23,A31,A32,A33'

# axes_id    = [0, 1, 2]
axes_id    = [2]
axes_name  = {0: r'$\hat{\mathbf{l}} \parallel \hat{\mathbf{n}},R=\infty$', 1: 'flat wall, $y$', 2: r'$\hat{\mathbf{l}} \perp \hat{\mathbf{n}},R=\infty$'}

mark_markers = False # True for marker, False no marker
markers    = {0: '*', 1: 'P', 2: 'X'}   # star, filled plus, filled cross: all different from o and s

ms           = 16          # marker size
every        = 8          # draw a marker on every n-th point

# NEW: how Mark's r is shifted so that the isosurface (gapA = gapA_isoValue) sits at r = 0
mark_sign  = -1           # -1: x = -(r - r_cross); the outside of the wall is at negative x, like the line_xxxx data                          # +1: x = +(r - r_cross)
mark_cross = 'last'       # which gapA = isoValue crossing becomes 0: 'last' = outer side of the wall, 'first' = inner side

# ******************************************************
RelaxingBubble_ABWallEvolation_PlotSwitch = 'ON'
out_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/RelaxingCriticalBubbleConf-p27-T0.9275-Aali-cycle_001116'

xi0   = 1.0         # x axis = signed_dist / xi0. Keep 1.0 if your data are already in xi_GL^0
ylim  = (-0.5, 5.5)      # set to None for automatic y range
alpha = 1.0         # transparency of each curve (lower it if the plot is crowded)
LineWidth = 1.5
axisFontSize = 18

first_idx = 0       # first file to consider (0 = line_00000.csv)
last_idx  = 23      # last file to consider, inclusive (24 = line_00024.csv). Use None for "up to the end"
PlotStep = 12        # use every `step`-th file: 1 = all files, 2 = every 2nd, 3 = every 3rd, ...

bubble_marker = 's'                 # marker shape for the line_xxxx curves (square)
bubble_ms     = 4                   # marker size
bubble_every  = 5                  # a marker on every n-th point of each curve
bubble_fc     = 'lightskyblue'      # fill color of the squares
bubble_label  = r'$\hat{\mathbf{l}} \parallel \hat{\mathbf{n}}$'   # legend text for this data set; edit freely, LaTeX works
# bubble_label  = ''   # legend text for this data set; edit freely, LaTeX works

bubble_shift = 'auto'     # 'auto': r = 0 where ||A|| crosses gapA_isoValue; 'none': keep signed_dist as saved
bubble_cross = 'first'    # which crossing is 0: 'first' = outer face of the wall (the lines come in from outside)

# *******************************************************
# plot configuration
fig_size  = (8, 5.5)     # figure size in inches (width, height)
fig_dpi   = 300          # resolution of the saved file
save_path = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/BBubble-EvolveExtraction-lPerpTOParallelwWall-FlatWall-config-27bar-T0.4Tc.png'   # .png, .pdf or .svg; None = do not save

# plot box position inside the figure, as fractions of the figure (0 to 1)
box_left, box_right, box_bottom, box_top = 0.15, 0.97, 0.15, 0.98
# box_left, box_right, box_bottom, box_top = 0.15, 0.97, 0.05, 0.80


# ======================================================

# =====================================================
#  plot enviriment
# =====================================================
fig, ax = plt.subplots(figsize=fig_size)

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

print('found', len(all_files), 'files | range', first_idx, '-', last_idx, '| using', len(files))
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

# legend entries for ReA (solid) / ImA (dashed): independent of every PlotSwitch
comp_handles = (
    [Line2D([], [], color=color_of[c], ls='-',  lw=LineWidth, label=rf'$\mathrm{{Re}}A_{{{c}}}$') for c in comps] +
    [Line2D([], [], color=color_of[c], ls='--', lw=LineWidth, label=rf'$\mathrm{{Im}}A_{{{c}}}$') for c in comps]
)

# defaults, so the legend works even when a PlotSwitch is OFF
proxy_handles = []
file_handles  = []
gapA_handles  = []
bubble_handles = []

def crossing(coord, gap, level, which='first'):
    """coordinate where gap crosses `level` (linear interpolation); first or last crossing"""
    g = np.asarray(gap) - level
    k = np.where(g[:-1] * g[1:] < 0)[0]
    if len(k) == 0:
        raise ValueError('gapA never crosses the isovalue; check gapA_isoValue')
    k = k[0] if which == 'first' else k[-1]
    return coord[k] + (coord[k+1] - coord[k]) * (0 - g[k]) / (g[k+1] - g[k])


if RelaxingBubble_ABWallEvolation_PlotSwitch == 'ON':
    for n, d in enumerate(dfs):
        # ||A|| = sqrt( sum_ij (ReA_ij^2 + ImA_ij^2) ); computed first, because it locates r = 0
        gapA_b = np.sqrt((d[cols_u]**2).sum(axis=1, skipna=False)
                         + (d[cols_v]**2).sum(axis=1, skipna=False))

        x_raw = d['signed_dist'].to_numpy()
        x0 = 0.0
        if bubble_shift == 'auto':
            try:
                x0 = crossing(x_raw, gapA_b.to_numpy(), gapA_isoValue, which=bubble_cross)
            except ValueError:
                print(os.path.basename(files[n]), ': ||A|| never crosses gapA_isoValue, not shifted')
        x = (x_raw - x0) / xi0                      # r = 0 where ||A|| = gapA_isoValue

        for col in cols_u:                          # ReA: solid
            ax.plot(x, d[col], color=color_of[col[1:]], ls='-', lw=LineWidth, alpha=alpha,
                    marker=bubble_marker, ms=bubble_ms, markevery=bubble_every,
                    markerfacecolor=bubble_fc, markeredgecolor=color_of[col[1:]], markeredgewidth=1.0)
        for col in cols_v:                          # ImA: dashed
            ax.plot(x, d[col], color=color_of[col[1:]], ls='--', lw=LineWidth, alpha=alpha,
                    marker=bubble_marker, ms=bubble_ms, markevery=bubble_every,
                    markerfacecolor=bubble_fc, markeredgecolor=color_of[col[1:]], markeredgewidth=1.0)

        ax.plot(x, gapA_b, ls='-', color=gapA_color_bubble, lw=LineWidth, alpha=alpha)

    ax.axvline(0, color='k', ls=':', lw=1)          # the isosurface position
    bubble_handles.append(Line2D([], [], ls='none', marker=bubble_marker, ms=bubble_ms + 1,
                                 markerfacecolor=bubble_fc, markeredgecolor='k',
                                 markeredgewidth=1.0, label=bubble_label))
    gapA_handles.append(Line2D([], [], color=gapA_color_bubble, ls='-', lw=LineWidth,
                               label=r'$||A||$, ' + bubble_label))
    
# ======================================================
#  plot 3rd path loaded data
# ======================================================
if RelaxingBubble_xyzAxis_PlotSwitch == 'ON':
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
        xk = xe[keep]                                   # x values that are kept

        ax.plot(xk, e['gapA'].to_numpy()[keep], ls='-', color=gapA_color_line, lw=LineWidth)
        gapA_handles.append(Line2D([], [], color=gapA_color_line, ls='-', lw=LineWidth,
                                   label=r'$||A||$, ' + s['label']))
        
        for col in cols_u + cols_v:
            if col not in e.columns:
                continue
            c = color_of[col[1:]]
            filled = col[0] == 'u'                      # ReA: filled, ImA: hollow
            ax.plot(xk, e[col].to_numpy()[keep], ls='-' if filled else '--', color=c,
                    marker=s['marker'], ms=s['ms'], markevery=s['every'],
                    markerfacecolor=s['fc'],
                    markeredgecolor=c, markeredgewidth=1.0, zorder=5)

        proxy_handles.append(Line2D([], [], ls='none', marker=s['marker'], ms=s['ms'] + 1,
                                markerfacecolor=s['fc'], markeredgecolor='k',
                                markeredgewidth=1.0, label=s['label']))            

# ======================================================
#    plot flat ABwall solutions from Mark
# ======================================================
# ---- load: every line = r, A11, A12, ..., A33 (all stored as complex numbers) ----
if FlatABWalls_PlotSwitch == 'ON':    
    FABW_data_dict = {}
    for axis in axes_id:
        FABW_data_dict[axis] = np.loadtxt(Flat_ABWalls_dir.format(axis), dtype=complex, delimiter=',', skiprows=1, ndmin=2)

    for axis in axes_id:
        d = FABW_data_dict[axis]
        r = d[:, 0].real                           # first column: r (real part)
        A = d[:, 1:]                               # next 9 columns: A11 ... A33 (complex)

        # NEW: gapA = sqrt( sum_ij |A_ij|^2 ), computed for every r
        gapA_M = np.sqrt((np.abs(A)**2).sum(axis=1))

        # NEW: shift r so that the gapA = gapA_isoValue crossing is at 0
        r_cross = crossing(r, gapA_M, gapA_isoValue, which=mark_cross)
        xm = mark_sign * (r - r_cross) / xi0
        print(f'Mark axis {axis}: gapA crossing ({mark_cross}) at r =', r_cross)

        # NEW: same cutoff as for the other data
        keep_m = (xm <= r_max) if r_max is not None else np.ones(len(xm), dtype=bool)

        ax.plot(xm[keep_m], gapA_M[keep_m], color=gapA_color_mark, ls='-', lw=LineWidth,
                marker=markers[axis] if mark_markers else 'none', ms=ms, markevery=every)
        gapA_handles.append(Line2D([], [], color=gapA_color_mark, ls='-', lw=LineWidth,
                                   label=r'$||A||$, ' + axes_name[axis]))        
        for k, c in enumerate(comps):
            ax.plot(xm[keep_m], A[keep_m, k].real, color=color_of[c], ls='-', lw=LineWidth,
                    marker=markers[axis] if mark_markers else 'none', ms=ms, markevery=every)
            ax.plot(xm[keep_m], A[keep_m, k].imag, color=color_of[c], ls='--', lw=LineWidth,
                    marker=markers[axis] if mark_markers else 'none', ms=ms, markevery=every,
                    markerfacecolor='none')            

    # one black legend entry per file (marker shape)
    if mark_markers:
        file_handles = [Line2D([], [], ls='none', color='k', marker=markers[a], ms=ms,
                               markerfacecolor='none', label=axes_name[a]) for a in axes_id]
    else:
        file_handles = []

# ======================================================
#  plot property controling and setting
# ======================================================
ax.set_xlabel(r'$r/\xi^{0}_{\mathrm{GL}}$', fontsize=axisFontSize)
ax.set_ylabel(r'$ReA_{\alpha j},\,\,ImA_{\alpha j}$', fontsize=axisFontSize)
ax.set_xlim([-25, 25])
if ylim is not None:
    ax.set_ylim(ylim)
ax.tick_params(labelsize=18)
ax.grid(alpha=0.25)
# ax.set_title(f'all {len(dfs)} lines', fontsize=12)

#extra_handles = proxy_handles + gapA_handles + file_handles
extra_handles = bubble_handles + proxy_handles + gapA_handles + file_handles
ax.legend(handles=comp_handles + extra_handles,
          ncol=7, fontsize=9, frameon=True, framealpha=0.9,
          loc='upper center',    # inside the box, in the empty band at the top
          labelspacing=0.3,      # vertical gap between rows (default 0.5)
          columnspacing=1.0,     # horizontal gap between columns (default 2.0)
          handlelength=1.8,      # length of the line sample (default 2.0)
          handletextpad=0.4,     # gap between line sample and text (default 0.8)
          borderpad=0.4)

fig.subplots_adjust(left=box_left, right=box_right, bottom=box_bottom, top=box_top)

if save_path is not None:
    fig.savefig(save_path, dpi=fig_dpi)
    print('saved', save_path)

plt.show()
