# Euler 362
# Kelvin Blaser     2019.02.11

from Primes import MakePrimeList, Mobius, intRoot

class SquareFreeFactorize:
    def __init__(self, N, talk=False):
        self.talk = talk
        self.N = N
        self.r = intRoot(N)
        self.primes = MakePrimeList(self.r)
        self.mobius = Mobius(self.r)
        self.isSquareFree = self.makeSquareFree(self.r)
        self.factCache = {}
        self.sfCache = {}

    def makeSquareFree(self, r):
        sf = [True]*(r+1)
        for x in range(2,intRoot(r)+1):
            for y in range(x*x, r+1, x*x):
                sf[y] = False
        return sf

    def countFactorizations(self, n, fMin=2):
        if (n, fMin) in self.factCache:
            return self.factCache[(n, fMin)]

        ans = self.countSquareFree(n) - self.countSquareFree(fMin-1)
        for f in range(fMin, intRoot(n)+1):
            if self.isSquareFree[f]:
                ans += self.countFactorizations(n//f, f)
        self.factCache[(n, fMin)] = ans

        if self.talk and fMin == 2:
            print 'S({0}) = {1}'.format(n, ans)
        return ans

    def countSquareFree(self, n):
        if n in self.sfCache:
            return self.sfCache[n]

        ans = sum(self.mobius(x)* (n // (x*x)) for x in range(1, intRoot(n)+1))
        self.sfCache[n] = ans
        return ans

if __name__ == '__main__':
    sol = SquareFreeFactorize(100)
    print 'SquareFree : [{0}]'.format(', '.join(['T' if sol.isSquareFree[x] else 'F' for x in range(11)]))
    print 'Mobius : {0}'.format(sol.mobius.memVec)
    print 'CountSquareFree(100) = {0}'.format(sol.countSquareFree(100))
    print 'S(100) = {0}'.format(sol.countFactorizations(100))
    sol = SquareFreeFactorize(10**10, talk=True)
    print 'S(10^10) = {0}'.format(sol.countFactorizations(10**10))
    print 'Factorization Cache Size : {0}'.format(len(sol.factCache))
    print 'SquareFree Cache Size : {0}'.format(len(sol.sfCache))
