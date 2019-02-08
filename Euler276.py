# Euler 276
# Kelvin Blaser     2019.02.07

from Primes import MakePrimeList

class PrimitiveTriangles:
    def __init__(self, pMax):
        self.pMax = pMax
        self.trianglesWithPerimeterLess = self.calcTrianglesWithPerimeterLess()
        self.mu = self.calcMu()

    def calcTrianglesWithPerimeterLess(self):
        T = [0]*(self.pMax+1)
        for p in range(3, len(T)):
            if p%2 == 0:
                T[p] = T[p-1] + (p**2 + 24) // 48
            else:
                T[p] = T[p-1] + ((p+3)**2 + 24) // 48
        return T

    def calcMu(self):
        primes = MakePrimeList(self.pMax)
        mu = [1]*(self.pMax+1)
        for p in primes:
            for x in range(p, len(mu), p):
                mu[x] *= -1
            for x in range(p*p, len(mu), p*p):
                mu[x] = 0
        return mu

    def trianglesLess(self, p):
        return self.trianglesWithPerimeterLess[p]

    def primitiveTrianglesLess(self, N):
        return sum( self.mu[x] * self.trianglesLess(N//x) for x in range(1, N) )


if __name__ == '__main__':
    sol = PrimitiveTriangles(10000000)
    print sol.trianglesLess(10**7)
    print 'Triangles Calculated'
    print 'Primitive Triangles with Perimeter Less than {0} : {1}'.format('10^7', sol.primitiveTrianglesLess(10**7))
