# Euler 263
# Kelvin Blaser     2019-02-26
#
# Checking cases for divisiblity and practicalness leads to
# n = +- 20 MOD 840
#
# Just check all those numbers for primality and practicality

from __future__ import division, print_function
from Primes import MakePrimeList, Miller_Rabin
from collections import defaultdict

def Euler263():
    primes = MakePrimeList(1000000)
    eps = []
    base = 840
    sexyTriples = 0
    while len(eps) < 4:
        if (base//84) % 1000000 == 0:
            print('base = {:10}   Sexy triples tested : {:6}'.format(base, sexyTriples))
        for n in [base-20, base+20]:
            if (Miller_Rabin(n-9) and
                not Miller_Rabin(n-7) and
                not Miller_Rabin(n-5) and
                Miller_Rabin(n-3) and
                not Miller_Rabin(n-1) and
                not Miller_Rabin(n+1) and
                Miller_Rabin(n+3) and
                not Miller_Rabin(n+5) and
                not Miller_Rabin(n+7) and
                Miller_Rabin(n+9)):
                sexyTriples += 1
                if (isPractical(n-8, primes) and
                    isPractical(n-4, primes) and
                    isPractical(n, primes) and
                    isPractical(n+4, primes) and
                    isPractical(n+8, primes)):
                    eps.append(n)
                    print('{0:10}\n\tSexy-Triple: {1:50}\n\tPracticals:  {2:60}'.format(n, (n-9, n-3, n+3, n+9), (n-8, n-4, n, n+4, n+8)))
        base += 840
    return sum(eps)

def isPractical(n, primes):
    primeFact = primeFactorization(n, primes)
    ps = list(primeFact.keys())
    ps.sort()
    if ps[0] != 2: return False
    sig = [1] + [(pow(ps[i], primeFact[ps[i]]+1) - 1) // (ps[i] - 1) for i in range(len(ps))]
    #print(sig)
    for i in range(len(ps)):
        if ps[i] > 1 + sig[i]: return False
        sig[i+1] *= sig[i]
    return True

def primeFactorization(n, primes):
    pf = defaultdict(int)
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            pf[p] += 1
            n //= p
    if n != 1:
        pf[n] += 1
    return pf


if __name__ == '__main__':
    primes = MakePrimeList(200)
    print('First Practicals : [{0}]'.format(', '.join(str(n) for n in range(2,151) if isPractical(n, primes))))
    print('Sum of first four engineers\' paradises: {}'.format(Euler263()))
