import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.lines import Line2D

# ===================== edit these =====================
data_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/Flat-ABWall-Solution-fromMark-27bar/AB_wall_sol_axis-{:}.csv'
axes_id    = [0, 1, 2]
# axes_id    = [0]
axes_name  = {0: 'along $x$', 1: 'along $y$', 2: 'along $z$'}
markers    = {0: 'o', 1: 's', 2: '^'}      # one marker shape per file

LineWidth    = 1.8
ms           = 6          # marker size
every        = 8          # draw a marker on every n-th point
axisFontSize = 26
ylim         = None       # e.g. (-0.5, 3), or None for automatic
# ======================================================

# ---- load: every line = r, A11, A12, ..., A33 (all stored as complex numbers) ----
data_dict = {}
for axis in axes_id:
    data_dict[axis] = np.loadtxt(data_dir.format(axis), dtype=complex,
                                 delimiter=',', skiprows=1, ndmin=2)

comps    = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
colors   = cm.tab10(range(len(comps)))         # one color per component
color_of = {c: colors[k] for k, c in enumerate(comps)}

fig, ax = plt.subplots(figsize=(8, 5.5))

for axis in axes_id:
    d = data_dict[axis]
    r = d[:, 0].real                           # first column: r (real part)
    A = d[:, 1:]                               # next 9 columns: A11 ... A33 (complex)

    gapA_M = np.sqrt((np.abs(A)**2).sum(axis=1))
    ax.plot(r, gapA_M, color='k', ls='-', lw=LineWidth)
       
    for k, c in enumerate(comps):
        # Re A: solid, filled markers
        ax.plot(r, A[:, k].real, color=color_of[c], ls='-', lw=LineWidth,
                marker=markers[axis], ms=ms, markevery=every,
                label=rf'$\mathrm{{Re}}A_{{{c}}}$' if axis == axes_id[0] else None)
        # Im A: dashed, hollow markers
        ax.plot(r, A[:, k].imag, color=color_of[c], ls='--', lw=LineWidth,
                marker=markers[axis], ms=ms, markevery=every,
                markerfacecolor='none',
                label=rf'$\mathrm{{Im}}A_{{{c}}}$' if axis == axes_id[0] else None)

        
# one black legend entry per file (marker shape)
file_handles = [Line2D([], [], ls='none', color='k', marker=markers[a], ms=ms,
                       markerfacecolor='none', label=axes_name[a]) for a in axes_id]

ax.set_xlabel(r'$r/\xi^{0}_{\mathrm{GL}}$', fontsize=axisFontSize)
ax.set_ylabel(r'$A_{\alpha j}$', fontsize=axisFontSize)
if ylim is not None:
    ax.set_ylim(ylim)
ax.tick_params(labelsize=18)
ax.grid(alpha=0.25)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles + file_handles, labels + [h.get_label() for h in file_handles],
          ncol=3, fontsize=12, frameon=True, framealpha=0.85, loc='best')

plt.tight_layout()
plt.show()
