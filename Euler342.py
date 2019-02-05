################################################################################
# Euler 342 - The Totient of a Square is a Cube
# Kelvin Blaser      2015.03.25
#
################################################################################

from Primes import MakePrimeList
from Euler import restrictedPrimeFactorizations
from bisect import bisect

def isCube(n):
    r = int(n**(1./3.))
    return (r**3 == n) or ((r+1)**3 == n)

def eulerPhi(n,primes):
    x = n
    phi = n
    for p in primes:
        if x%p == 0:
            phi *= p-1
            phi /= p
        while x%p == 0:
            x /= p
        if p*p > x:
            if x > 1:
                phi *= x-1
            return phi
    return phi
            

def Euler342(N):
    ps = MakePrimeList(int(N**0.5)+1)
    ret = 0
    for ix,p in enumerate(ps):
        if ix%10 == 0:
            print p, ret
        pp = p*p
        ppp = p*p*p
        while pp < N:
            jx = min(ix,bisect(ps,N//pp + 1))
            for x in restrictedPrimeFactorizations(ps[:jx],N//pp+1):
                n = x*pp
                if n >= N:
                    continue
                phi = eulerPhi(n,ps)
                if isCube(n*phi):
                    #print n, phi
                    ret += n
            pp *= ppp
    return ret

def Euler342b(N):
    ps = MakePrimeList(int(N**0.5)+1)
    ret = 0
    for n in xrange(2,N):
        if n%10000 == 0:
            print n, ret
        if isCube(n*eulerPhi(n,ps)):
            ret += n
    return ret


