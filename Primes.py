# Prime Number Functions
"""
A set of procedures for computing prime numbers, testing primality, etc.
"""

import numpy as sp
from bisect import bisect
from math import log, gcd

def intRoot(n):
    r = int(n**0.5)
    while (r+1)*(r+1) <= n:
        r += 1
    while r*r > n:
        r -= 1
    return r

def MakePrimeList(N: int, /) -> list[int]:
    """
    Uses the Sieve of Eratosthenes to return a list of all the primes less
    than or equal to N
    """

    # Initialize
    sieveBound = int((N+1)/2)
    sieve = [False]*sieveBound
    crossLimit = (int(sp.sqrt(N))-1)//2

    # Sieve
    for x in range(1,crossLimit+1):
        if not sieve[x]:
            y = 2*x*(x+1)
            while y < sieveBound:
                sieve[y] = True
                y += 2*x+1

    # Put the list together.
    primeList = [2]
    for x in range(len(sieve)):
        if not sieve[x]:
            primeList.append(2*x+1)
    #oddPrimes = [x for x in range(N+1) if (x%2 and not sieve[(x-1)/2])]
    #primeList.extend(oddPrimes)
    primeList.remove(1)

    return primeList

def isPrime(n, primeList=[]):
    """
    Checks if a number is prime by trial division by all primes up to
    sqrt(n)

    For repeated use, primeList should be calculated before hand.

    primeList = MakePrimeList(sqrt(N))
    """
    if primeList == []:
        primeList = MakePrimeList(int(sp.sqrt(n))+1)

    if n <= max(primeList):
        if n in primeList:
            return True
        else:
            return False

    j = 1
    rt = sp.sqrt(n)
    while (j < len(primeList) and primeList[j] < rt):
        j *= 2
        if j >= len(primeList):
            j = len(primeList)-1
    prime_test = primeList[:j+1]
    for p in prime_test:
        if n % p == 0:
            return False
    return True

def Miller_Rabin(n):
	a_list=[2,3,5,7,11,13,17]
	if n in a_list:
		return True
	if n%2 == 0:
		return False
	if n < max(a_list):
		return False
	d = (n-1)//2
	s = 1
	while d%2==0:
		d //= 2
		s += 1
	for a in a_list:
		if a > n-2:
			continue
		x = pow(a,d,n)
		if x == 1 or x == n-1:
			continue
		for i in range(s-1):
			x = pow(x,2,n)
			if x == 1:
				return False
			if x == n-1:
				break
		if x == n-1:
			continue
		return False
		#a2rd = [True for r in range(0,s) if pow(a,2**r*d, n) != n-1]
		#if pow(a,d,n) != 1 and all(a2rd):
		#	return False
	return True

class Mobius:
    memo = {}
    memVec = []

    def __init__(self, nMax):
        self.nMax = nMax
        if nMax <= len(self.memVec): return
        self.memVec = [1 for x in range(nMax+1)]
        primes = MakePrimeList(intRoot(nMax)+1)
        for p in primes:
            for x in range(p*p, nMax+1, p*p):
                self.memVec[x] = 0
            for x in range(p, nMax+1, p):
                self.memVec[x] *= -p
        for x in range(nMax+1):
            if self.memVec[x] == 0: continue
            if abs(self.memVec[x]) < x: self.memVec[x] *= -1
            if self.memVec[x] < 0: self.memVec[x] = -1
            else: self.memVec[x] = 1

    def __call__(self, n):
        if n <= self.nMax:
            return self.memVec[n]

class Mertens:
    memo = {}
    def __init__(self, nMax):
        r = int(nMax**(2.0/3.0))+1
        self.r = r
        primes = MakePrimeList(r)
        self.memVec = [1]*(r+1)
        self.memVec[0] = 0
        for p in primes:
            for x in range(p, r+1, p):
                self.memVec[x] = -self.memVec[x]
            for y in range(p*p, r+1, p*p):
                self.memVec[y] = 0
        for x in range(2, r+1):
            self.memVec[x] += self.memVec[x-1]

    def __call__(self, n):
        if n < 0: raise ValueError
        if n <= 1: return n
        if n <= self.r: return self.memVec[n]
        if n in self.memo: return self.memo[n]
        r = intRoot(n)
        ans = 1
        for d in range(1, r+1):
            if d > 1: ans -= self(n//d)
            ans -= ( max(r, n//d) - max(r, n//(d+1)) ) * self(d)
        self.memo[n] = ans
        return ans

class Mertens2:
    mobius = []
    memVec = []
    memo = {}
    def __init__(self, nMax):
        u = nMax**(1.0/3.0) * log(log(nMax))**(2.0/3.0)
        u = int(u) + 1
        if (u**2 + 2) <= len(self.mobius): return
        mob = Mobius(u**2+2)
        Mertens2.mobius = [mob(x) for x in range(u**2+1)]
        Mertens2.memVec = [x for x in self.mobius]
        self.memVec[0] = 0
        self.memVec[1] = 1
        for x in range(2, len(self.memVec)):
            self.memVec[x] += self.memVec[x-1]

    def __call__(self, n):
        if n <= len(self.memVec): return self.memVec[n]
        if n in self.memo: return self.memo[n]

        u = n**(1.0/3.0) * log(log(n))**(2.0/3.0)
        u = int(u) + 1

        S1 = 0
        for m in range(1,u+1):
            diff = 0
            for k in range(u//m+1, intRoot(n//m)+1):
                diff += self(n//(m*k))
            S1 += self.mobius[m] * diff

        S2 = 0
        for k in range(1, intRoot(n)+1):
            diff = 0
            for m in range(1, min(u, n//(k*k))+1):
                diff += self.mobius[m]*self.l(n//m, k)
            S2 += self(k) * diff

        self.memo[n] = self(u) - S1 - S2
        return self.memo[n]

    def l(self, y, k):
        r = intRoot(y)
        return max(r, y//k) - max(r, y//(k+1))


class Prime_Pi:
    # Memoize
    memo = {}
    restricted_memo = {}
    def __call__(self, m, primes):
        """
        Returns the number of primes less than or equal to m.
        Primes is a list of primes.  Needs to have at least the first
        sqrt(m) primes.
        Uses the Meissel Method
        """
        try:
            return self.memo[m]
        except KeyError:
            pass
        self.memo[m] = self.prime_count(m,primes)
        return self.memo[m]

    def prime_count(self, m, primes):
        if m < 2:
            return 0
        if m == 2:
            return 1
        if m <= primes[-1]:
            return bisect(primes,m)
        try:
            return self.memo[m]
        except KeyError:
            pass
        # Need to be careful with numerical issues in defining n
        # For example 1331 = 11^3, but  int(1331**(1./3)) returns 10
        # since 1331**(1./3) -> 10.999999998
        root = int(m**(1./3))
        if (root+1)**3 == m:
            root += 1
        n = self.prime_count(root, primes)
        root = int(sp.sqrt(m))
        if (root+1)**2 == m:
            root += 1
        mu = self.prime_count(root, primes)-n

        #print 'm = '+str(m)+', n = '+str(n)+', mu = '+str(mu)

        ans = self.restricted_prime_count(m,n, primes)
        ans += n*(mu+1) + (mu*mu - mu)//2 - 1
        # Need primes up to (n+mu)th prime
        # We know n+mu < m^1/3 + m^1/2
        for k in range(mu):
            ans -= self.prime_count(m // primes[n+k], primes)
        self.memo[m] = ans
        return ans

    def restricted_prime_count(self,m,n,primes):
        if n == 0:
            return m
        if m == 0:
            return 0
        if primes[n-1] > m:
            return 1
        try:
            return self.restricted_memo[(m,n)]
        except KeyError:
            pass
        ans = m
        #print '    m = '+str(m)+', n = '+str(n)
        for ix in range(n):
            ans -= self.restricted_prime_count(m//primes[ix], ix, primes)
        self.restricted_memo[(m,n)] = ans
        return ans

def combProdLessThan(iterable, r, N):
    '''Yields all combinations of r elements from list l whose product is
    less than or equal to N.

    INPUT:
        iterable - list of numerical elements, needs to be sorted.
        r - number of elements to choose from
        N - maximum product

    YIELD:
        combinations as a tuple
    '''
    count = 0
    pool = tuple(iterable)
    n = len(pool)
    if r > n:   # No combinations with r > n
        return

    def prod(itt):
        x = 1
        for y in itt:
            x *= y
        return x

    indices = list(range(r))  # Set up the list of indices
    if prod(tuple(pool[i] for i in indices)) <= N:
        yield tuple(pool[i] for i in indices)
    else:
        return

    while True:
        for i in reversed(range(r)):
            if indices[i] != i+n-r:  # Not done condition
                break
        else:   # Done
            return
        n = len(pool)  # If pool was reduced, return it to full size
        indices[i] += 1  # i is now the active pointer
        for j in range(i+1,r):
            indices[j] = indices[j-1]+1
        c = tuple(pool[k] for k in indices)
        if prod(c) <= N:
            yield c
        else:   # If product too large, temporarily reduce the pool
            n = indices[i]+r-i

def EulerPhi(N):
    ''' Returns an array phi, where phi[n] is equal to euler's totient function
    applied to n.'''
    phi = sp.arange(N+1,dtype=int)
    for p in range(2,N+1):
        if phi[p] != p:   # Didn't find a prime
            continue
        for x in range(p,N+1,p):
            phi[x] //= p
            phi[x] *= (p-1)
    return phi


def primitivePythagoreanTriples(N):
    ''' Generates all primitive pythagorean triples with legs less than or
    equal to N'''
    aMax = int((2*N*(2**0.5))**0.5)+1
    for a in range(3, aMax+1, 2):
        if a*a >= 2*N*(2**0.5):
            bMax = 1
        else:
            bMax = a#int((2*N*(2**0.5) - a*a)**0.5) + 1
        for b in range(1, min(a,bMax+1), 2):
            if gcd(a,b) > 1: continue
            x,y,z = a*b, (a*a-b*b)//2, (a*a+b*b)//2
            if x <= N and y <= N:
                yield x,y,z

def matModMult(A,B,MOD):
	''' Returns the matrix product AB modulo MOD.  A and B must be
	sp.array([[]],dtype=int)'''
	assert A.shape[1] == B.shape[0]

	X = sp.zeros((A.shape[0], B.shape[1]), dtype=sp.int64)
	for r in range(A.shape[0]):
		for c in range(B.shape[1]):
			for j in range(B.shape[0]):
				X[r,c] += A[r,j]*B[j,c]
			X[r,c] %= MOD
	return X

def matModPow(A,e,MOD):
	''' Returns the matrix power A^e modulo MOD. A is a square
	sp.array([[]],type=int), e and MOD are integers'''
	assert A.shape[0] == A.shape[1]
	if e == 0:
		return sp.eye(A.shape[0], dtype=sp.int64)
	if e == 1:
		return A

	X = matModPow(A,e//2,MOD)
	X = matModMult(X,X,MOD)
	if (e%2 == 1):
		X = matModMult(X,A,MOD)
	return X

def matModInverse(A,p):
	''' Returns the matrix inverse A^(-1) modulo a prime p
	for square matrix A. Raises a divide by zero exception if the
	determinant of A is 0 modulo p '''
	assert A.shape[0] == A.shape[1]
