# Euler 618
# Kelvin Blaser		2019.01.29

from Primes import MakePrimeList
import EulerUnitTest as eut
import sys

class Euler618:
    def __init__(self):
        self.MOD = 10**9
        self.fibs = self.makeFibonacci()
        self.primes = MakePrimeList(self.fibs[-1])
        self.s = self.dynamicSolution()
        
    def makeFibonacci(self):
        f = [0,1]
        for x in range(2, 25):
            f.append(f[-1]+f[-2])
        return f
        
    def dynamicSolution(self):
        s = [0] * (self.fibs[-1]+1)
        s[0] = 1
        last = 0
        print 'Calculating Dynamic Solution: {0}%'.format(last)
        for pix,p in enumerate(self.primes):
            percent = (100*pix) // len(self.primes)
            if percent > last:
                print 'Calculating Dynamic Solution: {0}%'.format(percent)
                last = percent
            for k in range(p, self.fibs[-1]+1):
                s[k] += p*s[k-p]
                s[k] %= self.MOD
        return s
        
    def S(self, k, maxPrimeIx=None):
        return self.s[k]
        
    def sumS(self):
        ans = 0
        for f in self.fibs[2:]:
            ans += self.S(f)
            ans %= self.MOD
        return ans
            
        
if __name__ == '__main__':
    sol = Euler618()
    print 'Fibonacci : {0}'.format(' '.join(str(f) for f in sol.fibs))
    print 'Num Primes : {0}'.format(len(sol.primes))
    print 'S(1) = {0}'.format(eut.testAssert(sol.S, 0, 1))
    print 'S(2) = {0}'.format(eut.testAssert(sol.S, 2, 2))
    print 'S(3) = {0}'.format(eut.testAssert(sol.S, 3, 3))
    print 'S(5) = {0}'.format(eut.testAssert(sol.S, 11, 5))
    print 'S(8) = {0}'.format(eut.testAssert(sol.S, 49, 8))
    print 'Sum(S(F_k) for k = 2..24) = {0}'.format(sol.sumS())