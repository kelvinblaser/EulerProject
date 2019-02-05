#--------------------------------------------------------
# Euler 224 - Almost right-angled triangles II
# Kelvin Blaser
#--------------------------------------------------------

from Primes import MakePrimeList

def squaresGen(N):
    x = 0
    while x*x <= N:
        yield x, x*x
        x += 1

def Euler224(N):
    '''Count the number of barely obtuse triangles with perimeter <= N'''    
    # Generate all pairs of squares for all numbers up to N//2+1
    M =  N//2 + 1
    squareSums = [[] for _ in range(M+1)]
    for a, a2 in squaresGen(M):
        if a%1000 == 0: print a
        for b, b2 in squaresGen(min(M-a2, a2)):
            n = a2 + b2
            squareSums[n].append((b,a))
    
    # Generate all pairs for  c^2-1 for c up to N//2+1           
    count = 0
    for c in range(3,M,2):
        pairs = set()
        if c%100000 == 1: print '{0}/{1} : {2}'.format(c,M,count)
        for x,y in squareSums[c-1]:
            for z,w in squareSums[c+1]:
                q,p = x*z+y*w, abs(x*w - y*z)
                pairs.add((min(q,p),max(q,p)))
                q,p = x*w+y*z, abs(x*z - y*w)
                pairs.add((min(q,p),max(q,p)))
        for a,b in pairs:
            if a+b+c <= N:
                #print a,b,c
                count += 1
    return count