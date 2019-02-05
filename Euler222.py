###############################################################################
# Euler 222 - Sphere Packing
# Kelvin Blaser     2015.1.24
#
###############################################################################

def pipeLen(rs, R):
    if len(rs) == 1:
        return rs,rs[0]
    r1 = rs.pop()
    r2 = rs.pop()
    if not rs:
        L = r1 + r2 + 2*(R*(r1+r2-R))**0.5
        return [r1,r2],L
    mids, L = pipeLen(rs,R)
    m1 = mids[0]
    m2 = mids[-1]
    L += r1 + r2 - m1 - m2
    L1 = L + 2*(R*(r1+m1-R))**0.5 + 2*(R*(r2+m2-R))**0.5
    L2 = L + 2*(R*(r1+m2-R))**0.5 + 2*(R*(r2+m1-R))**0.5
    if L1 < L2:
        return [r1]+mids+[r2], L1
    else:
        return [r2]+mids+[r1], L2
    
