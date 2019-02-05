# Euler 102 - Origin in the triangle

import pylab

class Point:
    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def strPoint(self):
        return '('+str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

def makeLineFunc(p1,p2):
    if not p1.x == p2.x:
        m = (p1.y-p2.y)/float(p1.x-p2.x)
        b = p1.y - m * p1.x
    else:
        return -1

    def f(p):
        return m*p.x+b
    
    return f

def thirdPointSameSideAsOrigin(p1, p2, p3):
    o = Point(0,0,0)
    line = makeLineFunc(p1,p2)
    if line == -1:
        t = Triangle(p1,p2,p3)
        t.printTriangle()
        return False
    if line(o) > 0 and line(p3) > p3.y:
        return True
    if line(o) < 0 and line(p3) < p3.y:
        return True
    return False

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def containsOrigin(self):
        if (thirdPointSameSideAsOrigin(self.p1,self.p2,self.p3) and
            thirdPointSameSideAsOrigin(self.p1,self.p3,self.p2) and
            thirdPointSameSideAsOrigin(self.p3,self.p2,self.p1) ):
            return True
        return False

    def printTriangle(self):
        print '[' + self.p1.strPoint() + ';' + self.p2.strPoint() + ';' + self.p3.strPoint() + ']'

    def plotTriangle(self):
        x = [self.p1.x, self.p2.x, self.p3.x, self.p1.x]
        y = [self.p1.y, self.p2.y, self.p3.y, self.p1.y]
        pylab.plot(x,y)
        xaxis = [-1000,0,1000]
        zero = [0,0,0]
        pylab.plot(xaxis,zero,'k')
        pylab.plot(zero,xaxis,'k')
        pylab.plot([0],[0],'ro')
        

def convertLineToTriangle(liner):
    # Parse Line
    numbers = []
    line = liner[:]
    for c in line:
        if c == ',':
            numbers.append(int(line[0:line.index(c)]))
            line = line[line.index(c)+1:]
    numbers.append(int(line))
    # Create Points
    p1 = Point(numbers[0],numbers[1])
    p2 = Point(numbers[2],numbers[3])
    p3 = Point(numbers[4],numbers[5])
    # Create Triangle
    triangle = Triangle(p1,p2,p3)

    return triangle

def readTriangles(filename):
    f = open(filename)
    triangles = []
    for line in f:
        triangles.append(convertLineToTriangle(line))

    f.close()
    return triangles

def countTrianglesContainingOrigin(filename):
    count = 0
    triangles = readTriangles(filename)

    for t in triangles:
        if t.containsOrigin():
            count += 1

    return count    



    
    
