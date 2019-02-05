# Euler 75 - Unique Pythagorean Triples
# Kelvin Blaser - 11-17-2012
import scipy as sp

def Euler75(pMax):
    """Finds the number of integer lengths of wire (less than or equal to n)
    that can be uniquely bent into an integer sided right triangle.
    """
    pythagTriples = {}
    mMax = int(sp.floor(sp.sqrt(pMax/2)))
    for m in range(2,mMax+1):
        nMax = min(m,(pMax - 2*m*m)/(2*m)+1)
        for n in range(1,nMax):
            p = 2*m*(m+n)
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            triple = [a,b,c]
            triple.sort()
            triple = tuple(triple)
            if not pythagTriples.has_key(p):
                pythagTriples[p]  =[]
            if not triple in pythagTriples[p]:
                for k in range(1,pMax/p+1):
                    kTrip = (triple[0]*k, triple[1]*k, triple[2]*k)
                    if not pythagTriples.has_key(k*p):
                        pythagTriples[k*p] = []
                    if not kTrip in pythagTriples[k*p]:
                        pythagTriples[k*p].append(kTrip)

    unique = []
    perimeters = pythagTriples.keys()
    for p in perimeters:
        if len(pythagTriples[p])==1:
            unique.append([p,pythagTriples[p]])
    unique.sort(key=lambda x: x[0])
    return len(unique),unique
