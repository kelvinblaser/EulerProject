#--------------------------------------------------------------------------
# Euler 583
#--------------------------------------------------------------------------

from Primes import primitivePythagoreanTriples
from collections import defaultdict

def integerRoot(n):
    r = int(n**0.5)
    while (r+1)*(r+1) <= n:
        r += 1
    return r

def Euler583(N):
    # Generate all relevant pythagorean triples
    pythLegs = defaultdict(list)
    for x,y,h in primitivePythagoreanTriples(N//2):
        for m in range(1, (N // (2*(x+y))) + 1):
            pythLegs[m*x].append(m*y)
            pythLegs[m*y].append(m*x)
    for x in pythLegs.keys():
        pythLegs[x].sort()
        #print x, pythLegs[x]
            
    # Make envelopes and see which ones work
    perSum = 0
    p2 = 1
    keys = list(pythLegs.keys())
    keys.sort()
    for x in keys:
        if x%2 == 1: continue
        if x > p2:
            print x
            p2 *= 2
        for z in pythLegs[x//2]:
            l2 = z*z + x*x//4
            l = integerRoot(l2)
            for y in pythLegs[x]:
                if y <= z: continue
                b2 = y*y + 2*y*z + l2
                b = integerRoot(b2)
                p = 2*(y+l) + x
                if b*b == b2 and p <= N:
                    perSum += p
                    #print x,y,l
    return perSum