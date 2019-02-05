###############################################################################
# Euler 492 - Exploding Sequence
# https://projecteuler.net/problem=492
#
# Kelvin Blaser     2014.12.15, 2015.1.7
#
# Sequence to calculate:
#           a_(n+1) = 6a_n^2 + 10a_n + 3,  a_1 = 1
# With the substitution x = 6a + 5, this becomes:
#           x_(n+1) = x_n^2 - 2
#
# This quadratic map has a known solution outlined in the paper at:
#  http://www.sciencedirect.com/science/article/pii/S0012365X03001584
#
#   x_n = alpha^(2^n) + beta^(2^n) where alpha and beta are the roots of
#        z^2 - x_0 z + 1 = 0
#
# The algorithm works by solving this equation in the ring Z/pZ .
#
###############################################################################

from Euler import tonelliShanks, isQuadResidue
from Primes import Miller_Rabin

def x2a(x,p):
    ''' Converts x to a using the substitution x = 6a+5 '''
    sixInv = pow(6,p-2,p)
    return (sixInv * (x-5))%p

def powRadMod(unit,radco,rad,e,MOD):
    if e == 0:
        return 1,0
    if e == 1:
        return unit, radco
    xunit, xradco = powRadMod(unit,radco,rad,e//2,MOD)
    yunit = xunit*xunit + xradco*xradco*rad
    yradco = xunit*xradco*2
    if e%2 == 0:
        return yunit%MOD,yradco%MOD
    zunit = yunit*unit + yradco*radco*rad
    zradco = yunit*radco + unit*yradco
    return zunit%MOD,zradco%MOD

def xnModP(n,p):
    ''' The guts of the algorithm. This calculates
                x_n = alpha^(2^n) + beta^(2^n) mod p
        See module documentation for sources
    '''
    x,y = powRadMod(11,3,13,pow(2,n-1,p*p-1),p)
    x *= 2*pow(pow(2,pow(2,n-1,p-1),p),p-2,p)
    x %= p
    return x

def B(x,y,n):
    ans = 0
    for p in xrange(x, x+y+1):
        #if p%10000 == 0:
            #print p-x, ans
        if not Miller_Rabin(p):
            continue
        ans += x2a(xnModP(n,p),p)
    return ans

if __name__ == '__main__':
    print 'B(10^%d, 10^%d, 10^%d) = %d'%(9,3,3,B(10**9,10**3,10**3))
    print 'B(10^%d, 10^%d, 10^%d) = %d'%(9,3,15,B(10**9,10**3,10**15))
    print 'B(10^%d, 10^%d, 10^%d) = %d'%(9,7,15,B(10**9,10**7,10**15))
