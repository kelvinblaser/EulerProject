# Euler 622
#
# A deck of size x (x is even) will return to its original state after m 
# shuffles iff 2^m = 1 mod x-1

from Primes import MakePrimeList
from collections import defaultdict
import itertools as it
from operator import mul

class Riffle:
    def __init__(self, N):
        self.N = N
        self.primes = MakePrimeList(N)
        
    def sumSat(self, m):
        # These are one less than the x's which return to their original state
        # after m shuffles.
        divisors = self.calcDivisor(2**m-1)
        
        # However, some of them might also return to their original state after
        # fewer than m shuffles.  We must purge these from the list
        xs = []
        for x in divisors:
            for l in range(1,m):
                z = 2**l - 1
                if z%x == 0:
                    break
            else:
                xs.append(x)
        
        return sum(xs) + len(xs)
    
    def calcDivisor(self, n):
        primeFact = defaultdict(int)
        for p in self.primes:
            if p*p > n:
                break
            while n%p == 0:
                n //= p
                primeFact[p] += 1
        if n != 1:
            primeFact[n] += 1
        
        primePows = [[p**x for x in range(primeFact[p]+1)] for p in primeFact.keys()]
        return [reduce(mul, d, 1) for d in  it.product(*primePows)]
        
if __name__ == '__main__':
    # 2^60 - 1 = (2^30+1)(2^30-1) = (2^10+1)(2^20-2^10+1)(2^15+1)(2^15-1)
    # We only need primes up to sqrt(2^20-2^10+1) ~ 2^10
    # Primes up to 200 will do the trick
    r = Riffle(2000)  
    print r.sumSat(8)
    print r.sumSat(60)