# Euler 141 Square Progressive Numbers
# Kelvin Blaser 2013-10-19

from fractions import gcd
from numpy import sqrt

def isSquare(n):
    if n < 0:
        return False
    r = int(round(sqrt(n)))
    if r*r == n:
        return True
    return False

MAX = 10**12
l = []
s = 0
for a in range(2,int(round(MAX**(1./3.)))):
    print a
    for b in range(1,a):
        if a*a*a*b + b*b >= MAX:
            break
        if gcd(a,b) == 1:
            c = 1
            n = a*a*a*b*c*c + b*b*c
            while n < MAX:
                if isSquare(n) and not (n,a) in l:
                    l.append((n,a))
                    s += n
                c += 1
                n = a*a*a*b*c*c + b*b*c
print s, len(l)
print l
