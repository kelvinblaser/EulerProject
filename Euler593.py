#-------------------------------------------------------------------
# Euler 593 - Fleeting Medians
#-------------------------------------------------------------------

from Primes import MakePrimeList

def makeSequences(n):
    primes = MakePrimeList(20*n)  # Large enough for the n's we want to consider
    S = [pow(primes[k], k+1, 10007) for k in range(n)]
    S2 = [S[k] + S[(k+1)//10000] for k in range(n)]
    return S, S2
        
def F(n,k):
    S, S2 = makeSequences(n)
    f = 0
    for i in range(n-k+1):
        m = S2[i:i+k]
        m.sort()
        f += m[k//2] + m[(k-1)//2]
    return f/2.0