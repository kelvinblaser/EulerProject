# Euler 252 - Convex Holes
#  Kelvin Blaser
#  2019.1.28
# Get points
# Depth first seach by building convex polygons triangle by triangle

import matplotlib.pyplot as plt
            
def squareNorm(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return (x2-x1)**2 + (y2-y1)**2
    
def crossProd(v, p1, p2):
    dx1, dy1 = p1[0] - v[0], p1[1] - v[1]
    dx2, dy2 = p2[0] - v[0], p2[1] - v[1]
    return dx1*dy2 - dx2*dy1
    
def calcArea(poly):
    A = 0
    for i in range(2, len(poly)):
        A += hero(poly[0], poly[i-1], poly[i])
    return A
    
def hero(p0,p1,p2):
    return abs(p0[0]*(p1[1]-p2[1]) + p1[0]*(p2[1]-p0[1]) + p2[0]*(p0[1]-p1[1]))

class ConvexHoleDFS:
    def __init__(self, n, talk=False):
        self.talk = talk
        self.fig = plt.figure(n)
        self.points = self.makePoints(n)
        self.points.sort()
        self.maxArea = 0
        self.maxPoly = []
        self.polygonsAnalyzed = 0
        
    def makePoints(self, n):
        s = 290797
        points = []
        for _ in range(n):
            s = (s*s)%  50515093
            x = (s%2000) - 1000
            s = (s*s) % 50515093
            y = (s%2000) - 1000
            points.append((x,y))
        return points
    
    def solve(self):
        for n,p in enumerate(self.points):
            self.n = n
            plt.clf()
            self.plotState()
            poly = [p]
            candidates = set(self.points[n+1:])
            self.dfs(poly, candidates)
            
        self.n += 1
        plt.clf()
        self.plotState()
        return self.maxArea / 2.0
        
    def plotPoints(self, color='b', points=None):
        if not points:
            points = self.points
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        plt.plot(x,y, 'o'+color, markersize=6)
        
    def plotPoly(self, poly, color):
        if len(poly) < 2: return
        x = [p[0] for p in poly] + [poly[0][0]]
        y = [p[1] for p in poly] + [poly[0][1]]
        plt.plot(x,y, color) 
        
    def plotState(self, title=None):
        if not title:
            title = 'Max Area: {0}'.format(self.maxArea/2.0)
        plt.title(title, fontsize=24)
        plt.xlabel('{0} initial point{1} analyzed\n{2} Polygon{1} analyzed'.format(self.n, '' if self.n == 1 else 's', self.polygonsAnalyzed),
                   fontsize=20)
        self.plotPoints(color='y')
        self.plotPoints(color='b', points = self.points[:self.n])
        self.plotPoly(self.maxPoly, 'g')
        plt.show(block=False)
        plt.pause(0.1)
        
    def dfs(self, poly, candidates):
        # Pre-condition: All points in candidates are to the left of each directed
        # line segment p[i]->p[i+1] in poly.  None of them are to the left of
        # p[-1]->p[0]
        for p in candidates:
            if len(poly) == 1:
                # We definitely want to consider all p
                newCandidates = set(q for q in candidates if crossProd(poly[0], p, q) > 0)
                self.dfs(poly + [p], newCandidates)
                continue
                
            # Guaranteed to be convex if all candidates are to the left of each
            # directed line segment except the one connecting the last point
            # to the first.  We just need to check if any of the other candidates
            # are inside the new polygon
            for q in candidates:
                if crossProd(poly[-1], p, q) > 0 and crossProd(p, poly[0], q) > 0:
                    # p does not make a convex hole
                    break
            else:
                # p does make a convex hole
                A = calcArea(poly + [p])
                self.polygonsAnalyzed += 1
                maxChange = False
                if A > self.maxArea:
                    self.maxArea = A
                    self.maxPoly = poly + [p]
                    maxChange = True
                if self.talk or maxChange:
                    plt.clf()
                    title = 'Current Area: {0} \n Max Area: {1}'.format(A/2.0, self.maxArea/2.0)
                    self.plotPoly(poly+[p], 'r')
                    self.plotState(title)
        
                newCandidates = set(q for q in candidates if crossProd(poly[-1], p, q) > 0)
                self.dfs(poly + [p], newCandidates)
                    
            
        
    
    
        
if __name__ == '__main__':
    sol = ConvexHoleDFS(20, True)
    print 'First few points: {0}, {1}, {2} ...'.format(*sol.points[:3])
    print 'Cross prod of first three points: {0}'.format(crossProd(*sol.points[:3]))
    print ''
    print 'DFS Initialization'
    print 'Num points: {0}'.format(len(sol.points))
    print 'Area for first {0} points: {1}'.format(20, sol.solve())
    print 'Polygon for first {0} point: {1}'.format(20, sol.maxPoly)
    print ''
    sol = ConvexHoleDFS(500, False)
    print 'Num points: {0}'.format(len(sol.points))
    print 'Area for first {0} points: {1}'.format(500, sol.solve())
    print 'Polygon for first {0} point: {1}'.format(500, sol.maxPoly)
    