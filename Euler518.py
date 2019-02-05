#-------------------------------------------------------------------
# Euler 518
#-------------------------------------------------------------------

from Primes import MakePrimeList, Miller_Rabin

def rootGreatestSquareDivisorList(N):
    sd = [1]*(N+1)
    for x in range(2,N):
        xx = x*x
        if xx > N: break
        for y in range(xx, N+1, xx):
            sd[y] = x
    return sd
    
def isDigitPowTen(n):
    while n >= 100:
        if not n % 10 == 0:
            return False
        n /= 10
    return True

def S(N):
    primes = MakePrimeList(N)
    squareDivisors = rootGreatestSquareDivisorList(N)
    s = 0
    for n,a in enumerate(primes):
        if isDigitPowTen(n):
            print n, a, s
        ap = a + 1
        den = squareDivisors[ap]
        num = den+1
        while True:
            bp = ap*num // den
            cp = ap*num*num // (den*den)
            if cp > N: break
            if Miller_Rabin(bp-1) and Miller_Rabin(cp-1):
                s += a + bp + cp - 2
            num += 1
            
        #for b in primes[n+1:]:
        #    if (b+1)*(b+1) >= (N+1)*(a+1):
        #        break
        #    c = (b+1)*(b+1) // (a+1) - 1
        #    if (a+1)*(c+1) == (b+1)*(b+1) and Miller_Rabin(c):
        #        s += a + b + c
    return s
    
if __name__ == '__main__':
    print 'S(100) = {0}'.format(S(100))
    print 'S(10^8) = {0}'.format(S(10**8))