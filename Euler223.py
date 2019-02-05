###############################################################################
# Euler 223 - Almost Right Angled Triangles I
# Kelvin Blaser     2015.2.6
#
# Want number of solutions to a^2 + b^2 = c^2 + 1 with a <= b <= c and
# a+b+c <= 25,000,000 = N
#
# Re-write      a^2 + b^2 = c^2 + 1
#               a^2 - 1 = c^2 - b^2
#               (a+1)(a-1) = (c+b)(c-b) = xy
# Then
#               c = (x+y)/2 and b = (x-y)/2
#
# Let a range from 2 to N/3.  Find all of the ways to write (a+1)(a-1) as xy
# and create solutions.  Keep a collection of those solutions which satisfy
# a <= b <= c and a+b+c <= N.
#
# To do this, I will make a prime factorization for each number up to N/3+1
#
###################3
# So Far:  Uses too much memory and crashes with N = 25,000,000.  Implemented
# in c++ and don't have the same problem.  Still slow though.  There's
# probably a better algorithm.
###############################################################################
from Primes import MakePrimeList
from collections import defaultdict

def primeFactorizations(n):
    '''
    Create a list of prime factorizations, where each prime factorizeation is
    a dictionary with primes as keys and exponents as values
    '''
    primes = MakePrimeList(n+1)
    
    fact = [defaultdict(int) for _ in range(n+1)]
        
    for p in primes:
        pp = p
        while pp <= n:
            for x in range(pp,n+1,pp):
                fact[x][p] += 1
            pp *= p
    
    return fact

def multiplyPrimeFactorizations(pf1, pf2):
    '''
    Given two prime factorizations pf1 and pf2, return the prime factorization
    of the product of pf1 and pf2.
    '''
    res = defaultdict(int)
    for p in pf1:
        res[p] += pf1[p]
    for p in pf2:
        res[p] += pf2[p]
    return res

def factors(pf):
    if len(pf.keys()) == 0:
        yield 1
        return
    new_pf = defaultdict(int)
    keys = pf.keys()
    for k in keys[1:]:
        new_pf[k] = pf[k]
    pp = [keys[0]**e for e in range(pf[keys[0]]+1)]
    for x in factors(new_pf):
        for p in pp:
            yield x*p

def countTriangles(a, N, prime_factorizations):
    fact = multiplyPrimeFactorizations(prime_factorizations[a-1], prime_factorizations[a+1])
    res = 0
    lhs = a*a-1
    for x in factors(fact):
        y = lhs / x
        if x >= y:
            continue
        if x%2 != y%2:
            continue
        b,c = (y-x)/2, (y+x)/2
        if a > b or b > c:
            continue
        if a + b + c > N:
            continue
        res += 1
    return res

def almostRightSided(N):
    '''
    Counts the number of almost right sided triangles with perimeter <= N.
    '''
    prime_factorizations = primeFactorizations(N//3+1)
    res = 0
    for a in range(2, N//3+1):
        res += countTriangles(a, N, prime_factorizations)
        if a % 1000 == 0:
            print a, res
    return res + (N - 1)//2
