# Euler 633
# Inclusion - Exclusion

from Primes import MakePrimeList
from math import pi

if __name__ == '__main__':
    primes = MakePrimeList(1000000)
    l = 20
    C = [0]*l
    a = [0]*l
    for n in range(1,l):
        a[n] = sum(1.0 / (p*p-1)**n for p in primes)
    C[0] = 6 / (pi * pi)
    for n in range(1, l):
        C[n] = 1.0 / n * sum((-1)**(k+1) * C[n-k]*a[k] for k in range(1, n+1))
    for n in range(l):
        print n, C[n]    