# Euler 650
#
# Solution is O(n^2 / log(n)) - Not sure if I can make it faster

from Primes import MakePrimeList
from collections import defaultdict

class DivisorsBinomial:
    def __init__(self, n, MOD):
        self.primes = MakePrimeList(n)
        self.n = n
        self.MOD = MOD
        self.calculateFactorials()
        self.calculateBinomials()
        self.calculateDivisors()
        self.sumDivisors()
        
    def calculateFactorials(self):
        fact = [defaultdict(int) for _ in range(self.n+1)]
        for p in self.primes:
            pp = p
            while pp <= self.n:
                for x in range(pp, self.n+1):
                    fact[x][p] += x//pp
                pp *= p
        self.factorials = fact
    
    def printFactorials(self):
        for x in range(len(self.factorials)):
            print '  {0}! = {1}'.format(x, self.primeFactString(self.factorials[x]))
            
    def primeFactString(self, primeFactDict):
        primes = list(primeFactDict.keys())
        if len(primes) == 0:
            return '1'
        primes.sort()
        primeStrings = ['{0}^{1}'.format(p, primeFactDict[p]) for p in primes if primeFactDict[p] != 0]
        return ' '.join(primeStrings)
        
    def calculateBinomials(self):
        binom = [defaultdict(int) for _ in range(self.n+1)]
        denom = defaultdict(int)
        for x in range(self.n+1):
            numer = defaultdict(int)
            for p in self.factorials[x].keys():
                numer[p] = (x+1) * self.factorials[x][p]
                denom[p] += 2 * self.factorials[x][p]
                binom[x][p] = numer[p] - denom[p]
        self.binomialProducts = binom
        
    def printBinomials(self):
        for x in range(len(self.binomialProducts)):
            print '  B({0}) = {1}'.format(x, self.primeFactString(self.binomialProducts[x]))
            
    def B(self, x):
        pf = self.binomialProducts[x]
        b = 1
        for p in pf:
            if pf[p] == 0: continue
            b *= pow(p, pf[p], self.MOD)
            b %= self.MOD
        return b
        
    def calculateDivisors(self):
        divs = [1 for _ in range(self.n+1)]
        for x in range(self.n+1):
            pf = self.binomialProducts[x]
            num, den = 1,1
            for p in pf:
               if pf[p] == 0: continue
               num *= pow(p, pf[p] + 1, self.MOD) - 1
               den *= p - 1
               num %= self.MOD
               den %= self.MOD
            divs[x] = num * pow(den, self.MOD - 2, self.MOD)
            divs[x] %= self.MOD                
        self.binomialProductDivisorSums = divs
        
    def printDivisors(self):
        for x in range(len(self.binomialProductDivisorSums)):
            print '  D({0}) = {1} MOD {2}'.format(x, self.binomialProductDivisorSums[x], self.MOD)
            
    def D(self, n):
        return self.binomialProductDivisorSums[n]
        
    def sumDivisors(self):
        sDivs = self.binomialProductDivisorSums[:]
        for x in range(2, self.n+1):
            sDivs[x] += sDivs[x-1]
            sDivs[x] %= self.MOD
        self.sumDivisors = sDivs
        
    def printSums(self):
        for x in range(len(self.sumDivisors)):
            print '  S({0}) = {1} MOD {2}'.format(x, self.sumDivisors[x], self.MOD)
        
    def S(self, n):
        if n > self.n:
            self = DivisorsBinomial(n, self.MOD)
        return self.sumDivisors[n]
    
if __name__ == '__main__':
    db = DivisorsBinomial(7, 10**9 + 7)
    print 'db.n =', db.n
    print 'db.MOD =', db.MOD
    print 'db.primes =', db.primes
    print ' '
    print '  db.factorials  '
    print '-----------------'
    db.printFactorials()
    print ' '
    print '  db.binomialProducts  '
    print '-----------------------'
    db.printBinomials()
    print ' '
    print '  db.binomialProductDivisorSums  '
    print '---------------------------------'
    db.printDivisors()
    print ' '
    print '  db.sumDivisors  '
    print '------------------'
    db.printSums()
    print ' '
    
    print 'B(5) =', db.B(5)
    print 'D(5) =', db.D(5)
    print 'S(5) =', db.S(5)
    print 'S({0}) = {1} MOD {2} ({3} = {4} MOD {2})'.format(10, db.S(10), db.MOD, 141740594713218418L, 141740594713218418 % db.MOD)
    print 'S({0}) = {1} MOD {2}'.format(100, db.S(100), db.MOD)
    print 'S({0}) = {1} MOD {2}'.format(20000, db.S(20000), db.MOD)