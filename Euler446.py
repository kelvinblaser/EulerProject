"""Euler 446 - Retractions B

See Euler 445.

If n = prod(p^v_p, p Prime) then
R(n) = -n + prod((1 + p^v_p), p Prime) = Q(n) - n

This solution relies on the fact that 
  n^4 + 4 = (n^2 - 2n + 2)(n^2 + 2n + 2)

To make this fast, we need to find the roots of n^4 + 4 mod p for each prime p,
then sieve.

For p = 2, the only root is 0.

For other p, we have (+-2 +- 2 * sqrt(-1)) / 2 = +-1 +- sqrt(-1)
So this reduces to finding the square roots of -1 mod p.
"""

from Euler import tonelliShanks
from Primes import MakePrimeList

MOD = 10**9 + 7

def Euler446(N):
    # Because both of the factors could possibly be divisibly by a prime
    # greater than N, we have to sieve over both factors separately to know
    # whether the leftover number at the end is a prime, or the product of two
    # primes.
    numsp = [n**2 + 2 * n + 2 for n in range(N + 1)]
    numsm = [n**2 - 2 * n + 2 for n in range(N + 1)]
    sumn = sum(numsp[k] * numsm[k] for k in range(N + 1))
    primes = MakePrimeList(2 * N)
    q = [1 for _ in range(N + 1)]
    for p in primes:
        if p == 2:
            roots = [0]
        elif p % 4 == 1:
            x = tonelliShanks(p - 1, p)
            roots = [1 + x, 1 - x, -1 + x, -1 - x]
            roots = set([r % p for r in roots])
        else:
            roots = []
        for r in roots:
            for n in range(r, N + 1, p):
                v = 0
                while numsp[n] % p == 0:
                    numsp[n] //= p
                    v += 1
                while numsm[n] % p == 0:
                    numsm[n] //= p
                    v += 1
                if v > 0:
                    q[n] *= (1 + p**v)
                    q[n] %= MOD
    for n in range(2, N + 1):
        if numsm[n] > 1 and numsm[n] == numsp[n]:
            q[n] *= (1 + numsm[n] * numsp[n])
            print("Hello!")
            continue
        if numsm[n] > 1:
            q[n] *= (1 + numsm[n])
        if numsp[n] > 1:
            q[n] *= (1 + numsp[n])
    return (sum(q) - q[0] - sumn + 4) % MOD

if __name__ == '__main__':
    # print(77532377300600 % MOD)
    for n in [1024, 10**7]:
        print(f'SR({n}) = {Euler446(n)}')
