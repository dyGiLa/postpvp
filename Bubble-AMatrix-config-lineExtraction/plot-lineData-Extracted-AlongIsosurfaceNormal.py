import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

# ===== edit these =====
out_dir = '/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/RelaxingCriticalBubbleConf-p27-T0.9275-Aali-cycle_001116'
column  = 'u11'          # which array to plot (u11, u12, ..., v33)
# ======================

files = sorted(glob.glob(os.path.join(out_dir, 'line_*.csv')))
print('found', len(files), 'files')

fig, ax = plt.subplots(figsize=(7, 5))

for f in files:
    d = pd.read_csv(f)
    ax.plot(d['signed_dist'], d[column], lw=1, alpha=0.7)

ax.axvline(0, color='k', ls='--', lw=1)   # the isosurface position
ax.set_xlabel('signed_dist  (0 = isosurface)')
ax.set_ylabel(column)
ax.set_ylim([0,3])

ax.set_title(f'{column} along {len(files)} lines')
plt.tight_layout()
plt.show()
