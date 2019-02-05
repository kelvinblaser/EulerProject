# Euler 272
#
# Prime powers have at most 3 solutions to x^3 = 1 MOD p^e
#
# Find all prime powers with 3 solutions.  Find all combinations of 
# five different prime powers with 3 solutions. This gives 243 solutions
# or 242 if you don't count 1.

from Primes import MakePrimeList, combProdLessThan
from math import log
from fractions import gcd
from bisect import bisect

def Euler272(n):
    primePowerMax = n // (7*9*13*19)
    if primePowerMax < 2:
        return 0
    oneSols = makeOneSols(primePowerMax // 31)
    oneSolDivThrees = [3*x for x in oneSols if 3*x <= primePowerMax // 31]
    #print oneSols
    #print oneSolDivThrees
    sumOneSols = oneSols[:]
    sumOneSolDivThrees = oneSolDivThrees[:]
    for i in range(1, len(oneSols)):
        sumOneSols[i] += sumOneSols[i-1]
        if i < len(oneSolDivThrees):
            sumOneSolDivThrees[i] += sumOneSolDivThrees[i-1]
    primePowers = [p for p in MakePrimeList(primePowerMax) if p%6 == 1 or p == 3]
    primePowers[0] *= 3 # 3 is special
    primePowers.sort()
    #print len(primePowers)
    ans = 0
    last = 0
    for comb in combProdLessThan(primePowers, 5, n):
        if comb[2] != last:
            last = comb[2]
            print comb, ans
        for x in combPowersLessThan(comb, n):
            ix = bisect(oneSols, n//x)
            ans += x * sumOneSols[ix-1]
            #print x, oneSols[ix-1], sumOneSols[ix-1]
            if x%3 != 0:
                ix = bisect(oneSolDivThrees, n//x)
                if ix > 0:
                    ans += x * sumOneSolDivThrees[ix-1]
                    #print x, n//x, oneSolDivThrees[ix-1], sumOneSolDivThrees[ix-1]
    return ans
    
def makeOneSols(n):
    isOneSol = [True]*(n+1)
    primes = [p for p in MakePrimeList(n) if p%6 == 1 or p == 3]
    for p in primes:
        for x in range(p, n+1, p):
            isOneSol[x] = False
    return [x for x in range(1, n+1) if isOneSol[x]]
    
def combPowersLessThan(comb, n):
    if len(comb) == 0:
        yield 1
        return
    pp = comb[-1]
    p = pp
    if pp == 9: p = 3
    prodRest = 1
    for q in comb[:-1]:
        prodRest *= q
    #print comb, n, prodRest, pp
    while pp <= n // prodRest:
        for x in combPowersLessThan(comb[:-1], n//pp):
            yield pp*x
        pp *= p
        #print '   ', pp
        
if __name__ == '__main__':
    #print Euler272(3 * 10**8)
    print Euler272(10**11)