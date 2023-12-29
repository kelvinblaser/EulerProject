"""Euler 447 - Retractions C

This one will require a different approach than the others.

This one is all about adding up a multiplicative function.  Since the form
of the function for primes is easy to extend and add up for all numbers,
we can extend the LucyHedghog algorithm.
v
R(n) = Q(n) - n
sum(R(n), n = 1 .. N) = sum(Q(n), n = 1 .. N) - N(N+1)/2

If n = prod(p^v, p Prime), then Q(n) = prod(1 + p^v, p Prime)

Can we solve sum(Q(n)) then?  Yes.

Define S(p, N) = sum(Q(n)) restricted to n not divisible by any prime <= p.

Then sum(Q(n), n = 1..N) = S(1, N)

Also let Sp(N) = sum(Q(p), p Prime, p <= N) i.e. the sum restricted over primes.

S(p, N) = Sp(N) - Sp(p) + 1 if p >= sqrt(N)
        = S(p + 1, N) + (1 + p) * S(p + 1, N // p) + (1 + p^2) * S(p + 1, N // p^2) ...
        = sum(q >= p, sum(v, (1 + q^v) S(q + 1, N // q^v)))   
"""
import Primes

MOD = 10**9 + 7

def F(N):
    return 0

if __name__ == '__main__':
    for exp in [7]:  #, 14]:
        print(f'F(10^{exp}) = {F(10**exp)}')