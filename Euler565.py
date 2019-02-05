# Euler 565

from Primes import MakePrimeList, Miller_Rabin

def S(n, pMOD):
    r = int(n**0.5) + 1
    primes = MakePrimeList(r)
    eligiblePrimePowers = []
    for p in primes:
        pp = 1
        pS = 0
        while pp <= n:
            pS += pp
            if pS % pMOD == 0:
                eligiblePrimePowers.append((pp, p))
            pp *= p
    # Check even multiples of pMOD
    start = (r//(2*pMOD) + 1)*(2*pMOD)
    for x in range(start, n+1, 2*pMOD):
        if Miller_Rabin(x-1):
            eligiblePrimePowers.append((x-1, x-1))
    eligiblePrimePowers.sort()
    print len(eligiblePrimePowers)