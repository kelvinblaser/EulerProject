#--------------------------------------------------------------------------
# Euler 549
#--------------------------------------------------------------------------

from Primes import MakePrimeList

def factorsInFactorial(p,n):
    pp = p
    f = 0
    while pp <= n:
        f += n // pp
        pp *= p
    return f

def sPrimePower(prime, exponent):
    top, bot = 1,1
    while factorsInFactorial(prime, top) < exponent:
        top *= 2
    while top - bot > 1:
        mid = (top + bot) // 2
        if factorsInFactorial(prime, mid) < exponent:
            bot = mid
        else:
            top = mid
    return top

def S(n):
    primes = MakePrimeList(n)
    s = [0]*(n+1)
    for p in primes:
        pp = p
        e = 1
        while pp <= n:
            sPrime = sPrimePower(p,e)
            for x in range(pp,n+1,pp):
                if sPrime > s[x]:
                    s[x] = sPrime
            pp *= p
            e += 1
    print s[:min(len(s), 20)]
    return sum(s)
            
if __name__ == '__main__':
    print 'S(100) = {0}'.format(S(100))
    print 'S(10^8) = {0}'.format(S(10**8))