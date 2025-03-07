from scipy.optimize import fsolve

def equations(svec, *paras):
    m1, m2, m3, n1, n2, n3, cosphi, sinphi = svec
    u11, v11, u12, v12, u13, v13, DeltaA = paras
    return [-u11 + ((cosphi*m1 - n1*sinphi)*DeltaA)/1.414213562,
            -v11 + ((cosphi*n1 + m1*sinphi)*DeltaA)/1.414213562,
            -u12 + ((cosphi*m2 - n2*sinphi)*DeltaA)/1.414213562,
            -v12 + ((cosphi*n2 + m2*sinphi)*DeltaA)/1.414213562,
            -u13 + ((cosphi*m3 - n3*sinphi)*DeltaA)/1.414213562,
            -v13 + ((cosphi*n3 + m3*sinphi)*DeltaA)/1.414213562,
            -1 + cosphi*cosphi + sinphi*sinphi,
            m1*n1 + m2*n2 + m3*n3]

inivec=[0.5, 0.45, 0.3, 0.6, 0.23, 0.45, 0.88, 0.34]
inivec2=(1.0, 0., 0., 0., 1.0, 0., 1., 0.)

paras=(1.618761211, 0., 0., 1.618761211, 0., 0., 2.289274059229696)
paras2=(0, 0., 0., 1.618761211, 1.618761211, 0., 2.289274059229696)

s = fsolve(equations, inivec2, args=paras2, xtol=1.49012e-13)

print(s)
print(s[0]*s[0]+s[1]*s[1]+s[2]*s[2])
print(s[3]*s[3]+s[4]*s[4]+s[5]*s[5])
print(s[6]*s[6]+s[7]*s[7])
print(equations(s,*paras2))
