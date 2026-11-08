"""
Mass current (Regan, Wiman, Sauls, Eq. 26) along 1D line cuts of a 3D dataset.

    j_i = Im[ K1 A*_{aj} d_i A_{aj} + K2 A*_{aj} d_j A_{ai} + K3 A*_{ai} d_j A_{aj} ]

(prefactor 4m/hbar dropped, K1 = K2 = K3 = 1)

f1.csv is a cut along x, f2.csv along y, f3.csv along z, so along each cut
only one derivative exists:  d_i A = n_i dA/d(arc_length),  with n = unit vector of the axis.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- paths ----------------
DATA_ROOT = "/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble"     # folder containing the csv files
SAVE_ROOT = "/home/heidi/Documents/dyGiLa-project/dyGiLa-visualization-images/B-phase-Bubble"      # folder for the plot
OUTNAME = "MassCurr_xyz-27bar-0.4Tc.png"

# ---------------- setup ----------------
K1 = K2 = K3 = 1.0

# file name -> (axis label, unit vector of the cut direction)
CUTS = {
    "Line-Data-x_axis-A_al_i-l_Vector-parallel-w-AB_Wall.csv": ("x", (1.0, 0.0, 0.0)),
    "Line-Data-y_axis-A_al_i-along-olive-tips.csv": ("y", (0.0, 1.0, 0.0)),
    "Line-Data-z_axis-A_al_i-l_Vector-perpendicular-w-AB_Wall.csv": ("z", (0.0, 0.0, 1.0)),
}

PlotLabels = {
    0: r'$\hat{\mathbf{l}} \perp \hat{\mathbf{n}}$',
    # 1: r'$\hat{\mathbf{l}} ? \hat{\mathbf{n}}$',
    1: r'along olive tips',    
    2: r'$\hat{\mathbf{l}} \parallel \hat{\mathbf{n}}$'
}

colors = ["tab:blue", "tab:red", "tab:green"]
LineStyle = ["-", "--", ":"]

axisFontSize = 18
LegendFontS = 9
LineWidth = 2.5
LegendNCoulumn = 3

ylim  = (-2.0, 2.0)
# ---------------- setup ----------------


def load_A(df):
    """A[n, alpha, i] = u_{alpha i} + i v_{alpha i}  (first index alpha, second index i)."""
    u = np.stack([df[f"u{a}{i}"].to_numpy() for a in (1, 2, 3) for i in (1, 2, 3)], axis=1)
    v = np.stack([df[f"v{a}{i}"].to_numpy() for a in (1, 2, 3) for i in (1, 2, 3)], axis=1)
    return (u + 1j * v).reshape(-1, 3, 3)


def mass_current(df, direction):
    if "vtkValidPointMask" in df:
        df = df[df["vtkValidPointMask"] == 1]
    df = df.sort_values("arc_length").reset_index(drop=True)

    s = df["arc_length"].to_numpy()
    A = load_A(df)
    n = np.asarray(direction, float)          # shape (3,), n_i

    dA = np.gradient(A, s, axis=0)            # dA/ds, shape (N, alpha, j)
    Ac = np.conj(A)

    t1 = np.einsum("naj,naj->n", Ac, dA)[:, None] * n   # A*_{aj} d_i A_{aj}
    t2 = np.einsum("naj,j,nai->ni", Ac, n, dA)          # A*_{aj} d_j A_{ai}
    t3 = np.einsum("nai,j,naj->ni", Ac, n, dA)          # A*_{ai} d_j A_{aj}

    return s, np.imag(K1 * t1 + K2 * t2 + K3 * t3)      # (N, 3): jx, jy, jz


def main():
    fig, ax = plt.subplots(figsize=(8, 5))
    comp_style = {0: "-", 1: "--", 2: ":"}

    for k, (fname, (axis, direction)) in enumerate(CUTS.items()):
        df = pd.read_csv(os.path.join(DATA_ROOT, fname))
        s, j = mass_current(df, direction)
        for c, comp in enumerate("xyz"):
            ax.plot(s, j[:, c], color=colors[k], ls=LineStyle[c], lw=LineWidth,
                    label=f"$J_{comp}$, {PlotLabels[k]}")

    ax.set_xlabel(r'$r/\xi^{0}_{\mathrm{GL}}$', fontsize=axisFontSize)
    ax.set_ylabel(r"$J_i/4m/\hbar$", fontsize=axisFontSize)
    if ylim is not None:
        ax.set_ylim(ylim)

    ax.tick_params(labelsize=18)
    ax.grid(alpha=0.3)
    # legend below the axes so it never covers the curves
    ax.legend(ncol=LegendNCoulumn, fontsize=LegendFontS, loc="upper left", framealpha=0.9)
 
    os.makedirs(SAVE_ROOT, exist_ok=True)
    outpath = os.path.join(SAVE_ROOT, OUTNAME)
    # bbox_inches="tight" crops extra white margins, so the plot fills the image
    fig.savefig(outpath, dpi=200, bbox_inches="tight")

    plt.show()
    print(f"saved {outpath}")


if __name__ == "__main__":
    main()
