import os

vtu_files = sorted([
    f for f in os.listdir(".")
    if f.endswith(".vtu")
])

if not vtu_files:
    raise RuntimeError("No VTU files found")

with open("domain.pvtu", "w") as f:

    f.write('<?xml version="1.0"?>\n')
    f.write('<VTKFile type="PUnstructuredGrid" version="1.0" byte_order="LittleEndian">\n')

    f.write('  <PUnstructuredGrid GhostLevel="0">\n')

    # ---------------- POINT DATA ----------------
    f.write('    <PPointData Scalars="GradPhi1">\n')

    for name in ["GradPhi1", "GradPhi2", "GradPhi3"]:
        f.write(
            f'      <PDataArray type="Float64" Name="{name}" NumberOfComponents="1"/>\n'
        )

    f.write('    </PPointData>\n')

    # ---------------- CELL DATA ----------------
    f.write('    <PCellData>\n')
    f.write('      <PDataArray type="UInt8" Name="vtkGhostType" NumberOfComponents="1"/>\n')
    f.write('    </PCellData>\n')

    # ---------------- POINTS ----------------
    f.write('    <PPoints>\n')
    f.write('      <PDataArray type="Float64" NumberOfComponents="3"/>\n')
    f.write('    </PPoints>\n')

    # ---------------- PIECES ----------------
    for vtu in vtu_files:
        f.write(f'    <Piece Source="{vtu}"/>\n')

    f.write('  </PUnstructuredGrid>\n')
    f.write('</VTKFile>\n')

print("Wrote domain.pvtu")
