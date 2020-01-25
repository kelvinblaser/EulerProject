# Euler 264
# Kelvin Blaser     2019-02-26

from __future__ import division, print_function
from collections import defaultdict
from itertools import combinations
from math import sin, cos, atan2
import scipy as sp
from scipy.optimize import root
import six

VERBOSE = False

def sumSquares(N):
    ssqrs = defaultdict(list)
    r = int(1.1 * (N**0.5)) # Make a little buffer room here
    for x in range(r+1):
        if VERBOSE and x % 1000 == 0:
            l = len(ssqrs)
            print(f'Calculating sumSquares: x = {x}: len(ssqrs) = {l}')
        for y in range(x+1):
            n = x*x + y*y
            if n % 5 != 0: continue  # how to justify?
            if n > N: break
            ssqrs[n].append((x,y))
    return ssqrs

def ReflectPoints(points):
    points = set(points)
    points.update({(y,x) for x,y in points})
    points.update({(-x,y) for x,y in points})
    points.update({(x,-y) for x,y in points})
    return points

def GetTriangleFromPoint(x3,y3):
    r2 = x3*x3 + y3*y3
    def f(x):
        ret = sp.zeros(4)
        x1, y1, x2, y2 = x
        ret[0] = (x1-x3)*(x2-5) + (y1-y3)*y2
        ret[1] = (x2-x3)*(x1-5) + (y2-y3)*y1
        ret[2] = x1*x1 + y1*y1 - r2
        ret[3] = x2*x2 + y2*y2 - r2
        return ret

    def df(x):
        x1, y1, x2, y2 = x
        f = sp.zeros((4,4))
        f[0,0] = x2 - 5
        f[0,1] = y2
        f[0,2] = x1 - x3
        f[0,3] = y1 - y3
        f[1,0] = x2 - x3
        f[1,1] = y2 - y3
        f[1,2] = x1 - 5
        f[1,3] = y1
        f[2,0] = 2*x1
        f[2,1] = 2*y1
        f[3,2] = 2*x2
        f[3,3] = 2*y2
        return f

    return root(f, GetInitVector(x3, y3)).x


def GetInitVector(x3, y3):
    r = (x3*x3 + y3*y3)**0.5
    theta = atan2(y3/r, x3/r)
    sqrt3by2 = 3**0.5 / 2
    x1, y1 = -0.5, sqrt3by2
    x2, y2 = -0.5, -sqrt3by2
    x1, y1 = cos(theta)*x1 - sin(theta)*y1, sin(theta)*x1 + cos(theta)*y1
    x2, y2 = cos(theta)*x2 - sin(theta)*y2, sin(theta)*x2 + cos(theta)*y2
    x1, y1 = r*x1, r*y1
    x2, y2 = r*x2, r*y2
    return sp.array((x1, y1, x2, y2))


def isQualifyingTriangle(triangle):
    p1, p2, p3 = triangle
    #if p1 == p2 or p2 == p3 or p1 == p3:
    #    return False
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    #if x1*x1 + y1*y1 != x2*x2 + y2*y2:
    #    return False
    #if x1*x1 + y1*y1 != x3*x3 + y3*y3:
    #    return False
    if (x2 - x1)*(x3 - 5) + (y2 - y1)*y3 != 0:
        return False
    if (x1 - x3)*(x2 - 5) + (y1 - y3)*y2 != 0:
        return False
    return True

def Perimeter(triangle):
    p1, p2, p3 = triangle
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    p = ((x3-x2)**2 + (y3-y2)**2)**0.5
    p += ((x2-x1)**2 + (y2-y1)**2)**0.5
    p += ((x1-x3)**2 + (y1-y3)**2)**0.5
    return p

def SumPerimetersOfTriangles(N):
    ssqrs = sumSquares(N*N / 27.0)
    sum_perimeters = 0.0
    r2_last = -1
    r2s = set()
    for r2, points in six.iteritems(ssqrs):
        if r2 < 25: continue
        if len(points) < 2: continue
        if VERBOSE and r2 // 100000 > r2_last:
            r2_last = r2 // 100000
            print(f'Iterating through triangles: r2 = {r2}')
        triangles = set()
        #for x3,y3 in ReflectPoints(points):
        #    x1, y1, x2, y2 = GetTriangleFromPoint(x3, y3)
        #    x1, y1, x2, y2 = int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2))
        #    triangle = tuple(sorted([(x1, y1), (x2, y2), (x3, y3)]))
            #print(triangle, isQualifyingTriangle(triangle))
        # for triangle in combinations(ReflectPoints(points), 3):
        #     if isQualifyingTriangle(triangle):
        #         triangles.add(triangle)
        #         r2s.add((r2, len(points)))
        points = ReflectPoints(points)
        for (x1, y1), (x2, y2) in combinations(points, 2):
            x3 = 5 - x1 - x2
            y3 = -y1 - y2
            if x3*x3 + y3*y3 == r2:
                triangles.add(tuple(sorted([(x1, y1),(x2,y2),(x3,y3)])))
        for triangle in triangles:
            #(x1, y1), (x2, y2), (x3, y3) = triangle
            #print(triangle, x1+x2+x3, y1+y2+y3)
            p = Perimeter(triangle)
            if p <= N and triangle[1] != triangle[2]:
                sum_perimeters += p
    #for r2, l in sorted(r2s):
    #    print(r2, l)
    return sum_perimeters


if __name__ == '__main__':
    domain = [50, 100, 1000, 100000]
    for N in domain:
        if N == domain[-1]:
            VERBOSE = True
        p = SumPerimetersOfTriangles(N)
        print(f'N = {N}: Sum of perimeters = {p}')
