################################################################################
# Euler 515 - Disonant Numbers
# Kelvin Blaser      2015.05.19
#
#  Conjecture:
#   d(p,p-1,k) = (k-1)^-1 mod p.
# Not sure how to prove, but it works in every case I've tried and passes the 
# test examples given.
################################################################################
from Primes import Miller_Rabin

def D(a,b,k):
    ret = 0
    for p in range(a,a+b):
        if not Miller_Rabin(p):
            continue
        ret += pow(k-1,p-2,p)
    return ret

if __name__ == '__main__':
    print 'D(101,1,10) = %d'%(D(101,1,10),)
    print 'D(10^3,10^2,10^2) = %d'%(D(10**3,10**2,10**2),)
    print 'D(10^6,10^3,10^3) = %d'%(D(10**6,10**3,10**3),)
    print 'D(10^9,10^5,10^5) = %d'%(D(10**9,10**5,10**5),)
