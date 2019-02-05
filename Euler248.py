# Euler 248
from itertools import product
from Primes import MakePrimeList, isPrime

thirteenFact = 2*3*4*5*6*7*8*9*10*11*12*13
def factorsOfThirteenFact():
    factors = set()
    primes = [(2,10), (3,5), (5,2), (7,1), (11,1), (13,1)]
    powers = [[p**x for x in range(a+1)] for p,a in primes]
    for t in product(*powers):
        f = 1
        for x in t:
            f *= x
        factors.add(f)
    return factors
    
def validPrimes(factors):
    primes = MakePrimeList(100000)
    validPrimes = [f+1 for f in factors if isPrime(f+1, primes)]
    return validPrimes
    
def solutions(sols, validPrimes, ix, val, phi):
    phiToGo = thirteenFact // phi
    while(ix >= 0 and phiToGo % (validPrimes[ix]-1) != 0):
        ix -= 1
    if ix < 0: return
    p = validPrimes[ix]
    phiNew = 1
    pp = 1
    while (phiToGo % phiNew == 0):
        if phiToGo == phiNew:
            sols.add(val*pp)
            #if len(sols) % 1000 == 0: print len(sols)
        solutions(sols, validPrimes, ix-1, val*pp, phi*phiNew)
            
        pp *= p
        if pp == p:
            phiNew *= p-1
        else:
            phiNew *= p
            
if __name__ == '__main__':
    facts = factorsOfThirteenFact()
    print max(facts)
    vp = validPrimes(facts)
    sols = set()
    solutions(sols, vp, len(vp)-1, 1, 1)
    sols = list(sols)
    sols.sort()
    print sols[0]
    print sols[-1]
    print 'sols[10] = {0}'.format(sols[10-1])
    print 'sols[100] = {0}'.format(sols[100-1])
    print 'sols[1000] = {0}'.format(sols[1000-1])    
    print len(sols)
    print 'sols[150,000] = {0}'.format(sols[150000-1])