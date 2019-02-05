###############################################################################
# Euler 221 - Alexandrian Integers
# Kelvin Blaser     2015.1.4
#
# Since A=pqr is positive, we know that exactly 0 or 2 of p,q and r are
# negative.  We can rearrange the equation and substitute A = pqr to get
#       1 = qr + pr + pq
# This shows that not all of p,q,r can be positive. Let q and r be negative
# and replace them with their negative values.
#       1 = qr - pr - pq
# The positive value p must be less than q and r, so with out loss of generality
# let p < q < r.
# Let q = p + k, then
#   1 = (p+k-p)r - p(p+k)   =>   r = (1 + p(p+k))/k = (p^2+1)/k + p
# Since r is an integer, k has to divide p^2+1.  We can run over p, and the
# divisors of p^2+1 to find the Alexandrian integers.
#           A = p(p+k)((p^2+1)/k + p)
# Also note that for every k, the divisor d = (p^2+1)/k gives the same
# Alexandrian integer, so we only need to check divisors up to
# floor(sqrt(p^2+1)) = p.
#
# To limit the p-values to run over, we see that A = p(p+k)(p^2+1)/k + p) > 4p^3
# for all k.  Thus once we have 150000 Alexandrian integers, we have an upper
# limit on p, namely (a/4)^(1/3) where a is the current 150000th Alexandrian
# integer.
###############################################################################

def Euler221(n):
    alexandrian_ints = []
    p = 1
    pmax = 2
    while p <= pmax:
        p21 = p*p+1
        if p%500 == 0:
            print '\t%d, %d, len=%d'%(p,int(pmax), len(alexandrian_ints))
            alexandrian_ints.sort()
        for k in range(1,p+1):
            if not p21%k == 0:  # Is there a faster way to get the 
                continue        # divisors of p^2+1?
            alexandrian_ints.append(p*(p+k)*(p21/k + p))
        if len(alexandrian_ints) >= n:
            #alexandrian_ints.sort()
            pmax = (alexandrian_ints[n-1] / 4.0)**(1./3.)
        else:
            pmax = p+2
        p += 1
    alexandrian_ints.sort()
    return alexandrian_ints[n-1], len(alexandrian_ints), p

if __name__ == '__main__':
    print Euler221(6)
    print Euler221(100)
    print Euler221(1000)
    print Euler221(150000)
