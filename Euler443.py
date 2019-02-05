################################################################################
# Euler 443 - GCD Sequence
# Kelvin Blaser      2015.02.21
#
################################################################################
from Primes import MakePrimeList, Miller_Rabin

def g(N):
    ps = MakePrimeList(int((2*N+2)**(0.5)))
    n = 9
    n_last = 9
    while n <= N:
        #print n
        z = 2*n-1
        if Miller_Rabin(z):
            k = (z-3)/2
        for p in ps:
            if z%p == 0:
                k = (p-3)/2
                break
        n_last = n
        n += k + 1
    return 2*n_last + N

if __name__ == '__main__':
    print 'g(1000) =', g(1000)
    print 'g(1000000) =', g(1000000)
    print 'g(10^15) =', g(10**15)
