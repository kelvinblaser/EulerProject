################################################################################
# Euler 437 - Fibonacci Primitive Roots
# Kelvin Blaser      2015.03.21
#
# Working in Z/pZ for prime p.  All numbers except 0 have an inverse. Suppose
# x is a Fibonacci primitive root of p.  Then we can divide the definition by
# x^n to get
#       x^n + x^(n+1) = x^(n+2) mod p
#       1 + x = x^2 mod p
#
# Thus, if x exists, it is a solution to the golden mean equation
#  x = (1 +(or -) sqrt(5))/2
# We can test if 5 is a quadratic residue modulo p.  If so, we calculate the
# root(s) x and test if either of these are primitive roots.
################################################################################

from Euler import isQuadResidue, tonelliShanks
from Primes import MakePrimeList

def isPrimitiveRoot(r1,r2,pp,primes):
    q = []
    n = pp-1
    for p in primes:
        if p*p > n:
            if n > 1:
                q.append(n)
            break
        if n%p == 0:
            q.append(p)
            while n%p == 0:
                n /= p
    b1,b2 = True,True
    for p in q:
        if pow(r1,(pp-1)/p,pp) == 1:
            b1 = False
        if pow(r2,(pp-1)/p,pp) == 1:
            b2 = False
    return b1 or b2

def Euler437(N):
    ps = MakePrimeList(N)
    ret = 0
    count = 0
    for p in ps[1:]: # ps[1:] excludes 2, the case where 2^-1 does not exist
        if isQuadResidue(5%p,p):
            r = tonelliShanks(5%p,p)
            inv2 = pow(2,p-2,p)
            x1 = (inv2*(1+r))%p
            x2 = (inv2*(1-r))%p
            if isPrimitiveRoot(x1,x2,p,ps):
                ret += p
                count += 1
    return count, ret

if __name__ == '__main__':
    print Euler437(10000)
    print Euler437(100000000)
