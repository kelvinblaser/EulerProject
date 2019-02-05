# Euler 77 - Prime Partition
# Kelvin Blaser - 11-17-2012

import Primes

def partialPrimePartition(n,p, primeList, partialPrimeMemo):
    """
    Calculates the number of ways n can be partitioned into primes with largest
    prime p.

    Need to calculate primeList before hand.
    """
    if p==2:
        return 1-(n%2)
    if partialPrimeMemo.has_key((n,p)):
        return partialPrimeMemo[(n,p)]
    if p==n:
        return 1

    partialPartition = 0
    pMax = min(n-p, p)
    ps = tuple([prime for prime in primeList if prime <= pMax])
    for prime in ps:
        partialPartition += partialPrimePartition(n-p, prime, ps,
                                                  partialPrimeMemo)
    partialPrimeMemo[(n,p)] = partialPartition
    return partialPartition

def primePartition(n, primeList, partialPrimeMemo):
    """
    Calculates the number of ways to partition n into a sum of primes.

    User needs to calculate primeList before using.
    """
    partition = 0
    ps = tuple([p for p in primeList if p <= n])
    for p in ps:
        partition += partialPrimePartition(n, p, ps, partialPrimeMemo)
    return partition

def Euler77(numWays):
    """
    Finds the first number that can be partitioned into primes in numWays.
    """
    primeList = Primes.MakePrimeList(max(numWays,100))
    partialPrimeMemo = {}
    n = 2
    while primePartition(n, primeList, partialPrimeMemo) < numWays:
        n += 1
    return n
