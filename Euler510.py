# Euler 510
# Kelvin Blaser 	2019.01.14
#
#  Done some geometry.  We are looking for all a,b,c fitting the limits where
#  c = ab / (a+b +2sqrt(ab))
#
#  Can paramatrize a = x^2 * z, b = y^2 * z, c = z * (xy)^2 / (x+y)^2
#  where gcd(x,y) = 1.  If gcd(x,y) is not one, move the common factor to z
#  If what is left in a and b are not squares, we don't get an integer solution
#
#  This is an injective parametrization
#
#
#  Looks like iterating and checking gcd is faster than stern-brocot.  Uses less
#  memory too.

from fractions import gcd
from Primes import intRoot
import sys
import time

def S(n):
    r = intRoot(intRoot(n)) + 1
    # Use Stern-Brocot to generate coprime pairs
    ans = fromPrimitive(1,1,n)
    sb = [(0,1,1,1)]
    while len(sb) > 0:
        n1, d1, n2, d2 = sb.pop()
        if d1 + d2 <= r:
            ans += fromPrimitive(n1+n2, d1+d2, n)
            sb.append((n1, d1, n1+n2, d1+d2))
            sb.append((n1+n2, d1+d2, n2, d2))
    return ans
    
def S2(n):
    r = intRoot(intRoot(n)) + 1
    # Iterate to find coprime pairs -  not sure which of these two is faster.
    ans = 0
    for x in range(1,r+1):
        for y in range(1,x+1):
            if gcd(x,y) != 1: continue
            a = x**2 * (x+y)**2
            k = n // a
            if k == 0: break
            b = y**2 * (x+y)**2
            c = x*x*y*y
            ans += T(k) * (a + b + c)        
    return ans
    
def fromPrimitive(x,y,n):
    a = ((x+y)*x)**2
    b = ((x+y)*y)**2
    c = (x*y)**2
    
    g = n // b
    
    return T(g) * (a + b + c)
    
def T(n):
    return (n*(n+1))//2
    
if __name__ == '__main__':
    print 'S(5) =', S(5)        # Should be 9
    print 'S(100) =', S(100)    # Should be 3072
    print 'S(10^9) =', S(10**9)
    print 'S(10^12) =', S(10**12)
    sys.stdout.flush()
    start = time.clock()
    ans = S2(10**16)
    end = time.clock()
    print 'S(10^16) =', ans, 'Took', end-start, 'seconds using iterative.'
    sys.stdout.flush()
    start = time.clock()
    ans = S(10**16)
    end = time.clock()
    print 'S(10^16) =', ans, 'Took', end-start, 'seconds using Stern-Brocot.'