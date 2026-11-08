"""
Mass current (Regan, Wiman, Sauls, Eq. 26) along many 1D line cuts, one csv per line_id.

    j_i = Im[ K1 A*_{aj} d_i A_{aj} + K2 A*_{aj} d_j A_{ai} + K3 A*_{ai} d_j A_{aj} ]

(prefactor 4m/hbar dropped, K1 = K2 = K3 = 1)

Files:  line_00000.csv, line_00001.csv, ...   (header: line_id, t, x, y, z, signed_dist, gapA, u11..v33)

Along each line only one derivative exists, taken against signed_dist (s):

    d_i A = n_i dA/ds ,     n_i = d x_i / ds   (unit vector of the line, taken from the x,y,z columns)

so the three components jx, jy, jz are obtained for every line.
If you prefer to give the line direction by hand, set DIRECTION below.
"""
import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- paths ----------------
DATA_ROOT = "/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble/RelaxingCriticalBubbleConf-EvolveExtraction-p27-T0.9275-Aali-cycle_001116"     # folder containing line_000xx.csv
SAVE_ROOT = "/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble"                # folder for the plot
OUTNAME = "MassCurr_EvolveExtraction_lineID-p27-0.4Tc-BBubble.png"

# ---------------- file selection ----------------
first_idx = 0       # first file to consider (0 = line_00000.csv)
last_idx  = 24      # last file to consider, inclusive (23 = line_00023.csv). Use None for "up to the end"
PlotStep = 3       # use every `step`-th file: 1 = all files, 2 = every 2nd, 3 = every 3rd, ...

# ---------------- setup ----------------
K1 = K2 = K3 = 1.0

# Direction of the line, used in d_i A = n_i dA/ds.
#   None            -> computed from the x,y,z columns (n = dx/ds, normalised, point by point)
#   (nx, ny, nz)    -> fixed direction for all lines, e.g. (1.0, 0.0, 0.0)
DIRECTION = None

colors = ["tab:blue", "tab:red", "tab:green", "tab:orange", "tab:purple",
          "tab:cyan", "black", "magenta", "tab:brown", "tab:olive"]    # 10 distinct colors, one per line_id

LineStyle = ["-", "--", ":"]          # jx, jy, jz

axisFontSize = 18
LegendFontS = 9
LineWidth = 2.5
LegendNCoulumn = 4

ylim  = (-2.0, 2.0)
xlim  = (-15.0, 15.0)
# ---------------- setup ----------------


FILE_RE = re.compile(r"^line_(\d+)\.csv$")


def select_files(folder):
    """Return [(file_index, path), ...] for line_xxxxx.csv, filtered by first_idx / last_idx / PlotStep."""
    found = []
    for name in os.listdir(folder):
        m = FILE_RE.match(name)
        if m:
            found.append((int(m.group(1)), os.path.join(folder, name)))
    found.sort()
    found = [(i, p) for i, p in found
             if i >= first_idx and (last_idx is None or i <= last_idx)]
    return found[::PlotStep]


def load_A(df):
    """A[n, alpha, i] = u_{alpha i} + i v_{alpha i}  (first index alpha, second index i)."""
    u = np.stack([df[f"u{a}{i}"].to_numpy() for a in (1, 2, 3) for i in (1, 2, 3)], axis=1)
    v = np.stack([df[f"v{a}{i}"].to_numpy() for a in (1, 2, 3) for i in (1, 2, 3)], axis=1)
    return (u + 1j * v).reshape(-1, 3, 3)


def line_direction(df, s):
    """Unit vector n_i(s) of the line, shape (N, 3)."""
    if DIRECTION is not None:
        n = np.asarray(DIRECTION, float)
        return np.tile(n / np.linalg.norm(n), (len(s), 1))
    pos = df[["x", "y", "z"]].to_numpy()
    dpos = np.gradient(pos, s, axis=0)                  # d(x,y,z)/ds
    return dpos / np.linalg.norm(dpos, axis=1)[:, None]


def mass_current(df):
    if "vtkValidPointMask" in df:
        df = df[df["vtkValidPointMask"] == 1]
    df = df.dropna(subset=["signed_dist", "x", "y", "z"])
    df = df.sort_values("signed_dist").drop_duplicates("signed_dist").reset_index(drop=True)

    s = df["signed_dist"].to_numpy()
    A = load_A(df)
    n = line_direction(df, s)                           # shape (N, 3), n_i

    dA = np.gradient(A, s, axis=0)                      # dA/ds, shape (N, alpha, j)
    Ac = np.conj(A)

    t1 = np.einsum("naj,naj->n", Ac, dA)[:, None] * n   # A*_{aj} d_i A_{aj}
    t2 = np.einsum("naj,nj,nai->ni", Ac, n, dA)         # A*_{aj} d_j A_{ai}
    t3 = np.einsum("nai,nj,naj->ni", Ac, n, dA)         # A*_{ai} d_j A_{aj}

    return s, np.imag(K1 * t1 + K2 * t2 + K3 * t3)      # (N, 3): jx, jy, jz


def main():
    files = select_files(DATA_ROOT)
    if not files:
        raise SystemExit(f"no line_xxxxx.csv found in {DATA_ROOT} for the chosen index range")

    fig, ax = plt.subplots(figsize=(8, 5))

    for k, (idx, path) in enumerate(files):
        df = pd.read_csv(path)
        line_id = int(df["line_id"].iloc[0])
        s, j = mass_current(df)
        for c, comp in enumerate("xyz"):
            ax.plot(s, j[:, c], color=colors[k % len(colors)], ls=LineStyle[c], lw=LineWidth,
                    label=f"$J_{comp}$, line_id = {line_id}")

    ax.set_xlabel(r'$r/\xi^{0}_{\mathrm{GL}}$', fontsize=axisFontSize)
    ax.set_ylabel(r"$J_i/4m/\hbar$", fontsize=axisFontSize)
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

        
    ax.tick_params(labelsize=18)
    ax.grid(alpha=0.3)
    ax.legend(ncol=LegendNCoulumn, fontsize=LegendFontS, loc="upper left", framealpha=0.9)

    os.makedirs(SAVE_ROOT, exist_ok=True)
    outpath = os.path.join(SAVE_ROOT, OUTNAME)
    # bbox_inches="tight" crops extra white margins, so the plot fills the image
    fig.savefig(outpath, dpi=200, bbox_inches="tight")

    plt.show()
    print(f"plotted {len(files)} file(s): " + ", ".join(os.path.basename(p) for _, p in files))
    print(f"saved {outpath}")


if __name__ == "__main__":
    main()
