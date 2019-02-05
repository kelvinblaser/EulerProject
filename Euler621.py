# Euler 621
# Kelvin Blaser
#
# The number of ways to express an integer n as the sum of 3 triangular numbers
# is the same as the number of ways to express 8n+3 as the sum of 3 odd squares. 

from Primes import MakePrimeList
from collections import defaultdict

class G: 
    def __init__(self, N):
        self.N = N
        self.primes = MakePrimeList(N)
        #self.twoOddCache = {}
        
    def __call__(self, n):
        numWays = 0
        m = 8*n+3
        r = int(m**0.5) + 3
        for k in range(1,r+1,2):
            if k*k > m:
                break
            if (k-1)%1000 == 0:
                print k
            numWays += self.twoOddSquares(m-k*k)
        return numWays
    
    def twoOddSquares(self, n):
        if n%4 != 2:
            return 0
        twoSquares = self.twoSquares(n)
        
        return twoSquares
        
    def twoSquares(self, n):
        # Get prime factors
        m = n
        primeFactorization = defaultdict(int)
        if self.N**2 < m:
            self.N = 2*self.N
            self.primes = MakePrimeList(self.N)
            
        for p in self.primes:
            if p*p > m:
                break
            while m%p == 0:
                primeFactorization[p] += 1
                m //= p
        if m != 1:
            primeFactorization[m] += 1
            
        # Calculate how many ways to write n as the sum of two squares
        a0 = primeFactorization[2]
        B = 1
        for p in primeFactorization.keys():
            if p%4 == 1:
                B *= primeFactorization[p] + 1
            if p%4 == 3:
                if primeFactorization[p]%2 == 1:
                    B = 0
                    break
        return B
        
if __name__ == '__main__':
    g = G(12000000)
    print g(1000)
    print g(10**6)
    print g(10**9)
    print g(17526*10**9)