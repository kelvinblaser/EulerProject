# Euler 468
#
# Use the prime factorizations of each binomial coefficient

from Primes import MakePrimeList
from collections import defaultdict

def intRoot(n):
    r = int(n**0.5)
    while (r+1)*(r+1) <= n:
        r += 1
    return r
    
class PrimeFactorization:
    primes = MakePrimeList(1000)
    
    def __init__(self, n):
        if PrimeFactorization.primes[-1] < intRoot(n):
            PrimeFactorization.primes = MakePrimeList(intRoot(n))
        self.pf = defaultdict(int)
        for p in PrimeFactorization.primes:
            if p*p > n: break
            while n%p == 0:
                self.pf[p] += 1
                n //= p
        if n > 1:
            self.pf[n] += 1
        
    def __mul__(self, other):
        if isinstance(other, PrimeFactorization):
            rhs = other
        else:
            rhs = PrimeFactorization(other)
            
        ret = PrimeFactorization(1)
        for k in set(rhs.pf.keys()) | set(self.pf.keys()):
            exponent = self.pf[k] + rhs.pf[k]
            if exponent != 0:
                ret.pf[k] = exponent
        return ret
        
    def __rmul__(self, other):
        lhs = PrimeFactorization(other)
        return self * lhs
        
    def __div__(self, other):
        if isinstance(other, PrimeFactorization):
            rhs = other
        else:
            rhs = PrimeFactorization(other)
        nrhs = PrimeFactorization(1)
        for k in rhs.pf.keys():
            nrhs.pf[k] = -rhs.pf[k]
        return self * nrhs
        
    def __rdiv__(self, other):
        lhs = PrimeFactorization(other)
        return lhs / self
        
    def __str__(self):
        if len(self.pf) == 0:
            return '1'
        keys = list(self.pf.keys())
        keys.sort()
        strs = ['{0}^{1}'.format(k, self.pf[k]) for k in keys if self.pf[k] != 0]
        return ' '.join(strs)
        
    def __repr__(self):
        return str(self)
        
class Euler468:
    def __call__(self, n):
        MOD = 10**9 + 993
        
        ans = n
        c = PrimeFactorization(1)
        for k in range(1, n//2 + 1):
            c = (c * (n-k+1)) / k
            if k%1000 == 0:
                print k, len(c.pf)
            primes = c.pf.keys()
            primes.sort()
            val = 1
            ans += primes[0]-1
            for ix in range(1, len(primes)):
                val *= pow(primes[ix-1],c.pf[primes[ix-1]], MOD)
                val %= MOD
                ans += (primes[ix] - primes[ix-1]) * val
                ans %= MOD
            if len(primes) > 1:
                val *= pow(primes[-1],c.pf[primes[-1]], MOD)
                val %= MOD
                ans += (n - primes[-1] + 1) * val
                ans %= MOD
        return (ans * 2) % MOD
        
if __name__ == '__main__':
    e = Euler468()
    print e(11)
    print e(1111)
    #print e(111111)
    print e(11111111)