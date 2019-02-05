################################################################################
# Project Euler - Combined Volume of Cuboids
# projecteuler.net/problem=212
# Kelvin Blaser    2014.11.24
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Gets the right answer when comparing each cuboid to all of the cuboids. But it
# take s half hour.
# I tried speeding things up by sorting the cuboids by the length of their
# inner corner, and then using a bisection method to reduce the number of
# comparisons required.  For some reason this produces a wrong answer.  Not sure
# why.  Perhaps I'm not thinking about the limiits correctly.
#
# A better approach (found in the Project Euler forum) would be to partition the
# space into 400x400x400 chunks.  Then each cuboid would only intersect with at
# most 8 chunks.  8N comparisons there as opposed to N(N-1)/2 for my way.  Then
# use inclusion-exclusion on each of the chunks.  Let M be the size of the total
# grid and m be the maximum size of a side of a cuboid.  There are ((M+1)/m)^3
# chunks, each with on average CN / ((M+1)/m))^3 cuboids which intersect.  C is
# some factor to account for cuboids which intersect with more than 1 (but less
# than or equal to 8) chunks.  The total comparisons for the inclusion-exclusion
# part is ((M+1)/m)^3 * 2^(CN/((M+1)/m))^3)
################################################################################

from Euler import laggedFibonacci
from itertools import combinations
from bisect import bisect_left, bisect_right, insort

class Cuboid():
    def __init__(self,x,y,z,dx,dy,dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.c1 = (x,y,z)
        self.c2 = (x+dx, y+dy, z+dz)
        self.r1 = sum(k*k for k in self.c1)**0.5
        self.r2 = sum(k*k for k in self.c2)**0.5
        self.volume = dx*dz*dy

    def __str__(self):
        x1,y1,z1 = self.c1
        x2,y2,z2 = self.c2
        s = ('Cuboid with opposite corners at (%d,%d,%d) and (%d,%d,%d)'
             '\tVolume: %d'%(x1,y1,z1, x2,y2,z2, self.volume))
        return s
    def __repr__(self):
        return self.__str__()

    # Suite of ordering properties
    def __eq__(self, other): return self.r1 == other.r1
    def __ne__(self, other): return self.r1 != other.r1
    def __lt__(self, other): return self.r1 < other.r1
    def __le__(self, other): return self.r1 <= other.r1
    def __gt__(self, other): return self.r1 > other.r1
    def __ge__(self, other): return self.r1 >= other.r1

def cuboidGen(N,MOD_CORNER=10000, MOD_SIZE=399):
    lfg = laggedFibonacci(N*6)
    for i in range(N):
        try:
            x,y,z,dx,dy,dz = (next(lfg) for i in range(6))
        except StopIteration:
            print 'Something wrong with laggedFibonacci generator lfg'
        x,y,z = x%MOD_CORNER, y%MOD_CORNER, z%MOD_CORNER
        dx,dy,dz = dx%MOD_SIZE, dy%MOD_SIZE, dz%MOD_SIZE
        yield Cuboid(x,y,z,dx+1,dy+1,dz+1)
    return

def doCuboidsIntersect(a,b):
    ax1,ay1,az1 = a.c1
    ax2,ay2,az2 = a.c2
    bx1,by1,bz1 = b.c1
    bx2,by2,bz2 = b.c2
    if (ax1 >= bx2 or bx1 >= ax2 or
        ay1 >= by2 or by1 >= ay2 or
        az1 >= bz2 or bz1 >= az2):
        return False
    return True

def _CuboidIntersect(a,b):
    ''' Returns a Cuboid which represents the intersection of cuboids a and b
        If the intersection is empty, it returns a cuboid with 0 volume and
        and undefined position'''
    ax1,ay1,az1 = a.c1
    ax2,ay2,az2 = a.c2
    bx1,by1,bz1 = b.c1
    bx2,by2,bz2 = b.c2
    x1,x2 = max(ax1,bx1), min(ax2,bx2)
    y1,y2 = max(ay1,by1), min(ay2,by2)
    z1,z2 = max(az1,bz1), min(az2,bz2)
    dx = max(0,x2-x1)
    dy = max(0,y2-y1)
    dz = max(0,z2-z1)
    return Cuboid(x1,y1,z1,dx,dy,dz)

def cuboidIntersectVolume(c):
    if isinstance(c,Cuboid):
        return c.volume
    return reduce(_CuboidIntersect, c).volume

def searchIx(cuboids, r1Min, r1Max):
    top = len(cuboids)-1
    bottom = 0
    while top - bottom > 1:
        mid = (top+bottom)//2
        if cuboids[mid].r1 < r1Min:
            bottom = mid
        else:
            top = mid
    ix = top
    top = len(cuboids)-1
    bottom = 0
    while top - bottom > 1:
        mid = (top+bottom)//2
        if cuboids[mid].r1 > r1Max:
            top = mid
        else:
            bottom = mid
    return ix,bottom

def sortedInsert(cuboids, c):
    top = len(cuboids)-1
    bottom = 0
    while top - bottom > 1:
        mid = (top+ bottom)//2
        if cuboids[mid].r1 > c.r1:
            top = mid
        else:
            bottom = mid
    return cuboids[:top]+[c,]+cuboids[top:]

def Euler212(N):
    cuboids = []
    V = 0
    maxSize = 400
    drMax = 4*3**0.5 * maxSize  # 400 is largest one side can be
    rMax = 0
    for n,c1 in enumerate(cuboidGen(N)):
        V += c1.volume
        if n == 0:
            cuboids.append(c1)
            continue
        #ix,jx = searchIx(cuboids, c1.r1-drMax, c1.r2*1.1)
        x,y,z = tuple(c1.c1[i]-maxSize for i in range(len(c1.c1)))
        ix = bisect_left(cuboids, Cuboid(x,y,z, 1,1,1))
        x,y,z = c1.c2
        jx = bisect_right(cuboids, Cuboid(x,y,z,1,1,1))
        #ix,jx = 0,len(cuboids)-1
        intersects_with = [c2 for c2 in cuboids[ix:jx+1]
                           if doCuboidsIntersect(c1,c2)]    
        # Inclusion-Exclusion Step
        if len(intersects_with) > rMax:
            rMax = len(intersects_with)
        for r in range(1,len(intersects_with)+1):
            sign = (-1)**r
            for c in combinations(intersects_with,r):
                civ = cuboidIntersectVolume(list(c)+[c1,])
                V += sign * civ
                #if civ > 0 and r > 1:
                #    print n, civ
        cuboids = sortedInsert(cuboids,c1)
        #cuboids.sort(key=lambda c : c.r1)
        if n%250 == 0:
            print n, V, len(intersects_with), ix, jx,rMax
    print 'rMax =',rMax
    return V
