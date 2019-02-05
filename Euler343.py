################################################################################
# Euler 343 - Fractional Sequences
# Kelvin Blaser   2015.02.23
#
# f(n) = p-1 where p is the largest prime that divides n+1
################################################################################
from Euler import isQuadResidue, tonelliShanks
from Primes import MakePrimeList
import scipy as sp

def roots(p):
    ''' Finds the roots of k^3 + 1 = (k + 1)(k^2 - k + 1) = 0 mod p '''
    k = [p-1,]
    twoInv = pow(2,p-2,p)
    n = (twoInv*twoInv - 1)%p
    if isQuadResidue(n,p):
        r = tonelliShanks(n,p)
        k += [(twoInv + r)%p, (twoInv - r)%p]
    return k

def seqSumCubes(N):
    k3 = sp.zeros(N+1, dtype=sp.int64)
    maxPrime = 0 * k3
    for k in xrange(1,N+1):
        k3[k] = k*k*k + 1

    ps = MakePrimeList(N+5)
    for p in ps:
        for kstart in roots(p):
            for k in xrange(kstart,N+1,p):
                while k3[k] % p == 0:
                    k3[k] /= p
                maxPrime[k] = p

    ret = 0
    for k in xrange(1,N+1):
        if k3[k] != 1 and k3[k] > maxPrime[k]:
            maxPrime[k] = k3[k]
        ret += maxPrime[k] - 1

    return ret

if __name__ == '__main__':
    print seqSumCubes(100)
    print seqSumCubes(2*10**6)

