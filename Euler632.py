# Euler 632

from Primes import MakePrimeList

def squareFreeNumbers(N):
    primes = MakePrimeList(N)
    sf = [True]*(N+1)
    numPrime = [0]*(N+1)
    last = 1
    for p in primes:
        if last//100000 != p//100000: print p
        for pp in range(p,N+1,p):
            numPrime[pp] += 1
        for pp in range(p*p, N+1, p*p):
            sf[pp] = False
        last = p
    return [(x, numPrime[x]) for x in range(1, N+1) if sf[x]]
    
def ck(N, k, squareFree, alpha):
    s = 0
    for q, m in squareFree:
        s += alpha[k][m] * (N//(q*q))
    return s
    
if __name__ == '__main__':
    choose = [[0]*11 for _ in range(11)]
    for n in range(11):
        choose[n][0] = 1
        for k in range(1,n+1):
            choose[n][k] = choose[n-1][k-1] + choose[n-1][k]
    alpha = [[0]*11 for _ in range(11)]
    for k in range(11):
        alpha[k][k] = 1
        for l in range(k+1, 11):
            for j in range(k,l):
                alpha[k][l] -= choose[l][j] * alpha[k][j]
                
    print choose
    print alpha
    
    sf = squareFreeNumbers(10**8)
    print len(sf)
    C = [ck(10**16, k, sf, alpha) for k in range(11)]
    print C
    
    ans = 1
    mod = 10**9+7
    for x in C:
        if x != 0:
            ans *= x
            ans %= mod
    print ans