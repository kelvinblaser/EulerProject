# Euler 241 - Perfection Quotients

from Primes import MakePrimeList
from collections import defaultdict
from fractions import Fraction

class Euler241:
    def __init__(self, pMAX):
        self.PMAX = pMAX  # Just a guess that no primes > PMAX will be used
        self.primes = MakePrimeList(self.PMAX)
        self.factorization = {}
        self.solutions = set()
        
    def __call__(self, N):
        p2 = 2
        while p2 <= N:
            #print p2
            self.findSolution(p2, Fraction(2*p2-1, p2), N, [2])
            p2 *= 2 # only odd powers of 2?
        return sum(x[0] for x in self.solutions if x[0] <= N)
        
    def findSolution(self, x, pq, N, primesTried):
        if pq.denominator == 2:
            self.solutions.add((x, pq))
            self.printSolutions()
            return # No odd numbers with integer perfection quotient?
        if pq.denominator % 2 == 1:
            return # Already got rid of our twos
        if x*pq.denominator > N*2*self.primes[-1]:
            return # Haven't gotten to N, but can't clear the denominator before we get there
        
        primesToTry = self.factorize(pq.numerator).keys()
        
        newPrimesTried = set(primesTried)
        for p in primesToTry:
            if p in primesTried or p > self.PMAX:
                continue
            newPrimesTried.add(p)   
            pp = p
            while x*pp <= N:
                npq = pq*Fraction(pp*p - 1, pp*(p-1))
                self.findSolution(x*pp, npq, N, newPrimesTried)
                pp *= p
                
    def maxPrime(self, n):
        f = self.factorize(n)
        return max(f.keys())
                
    def printSolutions(self):
        numSols = len(self.solutions)
        plural = '' if numSols == 1 else 'S'
        print '{0} SOLUTION{1} FOUND'.format(numSols, plural)
        sols = list(self.solutions)
        sols.sort()
        for x in sols:
            f = self.factorize(x[0])
            fstr = ''
            keys = list(f.keys())
            keys.sort()
            for k in keys:
                fstr += '{0}^{1} '.format(k, f[k])
            print '{0:>30}: {1:>4}\t{2}'.format(x[0], x[1], fstr)
        
        print '---------------------------------------------------------'
            
        
    def factorize(self, n):
        #try:
        #    return self.factorization[n]
        #except KeyError:
        #    pass
        
        factorization = {}
        x = n
        for p in self.primes:
            if p*p > n: break
            if n%p != 0: continue
            e = 0
            while n%p == 0:
                e += 1
                n //= p
            factorization[p] = e
        if n > 1: factorization[n] = 1
        #self.factorization[x] = factorization
        return factorization
        
    #def calculatePrimePowers(self, N):
    #    self.primePowers = {}
    #    for p in self.primes:
    #        self.primePowers[p] = [(1, (1,1))]
    #        pp = p
    #        while pp <= N:
    #            self.primePowers[p].append((pp, ((pp*p-1) // (p-1),pp)))
    #            pp *= p
    #    self.primePowerNumerators = defaultdict(dict)
    #    for p in self.primes:
    #        for pp, (num, den) in self.primePowers[p]:
    #            factorization = self.factorize(num)
    #            for q in factorization.keys():
    #                if q > self.PMAX: continue
    #                if not p in self.primePowerNumerators[q]:
    #                    self.primePowerNumerators[q][p] = []
    #                self.primePowerNumerators[q][p].append((pp, factorization[q]))
if __name__ == '__main__':
     e = Euler241(1000000)
     print e(10**30)