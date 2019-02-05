#---------------------------------------------------------------
# Euler 310
#---------------------------------------------------------------
from collections import defaultdict

def mex(it):
    s = set(it)
    l = list(s)
    for ix in range(len(l)):
        if l[ix] != ix:
            return ix
    return len(l)

def calcScore(n):
    g = [0]*(n+1)
    for x in range(1, n+1):
        gNext = [g[x-y*y] for y in range(1,int(x**0.5)+1)]
        g[x] = mex(gNext);
    return g
    
def countPositions(N):
    g = calcScore(N)
    counts = defaultdict(int)
    for x in g:
        counts[x] += 1
    print counts
    
    nonOrdered = 0
    for k1 in counts.keys():
        for k2 in counts.keys():
            k3 = k1^k2
            nonOrdered += counts[k1]*counts[k2]*counts[k1^k2]
    print nonOrdered
    
    allSame = counts[0]   # x,y and z can only all be the same if their score is 0
    twoSame = counts[0]*N # for each x | g(x) = 0, there are N pairs y,z | y=z, g(y)^g(z) = 0, and y,z != x 
    allDifferent = (nonOrdered - allSame - twoSame*3) // 6
    print (nonOrdered - allSame - twoSame*3)%6
    
    print allSame, twoSame, allDifferent
    return allSame + twoSame + allDifferent
    

if __name__ == '__main__':
    print 'losing positions 0 <= a <= b <= c <= {0}: {1}'.format(29, countPositions(29))
    print 'losing positions 0 <= a <= b <= c <= {0}: {1}'.format(100000, countPositions(100000))