# Euler 261
# Kelvin Blaser     2019-02-20

from fractions import gcd
from Euler import positivePell
from Primes import MakePrimeList

def solution():
    Nmax = 10**10
    kSet = set()
    r = int(Nmax**0.5) + 1
    primes = MakePrimeList(int(r**0.5) + 10)
    squareParts = [1]*(r+2)
    squareFreeParts = [x for x in range(r+2)]
    for x in range(2, r+2, 4):
        squareFreeParts[x] //= 2
    for x in range(4, r+2, 4):
        squareFreeParts[x] //= 4
    for p in primes:
        for x in range(p*p, r+2, p*p):
            while squareFreeParts[x] > 0 and squareFreeParts[x] % (p*p) == 0:
                squareFreeParts[x] //= p*p
                squareParts[x] *= p
    for m in range(1,r+1):  # k is at least m^2
        g = gcd(4, m*(m+1))
        xx = squareParts[m] * squareParts[m+1]
        y = squareFreeParts[m] * squareFreeParts[m+1]
        b = 4 // g
        D = y*b
        for z,v in positivePell(D,10000):
            if (z%2 == 0 or z < 2*m+1): continue
            q = xx*y*v
            x = (z-1)//2 - m
            k = m*(x+m+1) + q
            if k > Nmax: break
            kSet.add(k)
    kVec = list(kSet)
    kVec.sort()
    s = 0
    for k in kVec:
        s += k
    return s

if __name__ == '__main__':
    print solution()
