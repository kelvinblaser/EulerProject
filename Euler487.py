# Euler 487 - Sums of power sums
# Kelvin Blaser    2014.16.12
from Primes import Miller_Rabin

def f(k,n,p):
    ans = 0
    l = n%p
    if l <= p//2:
        for i in xrange(1, n%p+1):
            ans += pow(i,k,p)
    else:
        for i in xrange(l+1,p):
            ans -= pow(i,k,p)
        if n%(p-1) == 0:
            ans -= 1
    if n%(p-1) == 0:
        ans -= n // p
    return ans % p

def S(k,n,p):
    return ((n+1)*f(k,n,p) - f(k+1,n,p))%p

def Euler487(k,n,x,y):
    ans = 0
    for p in range(x,x+y+1):
        if not Miller_Rabin(p):
            continue
        s = S(k,n,p)
        print p,s
        ans += s
    return ans

if __name__ == '__main__':
    print S(4,100,10**15)
    print Euler487(10000,10**12,2*10**9, 2000)
