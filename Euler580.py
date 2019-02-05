#----------------------------------------------
# Euler 580
# 
# ps - primes of the form 4k + 1
# qs - primes of the form 4k + 3
#
# Hilbert numbers divisibly by x less than or equal to N
# if x is Hilbert
# floor((N + 3x) / (4x))
#----------------------------------------------
from Primes import MakePrimeList

def squareFreeGen(n, primes):
    '''Generates all square-free numbers less than or equal to n whose prime
    factors are a subset of primes. Assumes primes is sorted'''
    ixMax, a = 0, n
    while a > 0:
        ixMax += 1
        a /= 2
    cix = 0
    ix = [0]*(ixMax+2)
    p = 1
    if n >= 1: yield []
    while cix >= 0:
        if ix[cix] >= len(primes) or p*primes[ix[cix]] > n:
            cix -= 1
            p //= primes[ix[cix]]
            ix[cix] += 1
        else:
            p *= primes[ix[cix]]
            cix += 1
            ix[cix] = ix[cix-1]+1
            yield [primes[jx] for jx in ix[:cix]]
    return
    
def prod(l):
    x = 1
    for y in l: x *= y
    return x
    
def choose(n,k):
    if k < 0 or k > n: return 0
    c = 1
    if k > n//2: k = n - k
    for kk in range(k):
        c *= n-kk
    for kk in range(1,k+1):
        c /= kk
    return c
            
def squareFreeHilberts(N):
    rN = int(N**0.5)
    while (rN+1)*(rN+1) <= N:
        rN += 1
    primes = MakePrimeList(rN)
    ps = [p for p in primes if p%4 == 1]
    qs = [q for q in primes if q%4 == 3]
    
#    count = (N+3)//4
    count = 0
    for pset in squareFreeGen(rN, ps):
        pProd = prod(pset)
        pLen = len(pset)
        pMul = (-1)**pLen
        #if pLen > 1:
        #    print pProd, pset, count
        qProdMax = rN // pProd
        for qset in squareFreeGen(qProdMax, qs):
            qLen = len(qset)
            qMul = 0
            for x in range((qLen+1)//2, qLen*(qLen-1)//2 + 1):
                n1 = choose(qLen, 2)
                n2 = choose(qLen-1,2)
                qMul += ((-1)**x) * (choose(n1, x) - choose(n2, x))
            if qLen == 0: qMul = 1
            qq = (pProd*prod(qset))**2
            diff = pMul*qMul*((N+3*qq)/(4*qq))
            count += diff
            print qq, pset, qset, diff, count
    for q in qs:
        q2 = q*q
        if q2 > rN: break
        while q2 <= rN:
            count -= 1
            q2 *= 2
        print q, count
    return count
    
if __name__ == '__main__':
    #print 'Squarefree Hilberts <= 10^{0} : {1}'.format(7, squareFreeHilberts(10**7))
    pass