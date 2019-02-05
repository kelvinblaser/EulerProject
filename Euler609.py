#---------------------------------------------------------------
# Euler 609
#
# Ans: 172023848
#---------------------------------------------------------------

from Primes import MakePrimeList

def calcPrimePi(n, primes):
    pp = [0]*(n+1)
    pix = 0
    p = primes[pix]
    for x in range(1, n+1):
        pp[x] = pp[x-1]
        if x == p:
            pp[x] += 1
            pix += 1
            if pix < len(primes):
                p = primes[pix]
    return pp
    
def piSequence(n, primePi):
    x = n
    seq = [x]
    while x > 1:
        seq.append(primePi[x])
        x = primePi[x]
    return seq
    
  
def pNK(n, primePi, isPrime, cache, topValue):
    try:
        return cache[n][:]
    except KeyError:
        pass
    
    if n == 1: return (0,1)
    ret = list(pNK(primePi[n], primePi, isPrime, cache, False))
    ret[0] += 1
    if not isPrime[n]:
        ret = [0]+ret
    ret = tuple(ret)
    if not topValue:
        cache[n] = ret
    return ret

def P(n):
    primes = MakePrimeList(n)
    isPrime = [False for x in range(n+1)]
    for p in primes: isPrime[p] = True
    primePi = calcPrimePi(n, primes)
    seq = piSequence(n, primePi)
    #print seq
    kMax = len(seq)
    pnk = [0]*(kMax+1)
    pnk[1] = 1
    
    cache = {}
    for pix in range(len(primes)):
        p = primes[pix]
        pNext = n+1
        if pix < len(primes)-1:
            pNext = primes[pix+1]
        pnkSeq = pNK(p, primePi, isPrime, cache, True)
        d = pNext - p - 1
        for k in range(len(pnkSeq)):
            pnk[k] += pnkSeq[k]
            pnk[k+1] += d * pnkSeq[k]
        #print p, pnkSeq, pnk
        
    #for x in range(n,0,-1):
    #    pnkSeq = pNK(x, primePi, isPrime, cache, True)
    #    #print x, pnkSeq
    #    for k in range(len(pnkSeq)):
    #        pnk[k] += pnkSeq[k]
        
        if pix%100000 == 0: print pix, p, pnkSeq
    #print pnk
    pnk[0] -= len(primes)
    pnk[1] -= n
    pnk[1] += len(primes)
    #print pnk
    
    pr, MOD = 1, 10**9+7
    for x in pnk:
        if x != 0:
            pr *= x
            pr %= MOD
    return pr
    
if __name__ == '__main__':
    print 'P(10) = {0}'.format(P(10))
    print 'P(100) = {0}'.format(P(100))
    print 'P(10^8) = {0}'.format(P(10**8))