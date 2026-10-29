import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

# ===================== edit these =====================
out_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/RelaxingCriticalBubbleConf-p27-T0.9275-Aali-cycle_001116'

xi0   = 1.0         # x axis = signed_dist / xi0. Keep 1.0 if your data are already in xi_GL^0
ylim  = (-0.5, 3)      # set to None for automatic y range
alpha = 1.0         # transparency of each curve (lower it if the plot is crowded)
LineWidth = 2.2
axisFontSize = 26

first_idx = 0       # first file to consider (0 = line_00000.csv)
last_idx  = 28      # last file to consider, inclusive (24 = line_00024.csv). Use None for "up to the end"
PlotStep = 3        # use every `step`-th file: 1 = all files, 2 = every 2nd, 3 = every 3rd, ...
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

ax.set_xlabel(r'$r/\xi^{0}_{\mathrm{GL}}$', fontsize=axisFontSize)
ax.set_ylabel(r'$A_{\alpha j}$', fontsize=axisFontSize)
if ylim is not None:
    ax.set_ylim(ylim)
ax.tick_params(labelsize=18)
ax.grid(alpha=0.25)
ax.set_title(f'all {len(dfs)} lines', fontsize=12)

ax.legend(ncol=3, fontsize=16, frameon=True, framealpha=0.85, loc='right')

plt.tight_layout()
plt.show()
