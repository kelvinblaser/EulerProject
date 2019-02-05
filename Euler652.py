# Euler 652
# Kelvin Blaser		2019.02.04
#
# Solution Strategy:
#   1. Start with all (N-1)^2 pairs
#   2. Subtract 1 for each pair that are powers of the same base
#   3. Subtract 1 for each pair that are the same power of a different base
#   4. Add back 1 for each pair that fulfills both of the above (inclusion-exclusion)
#   5. Add in one for each fraction f = a/b where 1 <= a,b <= log(N)/log(2) and gcd(a,b) = 1
#
#   I can fold step 4 into step 2.  It's the same loop, so if I only count pairs
#   where the gcd of the powers is 1, I won't count any pairs that also fulfill
#   the criteria in step 3
#
#   Runs in O(N^1/4 log(N)) time and space
#   From the forum, I see that there are O(log(N)^2) algorithms.  Very impressive.

from fractions import Fraction
from math import log
from Primes import MakePrimeList

def intLog(N, b):
    l = int(log(N) / log(b))
    while pow(b,l) > N: l -= 1
    while pow(b,l+1) <= N: l += 1
    return l
    
def intRoot(N,b=2):
    r = int(N**(1.0/b))
    while pow(r,b) > N: r -= 1
    while pow(r+1,b) <= N: r += 1
    return r
    
def makeMu(l):
    primes = MakePrimeList(l)
    mu = [1]*(l+1)
    for p in primes:
        for x in range(p,l+1,p):
            mu[x] *= -1
        for xx in range(p*p, l+1, p*p):
            mu[xx] = 0
    return mu 
    
def makeSumPhi(l):
    primes = MakePrimeList(l)
    phi = [x for x in range(l+1)]
    for p in primes:
        for x in range(p,l+1,p):
            phi[x] *= (p-1)
            phi[x] //= p
    # Summatory phi starting from 2
    for x in range(3, l+1):
        phi[x] += phi[x-1]
    return phi
    
def makeLogCounts(N):
    l = intLog(N,2)
    logCounts = [0]*(l+1)
    # logCounts[x] will be the number of bases b for which intLog(N,b) == x
    last = N
    for x in range(1,l+1):
        # find the largest number y for which intLog(N,y) > x
        bot, top = 2, last
        if intLog(N,top) > x:
            logCounts[x] = 0
            continue
        if intLog(N,bot) <= x: 
            logCounts[x] = last - bot + 1
            last = 1
            continue
        while top - bot > 1:
            mid = bot + (top-bot)//2
            if intLog(N,mid) > x:
                bot = mid
            else:
                top = mid
        logCounts[x] = last - bot
        last = bot  
    return logCounts

def protoLogValues(N):
    ans = (N-1)*(N-1)
    ans -= powersOfSameBase(N)
    ans -= samePowerOfDifferentBase(N)
    ans += powerSameBaseAndSamePowerDiffBase(N)
    ans += powerOfTwoFractions(N)
    return ans
    
def powersOfSameBase(N):
    # Look for bases less than sqrt(N)
    # Many bases have the same logarithm log_b(N)
    # Count these first, then only count bases that are not powers of other 
    # bases and only count pairs of powers whose gcd is 1
    r = intRoot(N)
    l = intLog(N,2)
    lCounts = makeLogCounts(N)
    nonBases = set()
    for x in range(2,intRoot(r)+1):
        px = x*x
        while px <= r:
            nonBases.add(px)
            px *= x
    for nb in nonBases:
        lCounts[intLog(N,nb)] -= 1
        
    ans = 0
    sPhi = makeSumPhi(l)
    for x in range(2,l+1):
        ans += lCounts[x] * sPhi[x]
    return 2*ans + N - 1
    
def samePowerOfDifferentBase(N):
    # Pairs of squares + Pairs of cubes. 
    # Pairs of 4th powers already counted by pairs of squares
    # Pairs of 6th powers counted twice so add them back in
    # Looks like  sum(mu(x) * pairs of x powers)
    l = intLog(N,2)
    mu = makeMu(l)
    ans = 0
    for x in range(2, l+1):
        r = intRoot(N,x)
        ans += mu[x] * ((r-1)*(r-2)) // 2
    return -2*ans
    
def powerSameBaseAndSamePowerDiffBase(N):
    return 0
    
def powerOfTwoFractions(N):
    l = intLog(N,2)
    return len(set(Fraction(a,b) for a in range(1, l+1) for b in range(1,l+1)))
    
    
if __name__ == '__main__':
    print 'powersOfSameBase(100) = {0}'.format(powersOfSameBase(100))
    print 'samePowerOfDifferentBase(100) = {0}'.format(samePowerOfDifferentBase(100))
    
    print ''
    print 'D({0}) = {1}'.format(5, protoLogValues(5))         # Should be 13
    print 'D({0}) = {1}'.format(10, protoLogValues(10))       # Should be 69
    print 'D({0}) = {1}'.format(100, protoLogValues(100))     # Should be 9607
    print 'D({0}) = {1}'.format(10000, protoLogValues(10000)) # Should be 99959605
    
    print ''
    ans = protoLogValues(10**18)
    print 'D({0}) = {1}'.format('10^18', ans)
    print 'Last 9 digits: {0}'.format(ans%(10**9))
    print ''
    print 'D({0}) = {1}'.format('10^22', protoLogValues(10**22))