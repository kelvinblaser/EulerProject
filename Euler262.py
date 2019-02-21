# Euler 262
# Kelvin Blaser     2019-02-20
#
# Plotting this function in the specified area shows a few things.
# The area is a 'volcano', there's a mountain with a depression in the middle.
# The elevation is symmetric about the line y=x  (Easily seen from the formula)
# There are two paths from A to B.
#   1. Through the pass and through the depression along the line y = x
#   2. Around the mountain.
# The path around the mountain has the lowest maximum height.
# That height is the heighest point along the line y = 0 (or x = 0)
# Denote this point x0, with height h(x0)
#
# Here is the path:
#   1. Fly up from point A to height h(x0) at (200, 200)
#   2. Fly in a straight line tangent to contour h = h(x0)
#   3. Fly counter-clockwise along the contour h = h(x0) until (1400, 1400) is
#       in line of sight
#   4. Fly in a straight line tangent to contour h = h(x0) to (1400, 1400)
#   5. Fly down to point B

import numpy as np
from scipy.optimize import minimize_scalar, newton
import matplotlib.pyplot as plt

class Euler262:
    def __init__(self):
        self.A = (200, 200)
        self.B = (1400, 1400)
        self.x, self.y = np.meshgrid(range(1601), range(1601))
        self.z = self.height(self.x, self.y)
        self.contourHeight, self.contourMinY = self.calcContourHeight()
        self.contourEntry = self.calcContourEntry()
        self.contourExit = self.calcContourExit()
        self.contourX, self.contourY = self.calcContour()
        self.numPoints = 200000
        self.contourL = self.contourLength(self.numPoints)
        self.firstL = ((200-self.contourEntry[0])**2 + (200-self.contourEntry[1])**2)**0.5
        self.lastL  = ((1400-self.contourExit[0])**2 + (1400-self.contourExit[1])**2)**0.5
        self.pathL = self.firstL + self.contourL + self.lastL

    def height(self, x, y):
        return self.a(x,y) * np.exp( -abs(self.g(x,y)) )

    def grad(self, x, y):
        return (self._grad(x,y), self._grad(y,x))

    def _grad(self, x, y):
        return (self.aDer(x,y) - self.a(x,y) * self.gDer(x,y) ) * np.exp(-self.g(x,y))

    def a(self, x,y):
        return 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y)

    def g(self, x, y):
        return 0.000001*(x*x+y*y)-0.0015*(x+y)+0.7

    def aDer(self, x, y):
        return -0.005*(2*x + y) + 12.5

    def gDer(self, x, y):
        return 0.000002*x - 0.0015

    def calcContourHeight(self):
        res = minimize_scalar(lambda x : -self.height(x,0), bracket=(0,500,1600))
        return self.height(res.x, 0), (res.x, 0)

    def calcContourEntry(self):
        y0 = 50
        yf = newton(lambda y : self.rootFunc(y, 600, self.A), x0 = y0)
        return (self.xOnContour(yf, self.contourHeight, 600,), yf)

    def calcContourExit(self):
        y0 = 885
        yf = newton(lambda y : self.rootFunc(y, 1535, self.B), x0 = y0)
        return (self.xOnContour(yf, self.contourHeight, 1535,), yf)

    def rootFunc(self, yguess, x0, AB):
        xguess = self.xOnContour(yguess, self.contourHeight, x0)
        gx, gy = self.grad(xguess,yguess)
        return gx*(AB[0] - xguess) + gy*(AB[1] - yguess)

    def calcContour(self, numPoints = 1000):
        h = self.contourHeight
        scY = np.linspace(-self.contourEntry[1], self.contourExit[1], numPoints)
        cY = np.abs(scY)
        cX = 0 * cY
        cX[0] = self.contourEntry[0]
        for i,y in enumerate(cY):
            if i == 0: continue
            d = np.sign(scY[i]) * 100
            cX[i] = self.xOnContour(y, h, cX[i-1]+d)
        return cX, cY

    def xOnContour(self, y, h, x0):
        res = newton(lambda x : self.height(x,y)-h, x0 = x0)
        return res

    def contourLength(self, numPoints = 1000):
        cX, cY = self.calcContour(numPoints)
        for i in range(len(cX)-1):
            cX[i] = cX[i+1] - cX[i]
            cY[i] = cY[i+1] - cY[i]
        arc = np.sqrt(cX*cX + cY*cY)
        arc[len(arc)-1] = 0
        return sum(arc)

    def plot(self):
        fig = plt.figure('Volcano')
        plt.clf()

        plt.contour(self.x, self.y, self.z, 30)
        x = [self.A[0], self.B[0], self.contourEntry[0], self.contourExit[0]]
        y = [self.A[1], self.B[1], self.contourEntry[1], self.contourExit[1]]
        pathX = [200] + [val for val in self.contourX] + [1400]
        pathY = [200] + [val for val in self.contourY] + [1400]
        plt.plot(x,y, 'ob')
        plt.plot(pathX, pathY, 'r')

        xStr = 'x - Path Length Calculated with {0} Points'.format(self.numPoints)
        xStr += '\nContour Entry : {0}'.format(pointStr(self.contourEntry))
        xStr += '\nContour Exit  : {0}'.format(pointStr(self.contourExit))
        xStr += '\nContour Height: {0:.2f}'.format(self.contourHeight)
        plt.xlabel(xStr)
        plt.ylabel('y')
        titleStr = 'Path Length : {0:.4f} + {1:.4f} + {2:.4f} = {3:.3f}'
        titleStr = titleStr.format(self.firstL, self.contourL, self.lastL, self.pathL)
        plt.title(titleStr)
        plt.axis('square')

        plt.show()

def pointStr(x):
    return '({0:.3f}, {1:.3f})'.format(*x)

if __name__ == '__main__':
    sol = Euler262()
    corners = [(0,0), (0,1600), (1600, 0), (1600, 1600)]
    hStr = '\n\t'.join(['h{0} = {1}'.format(p, sol.height(*p)) for p in corners])
    print 'Heights at corners:\n\t{}'.format(hStr);

    en = pointStr(sol.contourEntry)
    ex = pointStr(sol.contourExit)
    print 'Contour Entry Point : (x,y) = {0}'.format(en)
    print 'Contour Exit Point  : (x,y) = {0}'.format(ex)
    print 'Contour height : h{0} = {1}'.format(en, sol.contourHeight)

    for numPoints in [100, 1000, 10000, 100000, 200000]:
        print 'Contour Length calculated from {0} points :\t{1}'.format(numPoints, sol.contourLength(numPoints))

    print ''
    print 'First Leg from {0} to {1} : {2:.4f}'.format(sol.A, en, sol.firstL)
    print 'Contour Leg from {0} to {1} : {2:.4f}'.format(en, ex, sol.contourL)
    print 'Last Leg from {0} to {1} : {2:.4f}'.format(ex, sol.B, sol.lastL)
    print 'Total path length : {0:.3f}'.format(sol.pathL)
    sol.plot()
