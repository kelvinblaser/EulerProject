# Euler 218 - Perfect Right Angled Triangles
# Kelvin Blaser 2013-10-19

from fractions import gcd

count = 0
max_q = 10**2
max_c = 10**8
for q in range(2, max_q):
    for r in range(q%2+1, q, 2):
        if (q*q + r*r)**2 > max_c:
            break
        if gcd(q,r) == 1:
            m = q*q - r*r
            n = 2*r*q
            a = m*m - n*n
            b = 2*m*n
            A = (a*b)/2
            if not (A%6 == 0 and A%28 == 0):
                count += 1
print count
