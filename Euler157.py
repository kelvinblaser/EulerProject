# Project Euler 157 - Solving the Diophantine Equation 1/a + 1/b = p/10^n
#  Kelvin Blaser    - 2013.12.11

import Primes
import scipy as sp

class Num_Divisors:
    def __init__(self, limit):
        self.primes = Primes.MakePrimeList(int(sp.sqrt(2*limit)))
        self.memo   = {}

    def __call__(self, n):
        if n in self.memo:
            return self.memo[n]
        m = n
        i = 0
        root = int(sp.sqrt(n)) + 1
        divs = 1
        while i < len(self.primes) and self.primes[i] < root:
            r = 0
            while n % self.primes[i] == 0:
                r += 1
                n /= self.primes[i]
            divs *= (r+1)
            root = int(sp.sqrt(n)) + 1
            i += 1
        if n != 1:
            divs *= 2
        self.memo[m] = divs
        return divs

def Euler157(N=9):
    num_sols = 0
    num_divisors = Num_Divisors(10**N)
    for n in range(1,N+1):
        ten_n = 10**n
        for i in range(n+1):
            for j in range(n+1):
                a = 1
                b = 2**i * 5**j
                p = (ten_n * (a + b)) / (a*b)
                num_sols += num_divisors(p)
       
                if i == 0 or j == 0:
                    continue

                a = 2**i
                b = 5**j
                p = (ten_n * (a + b)) / (a*b)
                num_sols += num_divisors(p)
                       
    return num_sols
