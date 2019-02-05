################################################################################
# Euler 407 - Idempotents
# Kelvin Blaser    2015.02.25
#
#       a^2 = a mod n
#       a^2-a = 0 mod n
#       a(a - 1) = 0 mod n
#
# Let n = pq with gcd(p,q) = 1.  Then a = 0 mod p and a-1 = 0 mod q.
#       a = 1 mod q, a = rp
#       rp = 1 mod q
#       r = p^-1[q] mod p;      r is the inverse of p in Z/Zq
# Thus there is a solution a = rp where r is the inverse of p in Z/Zq for every
# way to factor n = pq with gcd(p,q) = 1
################################################################################

from Primes import MakePrimeList, EulerPhi
from itertools import combinations
from scipy import prod

#-------------------------------------------------------------------------------
# Solution Algorithm
#
# Make a list of primes up to n_max
# Sieve an array to get Eulers totient phi(n) for n up to n_max
#   This is for use in calculating p^-1[q] = p^(phi(q)-1) mod q
# Sieve to get the prime factorization of each number.  The result is a list of
#   lists, where each sublist has entries of the form prime^exp.  For example,
#   prime_fact[180] = [2^2, 3^2, 5] = [4,9,5]
# Take products of combinations of all sizes from the list to get p and q.
#   Calculate p * (p^(phi(q)-1) mod q)
#   Add the largest to the sum.
#
# Algorithm works, but is kinda slow.  ~25 min
#-------------------------------------------------------------------------------

def primeFactorsLists(N,primes):
    p_facts = [0]*(N+1)
    for x in xrange(N+1):
        p_facts[x] = []
    count = 0
    for p in primes:
        if count%10000==0:
            print 'primeFactorsLists:\t%d/%d Complete'%(count,len(primes))
        for x in xrange(p,N+1,p):
            p_facts[x].append(1)
            y = x
            while y % p == 0:
                y /= p
                p_facts[x][-1] *= p
        count += 1
    return p_facts

def sumLargestIdempotents(N):
    primes = MakePrimeList(N)
    phi = EulerPhi(N)
    p_facts = primeFactorsLists(N,primes)
    ret = 0
    for x in xrange(1,N+1):
        if x % 10000 == 0:
            print 'Sum:\t%d/%d Complete\t\t%d'%(x,N,ret)
        idempotents = []
        for r in range(len(p_facts[x])+1):
            for c in combinations(p_facts[x],r):
                p = int(prod(c))
                q = x / p
                idempotents.append((p*pow(p,int(phi[q])-1,q))%x)
        #print x,phi[x], max(idempotents), idempotents
        ret += int(max(idempotents))
    return ret

def sumSlow(N):
    ret = 0
    for x in xrange(1,N+1):
        ids = [a for a in range(x) if (a*a) % x == a]
        #print x,ids[-1]
        ret += ids[-1]
    return ret


if __name__ == '__main__':
    print sumLargestIdempotents(10**7)
    
