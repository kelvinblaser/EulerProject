# Euler 365
from Primes import MakePrimeList
from itertools import combinations

def chineseRemainder(primeValueDict):
    n = 1
    x = 0
    
    for p in primeValueDict.keys():
        #X = x mod n
        #X = qn + x
        #X = z mod p
        #X = ((q mod p) * (n mod p) + x mod p) mod p
        #z = ((q mod p) * (n mod p) + x mod p) mod p
        #q = (z - x) / n mod p
        q = (primeValueDict[p] - x) % p
        q *= pow(n, p-2, p)
        q %= p
        x += q*n
        n *= p
    
    return x % n
    
def chooseMod(n,k,p):
    if k < 0 or k > n:
        return 0
    if n >= p:
        return (chooseMod(n//p, k//p, p) * chooseMod(n%p, k%p, p)) % p
    num, den = 1,1
    for kk in range(1, k+1):
        num *= n-kk+1
        den *= kk
        num %= p
        den %= p
    return (num * pow(den, p-2, p))%p
    
def Euler365():
    primes = [p for p in MakePrimeList(5000) if p > 1000]
    binom = {p : chooseMod(10**18, 10**9, p) for p in primes}
    return sum(chineseRemainder({p: binom[p] for p in c}) for c in combinations(primes, 3))

if __name__ == '__main__':
    print Euler365()