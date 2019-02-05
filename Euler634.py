# Euler 634 - Count numbers that can be written as x = a^2 b^3
# Kelvin Blaser		2019.01.14
#
# Three requirements for an acceptable x = prod(p^a) where p runs over primes
#  A. Some prime power must fulfill the a^2 portion
#  B. Some prime power must fulfill the b^3 portion
#  C. No prime power can be 1
#
# Given a prime power, we can immediately decide what can be done with it.
#  p^0 - Can be used anywhere, doesn't fulfill A or B
#  p^1 - Cannot be used.  Breaks requirement C
#  p^2 - Fulfills requirement A, but not B
#  p^3 - Fulfills requirement B, but not A
#  p^4 - Fulfills requirement A, but not B
#  p^5 - Fulfills requirements A AND B
#  p^6 - Fulfills requirement A OR B, but not both - Wild-card
#  p^n; n > 6 - Fullfills requirements A AND B
#
# Strategy:
#   1. Calculate how many numbers fulfill requirement C.
#   2. Subtract out those left which do not fulfill A.
#   3. Subtract out those left which do not fulfill B.
#   4. Add back in 1, since 1 (and only 1) fulfills C, but not A and not B
#   5. Subtract out the lone wild-cards, since they pass the previous filters,
#      but do not fulfill all requirements.
#
#
# Details
#   1. Calculate how many numbers fulfill C
#
#      We need x = prod(p^a) where all a = 0 or a >= 2
#      Consider pairs of positive integers y, k such that k | y and k is square 
#      free. Write x = y^2 * k.  Each such pair describes a unique x fulfilling 
#      requirement C, and every number fulfilling requirement C can be written
#      as such.
#
#      Iterate over square free k, and count the multiples of k that are less
#      than or equal to sqrt(n/k).  This will be zero for k > n^(1/3), so we
#      only need to iterate k up to ~2x10^6 - Doable
#
#       g(n) = sum(|mu(k)| * floor(floor(floor(n/k)^(1/2)) / k) for k = 1..floor(n^(1/3)))
#
#   2. Subtract out those left which do not fulfill A
#   
#      We need x = prod(p^a) where all a = 0 or 3.
#      This is just the number of square free values less than or equal to 
#      n^(1/3).  We already calculated these in 1.
#
#       k(n) = sum(|mu(k)| for k = 1..floor(n^(1/3)))
#
#   3. Subtract out those left which do not fulfill B
#
#      We need x = prod(p^a) where all a = 0, 2 or 4. 
#      This is just the number of cube free values less than or equal to
#      n^(1/2).  Calculate this by inclusion exclusion over k^3 for k^3 less
#      than or equal to n^(1/2)
#
#       h(n) = sum( mu(k) * floor(floor(n^(1/2)) / k^3) for k = 1..floor(floor(n^(1/2))^(1/3))
#   
#   4. Add back in 1.  This is the easiest part
#
#   5. Subtract out the lone wild-cards
#
#      We need x = p^6 where p is prime
#      Simply seive all primes up to n^(1/6) and count them.  

from Primes import MakePrimeList
import sys

def intRoot(x,n):
    r = int(x**(1.0 / n))
    while r**n > x:
        r -= 1
    while (r+1)**n <= x:
        r += 1
    return r

class Solution:
    def __init__(self, N):
        self.N = N
        self.primes = MakePrimeList(intRoot(N,3))
        self.calculateMu()
        
    def calculateMu(self):
        r3 = intRoot(self.N, 3)
        mu = [1 for _ in range(r3+1)]
        mu[0] = 0
        for p in self.primes:
            for x in range(p, r3+1, p):
                mu[x] *= -1
            for x in range(p*p, r3+1, p*p):
                mu[x] = 0
        self.mu = mu
        
    def fulfillsC(self):
        n = self.N
        mu = self.mu
        l = len(mu)
        return sum(intRoot(n//k, 2)//k for k in range(1,l) if not mu[k] == 0)
        
    def notFulfillsA(self):
        mu = self.mu
        l = len(mu)
        return sum(1 for k in range(1,l) if not mu[k] == 0)
        
    def notFulfillsB(self):
        r2 = intRoot(self.N, 2)
        kMax = intRoot(r2, 3)
        mu = self.mu
        return sum(mu[k] * (r2//(k**3)) for k in range(1,kMax+1))
        
    def loneWildCards(self):
        r6 = intRoot(self.N, 6)
        return sum(1 for p in self.primes if p <= r6)
        
    def F(self):
        return self.fulfillsC() - self.notFulfillsA() - self.notFulfillsB() + 1 - self.loneWildCards()
       
        
if __name__ == '__main__':
    print '[1001^(1/3)] =', intRoot(1001,3)
    sol = Solution(1001)
    print 'Primes less than 1001^(1/3) :', sol.primes
    print 'Mobiusfunction :', sol.mu
    sol = Solution(100)
    print 'Numbers less than 100 which fullfill C:', sol.fulfillsC()    # Should be 14
    print 'Those left that do not fulfillA:', sol.notFulfillsA()        # Should be 3
    print 'Those left that do not fulfillB:', sol.notFulfillsB()        # Should be 9
    print 'Primes less than 100^(1/6):', sol.loneWildCards()            # Should be 1
    print ''
    print 'F(100) =', sol.F()                           # Should be 2
    print 'F(2x10^4) =', Solution(20000).F()            # Should be 130
    print 'F(3x10^6) =', Solution(3000000).F()          # Should be 2014
    sys.stdout.flush()
    print 'F(9x10^18) =', Solution(9 * 10**18).F()      # Should be the right answer