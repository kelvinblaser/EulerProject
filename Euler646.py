# Euler 646

from Primes import MakePrimeList
from collections import defaultdict
from math import log

class Euler646:
    def __init__(self):
        self.primes = MakePrimeList(70)
        #self.cache = {}
        #self.allCache = {}
        #self.printLimit = 0
        #self.printDict = {}
        
    def sumAllFactors(self, n):
        ans = 1
        for p in self.primes:
            pp = 1
            z = 1
            while n%p == 0:
                pp *= -p
                z += pp
                n //= p
            ans *= z
        return ans
        
    def sLess(self, limit):
        sumOver = self.factors[0]
        searchOver = self.factors[1]
        
        sumOver.sort(key = lambda x : abs(x))
        searchOver.sort(key = lambda x : abs(x))
        
        sumSearchOver = searchOver[:]
        for ix in range(1, len(searchOver)):
            sumSearchOver[ix] += sumSearchOver[ix-1]
        
        searchIndex = len(searchOver)-1
        ans = 0
        for x in sumOver:
            while searchIndex >= 0 and abs(searchOver[searchIndex]) > limit // abs(x):
                searchIndex -= 1
            if searchIndex < 0: break
            ans += x * sumSearchOver[searchIndex]
            
        return ans
        
        #if limit == 0: return 0
        #if limit == 1: return 1
        #if n == 1: return 1
        #
        #if limit >= n:
        #    if n in self.allCache:
        #        return self.allCache[n]
        #    self.allCache[n] = self.sumAllFactors(n)
        #    return self.allCache[n]
        #
        #key = (n, limit)
        #if key in self.cache:
        #    return self.cache[key]
        #
        #ix = 0
        #while n%self.primes[ix] != 0:
        #    ix += 1
        #    
        #p = self.primes[ix]
        #e = 0
        #while n%p == 0:
        #    e += 1
        #    n //= p
        #    
        #if p < 30:
        #    self.printDict[p] = log(limit) / log(10)
        #    self.printUpdate()
        #    
        #pp = 1
        #ans = 0
        #for ee in range(e+1):
        #    ans += (-1)**ee * pp * self.sLess(n, limit//pp)
        #    pp *= p
        #    
        #ans %= 10**9+7
        #
        #self.cache[key] = ans
        #return ans
        
    def S(self, nFact, lowerLimit, upperLimit):
        n = 1
        for x in range(2, nFact+1):
            n *= x
            
        self.primeFactorize(nFact)
        
        self.factors = [[1],[1]]
        for p in self.primes:
            #print p, [len(x) for x in self.factors]
            listIndex = 0 if len(self.factors[0]) < len(self.factors[1]) else 1
            pps = [(-p)**e for e in range(self.primeFactorization[p]+1) if p**e <= upperLimit]
            self.factors[listIndex] = [x*y for x in pps for y in self.factors[listIndex] if abs(x*y) <= upperLimit]
        #return [len(x) for x in self.factors]
        return (self.sLess(upperLimit) - self.sLess(lowerLimit-1))
        
    def primeFactorize(self, nFact):
        self.primeFactorization = defaultdict(int)
        for p in self.primes:
            pp = p
            while pp <= nFact:
                self.primeFactorization[p] += nFact // pp
                pp *= p
        
    def printUpdate(self):
        keys = self.printDict.keys()
        keys.sort()
        print '-------------------------------------------'
        print 'Cache size: {0}'.format(len(self.cache))
        for p in keys:
            print '{0} - {1}'.format(p, self.printDict[p])
        print '-------------------------------------------'
        print ''
        
if __name__ == '__main__':
    sol = Euler646()
    print sol.S(10, 100, 1000)
    print sol.S(15, 10**3, 10**5)
    print sol.S(30, 10**8, 10**12)
    print sol.S(70, 10**8, 10**12)
    x = sol.S(70, 10**20, 10**60)
    MOD = 10**9+7
    print '{0} = {1} MOD {2}'.format(x, x%MOD, MOD)