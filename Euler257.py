# Euler 257 - Angle Bisectors
# Kelvin Blaser     2019.02.07
#
#------------------------------------------------------------------------------
#    GEOMETRY
#
# Let x = |AE|, then |EB| = c - x
# Angle bisector theorem says
#        x / b = (c-x) / a  => (a+b) x = bc => x = bc / (a+b)
# Similarly, let y = |AG|
#        y / c = (b-y) / a  => (a+c) y = bc => y = bc / (a+c)
#
# Ratio of areas is integer k
#       bc Sin A    (a+b)(a+c)
#   k = --------  = ----------   => kbc = (a+b)(a+c)
#       xy Sin A        bc
#
#   k <= 1   ==>  a <= 0
#   k = 4    ==>  a = b = c
#   k > 4    ==>  a > b
#
#   We only need to consider k = 2,3, and 4.  When k = 4, we have equilateral
#   triangles of which there are N
#
#------------------------------------------------------------------------------
#    GENERATING PRIMITIVE TRIPLES
#
# Can show that all primitive triples have the following form
#
#     a = (k-1)n(m-kn) / d
#     b = (m-(k-1)n)(m-kn) / d
#     c = mn / d
#
#  Here d is the gcd of the numerators and gcd(m,n) = 1
# With k = 2 and m % 2 = 0, d = 2
# With k = 3 and m % 6 = 0, d = 6
# With k = 3 and m % 6 = 2 or 4, d = 2
# With k = 3 and m % 6 = 3, d = 3
#
# Can further show that if gcd(m,n) = 1, all such a,b,c are primitive and that
# no two pairs (m,n) give the same primitive triple.  Thus we can enumerate all
# primitive triples in one-to-one fashion with m,n pairs
#
# This proof follows the one for pythagorean triples at
#   https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#
#  Solve kbc = (a+b)(a+c) for a. The quadratic disciminant must be an integer, so
#  we have to solve
#
#   (b+c)^2 + 4(k-1)bc = q^2   =>  x^2 = q^2 + k(k-1)y^2  where
#                                    x = b + (2k-1) c
#                                    y = 2c
#                                    q = 2a + b + c
#
#  Solve this equation similar to the pythagorean equation z^2 = x^2 + y^2
#
# Use the triangle inequality a+b > c, the orderint a <= b <= c and perimeter
# limit a+b+c <= N to set bounds on the appropriate m and n.
#
#------------------------------------------------------------------------------
#
# Runs in about 30 seconds

from fractions import gcd
import time

def countTriangles(N, talk=False):
    r = int((2*N)**0.5)
    while r*r > 2*N: r -= 1
    while (r+1)**2 <= 2*N: r += 1

    count = N // 3 # Equilateral triangles - case k = 4
    prims = 0
    tries = 0
    triF = 0
    abF = 0
    bcF = 0
    pF = 0
    if talk:
        tup = ('k', '  m  ', ' mMax', ' triangles', 'primatives', '  tested', '  a+b <= c', '     a > b', '     b > c', '     p > N')
        print '{} {:5} {:5} {:10} {:10} {:10} {:10} {:10} {:10} {:10}'.format(*tup)
        print '-'*90
    for k in [2,3]:
        for m in range(1, k*r+1):
            if talk and m%1000 == 0:
                tup = (k, m, k*r, count, prims, tries, triF, abF, bcF, pF)
                print '{} {:5} {:5} {:10} {:10} {:10} {:10} {:10} {:10} {:10}'.format(*tup)
            # Set some constraints to avoid testing many non-valid (m,n) pairs
            d = (2 if m%2 == 0 else 1) * (3 if k == 3 and m%3 == 0 else 1)
            nMin = max(1, int(m*(k**0.5 - 1) / ((k-1)*k**0.5)), (m - (N*d)//m - 1) // (k-1))
            nMax = m//(k+1)
            for n in range(nMin, nMax + 1):
                if gcd(m,n) != 1: continue
                a = (k-1) * n * (m - k*n)
                b = (m - (k-1)*n) * (m - k*n)
                c = m*n
                # Make sure a,b,c is primative
                g = gcd(a,gcd(b,c))
                a //= g
                b //= g
                c //= g
                # Some analysis code here to see where the most non-valid pairs
                # are failing - should help tighten up the bounds
                if talk:
                    tries += 1
                    if a+b <= c: triF += 1
                    if a > b: abF += 1
                    if b > c: bcF += 1
                    if a+b+c > N: pF += 1
                # Count them up
                if a+b > c and a <= b <= c and a+b+c <= N:
                    prims += 1
                    count += N // (a+b+c)
    return count

if __name__ == '__main__':
    start = time.clock()
    print 'Perimeter <= {0} : {1}'.format(10000,  countTriangles(10000))  # Should be 7677
    print 'Perimeter <= {0} : {1}'.format(100000, countTriangles(100000)) # Should be 92318
    #print 'Perimeter <= {0} : {1}'.format('10^8', countTriangles(10**8, True)) # 139012411
    print 'Perimeter <= {0} : {1}'.format('10^8', countTriangles(10**8, False)) # 139012411
    end = time.clock()
    print 'Took {} seconds'.format(end - start)
