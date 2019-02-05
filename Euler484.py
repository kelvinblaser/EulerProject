# Euler 484 - Arithmetic Derivative
# projecteuler.net/problem=484
# Kelvin Blaser     2014.11.23

import Primes
reload(Primes)
import scipy as sp
import time

prime_pi = Primes.Prime_Pi()
'''Q_mem = {}
def Q(n,primes):
    #print 'Calculating Q[%d]'%(n,)
    if n >= 10**7:
        PRINT = True
    else:
        PRINT = False
    try:
        return Q_mem[n]
    except KeyError:
        pass
    ans = n
    r = 1
    while r <= len(primes) and sp.prod(primes[:r]) <= n:
        sign = (-1)**r
        count = 0
        for c in Primes.combProdLessThan(primes, r, n):
            ans += sign * (n//int(sp.prod(c)))
            count += 1
        if PRINT:
            print '%d from list of len %d: %d times; \t%d : %d'%(r,len(primes),
                                                            count, n, ans)
        r += 1
    Q_mem[n] = ans
    #print '\tQ[%d] = %d'%(n,ans)
    return ans
'''
def Q(n,ix,primes):
    '''Make sure to give it exactly the right primes.  p <= sqrt(N)'''
    if primes[ix] > n:
        return 0
    ans = n // primes[ix]
    jx = ix + 1
    while jx < len(primes):
        if primes[jx] > n:
            break
        ans -= Q(n // primes[ix], jx ,primes)
        jx += 1
    return ans

def f(p,r):
    ''' Returns gcd(p^r,(p^r)') if p is prime.'''
    if r%p == 0:
        return p**r
    return p**(r-1)

def F(n,ix,primes):
    #print 'Calculating F(%d,%d)'%(n,primes[ix])
    if primes[ix] > n:
        return 1
    rt = sp.sqrt(n)
    if primes[ix] > rt:
        return prime_pi(n,primes) - prime_pi(primes[ix]-1,primes) + 1

    rt = int(rt)
    # Calculate pi(n)-pi(sqrt(n))+1 = Q(n)
    top = len(primes)- 1
    bottom = 0
    while top - bottom > 1:
        mid = (top + bottom)/2
        if primes[mid] > rt:
            top = mid
        else:
            bottom = mid
    ans = n - sum(Q(n, ix, primes[:top]) for ix in range(top))
    #ans = 0
    # Calculate sum over F's
    jx = ix
    while primes[jx] <= rt:
        pr = p = primes[jx]
        r = 1
        while pr <= n:
            if r%p == 0:
                fpr = pr
            else:
                fpr = pr / r
            ans += fpr * F(n//pr, jx+1, primes)
            r += 1
            pr *= p
        jx += 1
    #print '\tF(%d,%d) = %d'%(n,primes[ix],ans)
    return ans

def Euler484a(N):
    start = time.clock()
    p_max = int(sp.sqrt(N)+1000)
    primes = Primes.MakePrimeList(p_max)
    print 'Primes up to %d calculated.  %d primes'%(p_max, len(primes))
    ans = F(N,0,primes)
    end = time.clock()
    print '%f seconds'%(end - start,)
    return ans

def make_mobius(n,primes):
    mob = sp.ones(n+1,dtype=int)
    for x in primes:
        for y in range(x*x,n+1,x*x):
            mob[y] = 0
        for y in range(x,n+1,x):
            mob[y] *= -1
    return mob

def make_marten(mobius):
    marten = 0*mobius
    for i in range(1,len(mobius)):
        marten[i] = marten[i-1]+mobius[i]
    return marten

def make_dfact(n,primes):
    dfact = {}
    r = 1
    while r <= len(primes) and sp.prod(primes[:r]) <= n:
        for c in Primes.combProdLessThan(primes, r, n):
            d = int(round(sp.prod(c))+0.01)
            dfact[d] = c
        r += 1
    return dfact

def Euler484(N):
    rt = int(sp.sqrt(N)+0.0001)
    primes = Primes.MakePrimeList(rt)
    mobius = make_mobius(rt, primes)
    marten = make_marten(mobius)
    d_fact = make_dfact(rt, primes)
    marten_mem = {}

    def Marten(n):
        if n < len(marten):
            return marten[n]
        try:
            return marten_mem[n]
        except KeyError:
            pass
        ans = 1
        r = int(sp.sqrt(n)+0.0001)
        for g in range(2,r+1):
            ans -= Marten(n//g)
        for z in range(1,r):
            ans += ((n//z) - (n//(z+1))) * Marten(z)
        if n//r != r:
            ans += ((n//r) - (n//(r+1))) * Marten(r)
        marten_mem[n] = ans
        return ans
    
    def sqf(n):
        ans = n
        r = int(sp.sqrt(n)+0.0001)
        for d in range(2,r+1):
            ans += mobius[d]*(n//(d*d))
        return ans

    def F(n):
        if n == 1:
            return 1
        ans = sqf(n)
        r = int(sp.sqrt(n)+0.0001)
        for d in range(2,r+1):
            if mobius[d] != 0:
                c = list(d_fact[d])
                ans -= mobius[d] * F1(c ,[2]*len(c), n//(d*d))
        return ans

    def F1(p,r,n):
        if n == 0:
            return 0
        if not p:
            return F(n)
        p0 = p.pop(0)
        r0 = r.pop(0)
        if p0 == 2 and r0 == 2:
            return 4*F1(p,r,n)
        pn = p[:]
        rn = r[:]
        pn.insert(0,p0)
        rn.insert(0,1)
        ans = f(p0,r0) * F1(p,r,n)
        n /= p0
        s = 0
        while n > 0:
            ans -= f(p0,r0+s) * F1(pn,rn,n)
            ans += f(p0,r0+s+1) * F1(p,r,n)
            n /= p0
            s += 1
        return ans

    def f(p,r):
        if r%p == 0:
            return p**r
        return p**(r-1)

    return F(N), sqf, F, F1

if __name__ == '__main__':
    E20 = Euler484(20)
    print 'F(20) = %d'%(E20,)
    E100 = Euler484(100)
    print 'F(100) = %d'%(E100,)
