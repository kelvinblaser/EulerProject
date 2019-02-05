# Euler 653
# Kelvin Blaser		2019.01.29
#
# Imagine the marbles simply passing through each other instead of colliding.
# Calculate the distance each marble has to travel. 
# In reality, the marble closest to the end exits first, second closest exits second, etc.
# 
# Algoritm:
#	1. Make a list of exit distances
#	2. Sort them
#	3. Query for the (N-j)th exit distance.

import EulerUnitTest as eut

class Euler653:
    def __init__(self, L, N):
        self.N = N
        self.L = L
        self.gaps = self.calcGaps()
        self.positions = self.calcPositions()
        self.distances = self.calcDistancesTraveled()
        
    def calcGaps(self):
        g = []
        r = 6563116
        for _ in range(self.N):
            g.append(r)
            r = (r*r)%32745673
        return g
    
    def calcPositions(self):
        p = [(g%1000)+1 for g in self.gaps]
        p[0] += 10
        for i in range(1, len(p)):
            p[i] += p[i-1] + 20
        return p
        
    def calcDistancesTraveled(self):
        westwardOnLeft = 0
        distances = []
        for i in range(self.N-1, -1, -1):
            if self.gaps[i] > 10000000:
                d = self.positions[i] + self.L - 20
                d -= 20 * (i + westwardOnLeft)
                distances.append(d)
                westwardOnLeft += 1
            else:
                d = self.L - self.positions[i] - 20 * westwardOnLeft
                distances.append(d)
        distances.sort()
        return distances
        
    def d(self, j):
        return self.distances[self.N - j]
        
        
if __name__ == '__main__':
    sol = Euler653(5000, 3)
    print 'N = {0}, L = {1}'.format(sol.N, sol.L)
    print 'Gaps : {0}'.format(sol.gaps)
    print 'Positions : {0}'.format(sol.positions)
    print 'Distances : {0}'.format(sol.distances)
    print 'd(5000, 3, 2) = {0}'.format(eut.testAssert(sol.d, 5519, 2))
    sol = Euler653(10000, 11)
    print 'd(10 000, 11, 6) = {0}'.format(eut.testAssert(sol.d, 11780, 6))
    sol = Euler653(100000, 101)
    print 'd(100 000, 101, 51) = {0}'.format(eut.testAssert(sol.d, 114101, 51))
    sol = Euler653(1000000000, 1000001)
    print 'd(1 000 000 000, 1 000 001, 500 001) = {0}'.format(sol.d(500001))
    