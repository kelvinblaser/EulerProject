###############################################################################
# Euler 233 - Lattice points on a circle
# Kelvin Blaser     2015.1.24
#
# This problem reduces to finding the solutions of
#       a^2 + b^2 = 2c^2        c = 2N always and c = N if a,b,c all odd
#
# One can show that
###############################################################################
from fractions import gcd
from bisect import bisect
from Primes import MakePrimeList

def qNumGen(qs, b, n):
    ''' Creates all numbers of the form q1^b1 * q2^b2 * q3^b3 <= n where
    q1,q2,q3 can be any 3 of qs and b1,b2,b3 are specified by b

    qs needs to be a sorted iterable and b needs to be a three component list
    or tuple. '''
    b = list(b)
    b.sort()
    b3,b2,b1 = tuple(b)
    for q1 in qs:
        n1 = q1**b1
        if n1 > n:
            break
        if b2 == 0:
            yield n1
            continue
        for q2 in qs:
            if q2 == q1:
                continue
            n2 = q2**b2
            if n2*n1 > n:
                break
            if b3 == 0:
                yield n1*n2
                continue
            for q3 in qs:
                if q3 == q2 or q3 == q1:
                    continue
                n3 = q3**b3
                if n3*n2*n1 > n:
                    break
                yield n3*n2*n1
    return

def pNumsSums(qs, n):
    possible = [False]+[True]*n
    for q in qs:
        for x in range(q,n+1,q):
            possible[x] = False
    pNums = [x for x in range(1,n+1) if possible[x]]
    pSums = [x for x in pNums]
    for i in range(1,len(pSums)):
        pSums[i] += pSums[i-1]
    return pNums, pSums

def Euler233(N):
    ps = MakePrimeList(max(17,N/(5**3*13**2)))
    qs = [q for q in ps if q%4 == 1]
    pNums, pSums = pNumsSums(qs, N/(5**3*13*2*17))
    patterns = [(52,0,0),(17,1,0),(10,2,0),(7,3,0),(3,2,1)]
    nums420sum = 0
    for b in patterns:
        for qNum in qNumGen(qs,b,N):
            ix = bisect(pNums, N / qNum)
            if ix > 0:
                nums420sum += qNum * pSums[ix-1]
    return nums420sum


                
