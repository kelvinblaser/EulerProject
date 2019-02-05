# Euler 579 - Lattice points in lattice cubes

from itertools import permutations

def countLatticePoints(cube, N):
    xVals = [x[0] for x in cube]
    yVals = [x[1] for x in cube]
    zVals = [x[2] for x in cube]
    dx = max(xVals)
    dy = max(yVals)
    dz = max(zVals)
    if dx > N or dy > N or dz > N:
        return 0
    return (N-dx+1)*(N-dy+1)*(N-dz+1) # just count cubes for now
    
def calcCanonicalSides(N):
    N2 = N*N
    sides = [set() for _ in range(N2+1)]
    for c in range(N+1):
        c2 = c*c
        for b in range(c+1):
            b2 = b*b
            if b2 + c2 > N2: break
            for a in range(b+1):
                a2 = a*a
                if a2 + b2 + c2 > N2: break
                sides[a2+b2+c2].add((a,b,c))
    return sides
    
def pointAdd(x1, x2):
    return tuple([x1[i]+x2[i] for i in range(3)])

def pointMul(x1, x2):
    return sum(x1[i]*x2[i] for i in range(3))
    
def calcCanonicalCubes(N):
    sides = calcCanonicalSides(N)
    #print 'Num sides :', sum(len(x) for x in sides)
    cubes = set()
    for k in range(1,N*N+1):
        if k%100 == 0:
            print k
        corners = set()
        kubes = set()
        for x,y,z in sides[k]:
            corners.update(permutations((x,y,z)))
            corners.update(permutations((x,y,-z)))
            corners.update(permutations((x,-y,z)))
            corners.update(permutations((x,-y,-z)))
            #corners.update(permutations((-x,y,z)))
            #corners.update(permutations((-x,y,-z)))
            #corners.update(permutations((-x,-y,z)))
            #corners.update(permutations((-x,-y,-z)))
        #print k, len(corners)
        corners = list(corners)
        for ix1 in range(len(corners)-2):
            x1 = corners[ix1]
            for ix2 in range(ix1+1, len(corners)-1):
                x2 = corners[ix2]
                if pointMul(x1,x2) != 0: continue
                for ix3 in range(ix2+1, len(corners)):
                    x3 = corners[ix3]
                    if pointMul(x1,x3) != 0: continue
                    if pointMul(x2,x3) != 0: continue
                    x4 = pointAdd(x1,x2)
                    x5 = pointAdd(x1,x3)
                    x6 = pointAdd(x2,x3)
                    x7 = pointAdd(x4,x3)
                    wholeCube = [(0,0,0), x1,x2, x3, x4,x5,x6, x7]
                    dx = -min(x[0] for x in wholeCube)
                    dy = -min(x[1] for x in wholeCube)
                    dz = -min(x[2] for x in wholeCube)
                    wholeCube = [pointAdd(x, (dx, dy,dz)) for x in wholeCube]
                    wholeCube.sort()
                    kubes.add(tuple(wholeCube))
        cubes.update(kubes)
    return cubes
    
def S(N):
    return sum(countLatticePoints(c,N) for c in calcCanonicalCubes(N))
    