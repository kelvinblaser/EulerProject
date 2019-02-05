# Euler 639

from Primes import MakePrimeList, Miller_Rabin
from bisect import bisect
from fractions import Fraction, gcd
from math import log

def intRoot(n):
    r = int(n**0.5)
    while (r+1)*(r+1) <= n:
        r += 1
    return r
    
def intLog(n, m):
    l = int(log(n) / log(m))
    while m**l > n:
        l -= 1
    while m**(l+1) <= n:
        l += 1
    return l
    
    
def lcm(a,b):
    return a*b / gcd(a,b)
    
def dPow10(m):
    n = m
    while n > 10:
        if not n%10 == 0: return False
        n //= 10
    return True

def ddPow10(m, e):
    n = m
    while n > 10**e:
        if not n%10 == 0: return False
        n //= 10
    return True

class SumMultiplicative:
    def __init__(self, kMax, N, MOD):
        self.kMax = kMax
        self.N = N
        self.R = intRoot(N)
        self.MOD = MOD
        self.primes = MakePrimeList(intRoot(N))
        self.squareFreeParts = self.calculateSquareFreeParts()
        self.sCache = self.initializeSCache()
        self.partialSumCache = {}
        
        self.chooseCache = {}
        self.calculateBernoulli()
        self.calculateFaulhaber()
        self.sumOverPrimesCache = self.initializeSumOverPrimesCache()
        self.partialSumOverPrimesCache = {}
        
        self.psCalled = 0
        self.psCacheHits = 0
        self.psopCalled = 0
        
    def calculateSquareFreeParts(self):
        sfp = [1]*(self.R+1)
        for p in self.primes:
            for x in range(p, self.R+1, p):
                sfp[x] *= p
        return sfp
        
    def initializeSCache(self):
        sc = [[0]*(self.R+1) for k in range(self.kMax+1)]
        for k in range(1, self.kMax+1):
            print 'Initializing sum cache: R = {0}, k = {1}'.format(self.R, k)
            for x in range(1, self.R+1):
                sc[k][x] = sc[k][x-1] + pow(self.squareFreeParts[x], k, self.MOD)
                sc[k][x] %= self.MOD
        return sc
        
    def choose(self,n,k):
        if (n,k) in self.chooseCache:
            return self.chooseCache[(n,k)]
            
        if k == 0 or k == n:
            return 1
        self.chooseCache[(n,k)] = self.choose(n-1,k-1) + self.choose(n-1, k)
        return self.chooseCache[(n,k)]
        
    def calculateBernoulli(self):
        self.bernoulli = [Fraction(0) for x in range(self.kMax+1)]
        for m in range(self.kMax+1):
            for k in range(m+1):
                for v in range(k+1):
                    b =(-1)**v * self.choose(k, v) * (v+1)**m * Fraction(1, k+1)
                    self.bernoulli[m] += b
                    
    def calculateFaulhaber(self):
        self.faulhaber = [[0] + [(self.bernoulli[m+1-j] / (m+1)) * self.choose(m+1, m+1-j) for j in range(1, m+2)] for m in range(self.kMax+1)]
    
    def evaluatePolynomial(self, poly, n):
        den = 1
        for x in poly:
            den = lcm(den, x.denominator)
        num = 0
        for exponent, f in enumerate(poly):
            part = f.numerator * (den / f.denominator) * pow(n, exponent, self.MOD)
            num += part
            num %= self.MOD
        return (num * pow(den, self.MOD - 2, self.MOD)) % self.MOD 
        
    def initializeSumOverPrimesCache(self):
        sopc = [[0]*(self.R+1) for k in range(self.kMax+1)]
        for k in range(1, self.kMax+1):            
            pix, pNext = 0,2
            for x in range(1, self.R+1):
                if x == pNext:
                    sopc[k][x] = sopc[k][x-1] + pow(x, k, self.MOD)
                    sopc[k][x] %= self.MOD
                    pix += 1
                    if pix < len(self.primes):
                        pNext = self.primes[pix]
                else:
                    sopc[k][x] = sopc[k][x-1]
            print 'Initializing sum over primes cache: R = {0}, k = {1}'.format(self.R, k)
        return sopc
          
    def sumOverPrimes(self, k, n): # Z
        if n <= self.R:
            return self.sumOverPrimesCache[k][n]
        return self.partialSumOverPrimes(k, n, intRoot(n))
    
    def partialSumOverPrimes(self, k, v, m): # W
        self.psopCalled += 1
        if (k, v, m) in self.partialSumOverPrimesCache:
            return self.partialSumOverPrimesCache[(k,v,m)]
        
        if m < 2:
            return self.evaluatePolynomial(self.faulhaber[k], v) - 1
            
        if v < m*m: return self.sumOverPrimes(k,v)
        if not Miller_Rabin(m):
            p = self.primes[bisect(self.primes, m)-1]
            return self.partialSumOverPrimes(k, v, p)
            
        # Pre-compute some values to avoid hitting recursion depth max
        #l = m-1
        #while l > 2 and (k,v,l) not in self.partialSumOverPrimesCache:
        #    l -= 1
        #for j in range(l, m):
        #    self.partialSumOverPrimes(k, v, j)
        #    
        #ans = self.partialSumOverPrimes(k, v, m-1)
        #ans -= pow(m, k, self.MOD) * self.partialSumOverPrimes(k, v//m, m-1)
        #ans += pow(m, k, self.MOD) * self.partialSumOverPrimes(k, m-1, m-1)
        #ans %= self.MOD
        
        p = m
        ans = self.partialSumOverPrimes(k, v, 1)
        for qix, q in enumerate(self.primes):
            if q > p: break
            if (v == self.N and ddPow10(qix, 2)):
                print 'sop', v, k, qix, q, len(self.partialSumCache), len(self.partialSumOverPrimesCache)
            ans -= pow(q, k, self.MOD) * ( self.partialSumOverPrimes(k, v//q, q-1) - self.partialSumOverPrimes(k, q-1, q-1) )
            ans %= self.MOD
                    
        self.partialSumOverPrimesCache[(k,v,m)] = ans
        return ans
        
    #def sumDivisibleByPrime(self, k, p, n): # X
    #    ans = pow(p,k, self.MOD) * self.reducedSumDivisibleByPrime(k, p, n)
    #    return ans % self.MOD
    #    
    #def reducedSumDivisibleByPrime(self, k, p, n): # Y
    #    if n < p: return 0
    #    try:
    #        return self.reducedSumDivisibleByPrimeCache[(k,p,n)]
    #    except KeyError:
    #        pass
    #        
    #    ans = 1 + self.reducedSumDivisibleByPrime(k, p, n//p)
    #    r = intRoot(n//p)
    #    qix = bisect(self.primes, p)
    #    if qix < len(self.primes) and self.primes[qix] == p: qix += 1
    #    for q in self.primes[qix:]:
    #        if p == 2: print q, n
    #        if q > r: break
    #        ans += self.sumDivisibleByPrime(k, q, n//p)
    #        ans %= self.MOD
    #    if p < n//p:
    #        ans += self.sumOverPrimes(k, n//p)
    #        ans -= self.sumOverPrimes(k, max(p,r))
    #        ans %= self.MOD
    #    
    #    self.reducedSumDivisibleByPrimeCache[(k,p,n)] = ans
    #    return ans
    
    def partialSum(self, k, n, m):
        self.psCalled += 1
        if (k, n, m) in self.partialSumCache:
            self.psCacheHits += 1
            return self.partialSumCache[(k,n,m)]
        if m >= n:
            return self.S(k, n) - 1
        if m < 2:
            return 0
        if m == 2:
            return (pow(2,k,self.MOD) * intLog(n, 2))%self.MOD
            
        if not Miller_Rabin(m):
            p = self.primes[bisect(self.primes, m)-1]
            return self.partialSum(k, n, p)
            
        # Precompute some values to avoid hitting recursion depth limits
        pix = bisect(self.primes, m)-1
        p = self.primes[pix]
        #pLess = self.primes[pix-1]
        #ix = pix-1
        #if (n == self.N and dPow10(pix)) or n == 10**12: #dPow10(pix):
        #    print n, k, pix, p, self.psCalled, len(self.partialSumCache), self.psopCalled, len(self.partialSumOverPrimesCache)
        #while ix > 0 and (k, n, self.primes[ix]) not in self.partialSumCache:
        #    ix -= 1
        #for jx in range(ix,pix):
        #    self.partialSum(k, n, self.primes[jx]) 
        #
        #ans = intLog(n, p)
        #for e in range(1, intLog(n, p)+1):
        #    ans += self.partialSum(k, n//pow(p,e), pLess)
        #    ans %= self.MOD
        #ans *= pow(p,k,self.MOD)
        #ans += self.partialSum(k, n, pLess)
        #ans %= self.MOD
        
        ans = 0
        r = intRoot(n)
        for qix, q in enumerate(self.primes):
            if q > p or q > r: break
            if (n == self.N and dPow10(qix)) or n == 10**12:
                print 'sum', n, k, qix, q, len(self.partialSumCache), self.psCalled, self.psCacheHits, len(self.partialSumOverPrimesCache)
            partAns = intLog(n,q)
            if not q == 2:
                for e in range(1, intLog(n,q)+1):
                    partAns += self.partialSum(k, n//(q**e), q-1)
                    partAns %= self.MOD
            ans += pow(q, k, self.MOD) * partAns
            ans %= self.MOD
        if q <= r:
            self.partialSumCache[(k,n,m)] = ans
            return ans
            
        for j in range(n//p, n//r + 1):
            ans += self.S(k, j) * (self.sumOverPrimes(k, min(p, max(r, n//j))) - self.sumOverPrimes(k, max(r, n//(j+1))))
            ans %= self.MOD
        
        #for q in self.primes[qix:]:
        #    if q > p: break
        #    if (n == self.N and dPow10(qix)) or n == 10**12:
        #        print 'sum', n, k, qix, q, len(self.partialSumCache), self.psCalled, self.psCacheHits, len(self.partialSumOverPrimesCache)
        #    partAns = intLog(n,q)
        #    if not q == 2:
        #        for e in range(1, intLog(n,q)+1):
        #            partAns += self.partialSum(k, n//(q**e), q-1)
        #            partAns %= self.MOD
        #    ans += pow(q, k, self.MOD) * partAns
        #    ans %= self.MOD
        
        self.partialSumCache[(k,n,m)] = ans
        return ans
        
    def S(self, k, n):
        if n <= self.R:
            return self.sCache[k][n]
        r = intRoot(n)
        ans = 1 + self.partialSum(k, n, r)
        for i in range(1, n // r + 1):
            ans += self.S(k, i) * (self.sumOverPrimes(k, max(n//i, r)) - self.sumOverPrimes(k, max(n//(i + 1), r)))
            ans %= self.MOD
        return ans
        
    def SumSOverK(self, kMax, n):
        ans = 0
        for k in range(1, kMax+1):
            ans += self.S(k, n)
            ans %= self.MOD
            self.partialSumCache = {}
            self.partialSumOverPrimesCache = {}
        print self.psCalled, len(self.partialSumCache), self.psopCalled, len(self.partialSumOverPrimesCache)
        return ans

if __name__ == '__main__':
    sm = SumMultiplicative(2, 10, 10**9 + 7)
    s1_10 = sm.S(1,10)
    #print 'S1(10) = {0}'.format(s1_10)
    sm = SumMultiplicative(2, 100, 10**9 + 7)
    s1_100 = sm.S(1, 100)
    s2_100 = sm.S(2, 100)
    #print 'S1(100) = {0}'.format(s1_100)
    #print 'S2(100) = {0}'.format(s2_100)
    sm = SumMultiplicative(2, 10000, 10**9 + 7)
    s1_10_4 = sm.S(1, 10000)
    #print 'S1(10000) = {0}'.format(s1_10_4)
    sm = SumMultiplicative(3, 10**8, 10**9 + 7)
    s1_10_8_3 = sm.SumSOverK(3, 10**8)
    #print 'sum( Sk(10^8) for k = 1 .. 3 ) = {0} MOD {1}'.format(s1_10_8_3, sm.MOD)
    sm = SumMultiplicative(50, 10**12, 10**9 + 7)
    s1_10_12_50 = sm.SumSOverK(50, 10**12)
    #print 'sum( Sk(10^12) for k = 1 .. 50 ) = {0} MOD {1}'.format(s1_10_12_50, sm.MOD)
    
    print ''
    print '------------------------------------------------------------'
    print 'Answers'
    print ''
    print 'S1(10) = {0}'.format(s1_10)
    print 'S1(100) = {0}'.format(s1_100)
    print 'S2(100) = {0}'.format(s2_100)
    print 'S1(10000) = {0}'.format(s1_10_4)
    print 'sum( Sk(10^8) for k = 1 .. 3 ) = {0} MOD {1}'.format(s1_10_8_3, sm.MOD)
    print 'sum( Sk(10^12) for k = 1 .. 50 ) = {0} MOD {1}'.format(s1_10_12_50, sm.MOD)
    print '------------------------------------------------------------'
    
# Poorly named methods below
#
# Method names correspond to the chicken-scratch notes in my notebook
#
#def S(k, n, primes):
#    r = intRoot(n)
#    ans = 1
#    for p in primes:
#        if p > r: break
#        ans += X(k, p, n, primes)
#    ans += Z(k, n, primes)
#    ans -= Z(k, r, primes)
#    return ans
#    
#def X(k, p, n, primes):
#    return p**k * Y(k, p, n, primes)
#    
#def Y(k, p, n, primes):
#    if n < p: return 0
#    ans = 1 + Y(k, p, n//p, primes)
#    r = intRoot(n//p)
#    for q in primes:
#        if q <= p: continue
#        if q > r: break
#        ans += X(k, q, n//p, primes)
#    if p < n//p:
#        ans += Z(k, n//p, primes)
#        ans -= Z(k, max(p, r), primes)
#    return ans
#    
#def Z(k, n, primes):
#    if n <= primes[-1]:
#        ans = 0
#        for p in primes:
#            if p > n: break
#            ans += p**k
#        return ans
#    return W(k, n, intRoot(n), primes)
#    
#def W(k, v, m, primes):
#    print v, m
#    if m < 2:
#        return sum(x**k for x in range(2, v+1))
#    if v < m*m: return W(k, v, intRoot(v), primes)
#    if not Miller_Rabin(m):
#        p = primes[bisect(primes,m)-1]
#        return W(k, v, p, primes)
#    return W(k, v, m-1, primes) - m**k * (W(k, v//m, m-1, primes) - W(k, m-1, m-1, primes))
#    