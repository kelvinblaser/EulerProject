###############################################################################
# Euler 364 - Comfortable Distance
# Kelvin Blaser     2015.1.6
#
# A few observations:
# 1. People fill the seats until there are no seats with two empty neighbors
# 2. At this point, the empty seats in the row will be either alone or in sets
#    of 2.
# 3. Also at this point, the end points can either be filled or adjacent to a
#    filled seat.  There can be zero, one or two empty end points.  I will treat
#    each case separately.
# 4. At this point, if there are x internal sets of one and y sets of two
#    empty seats, the number of ways to finish filling the seats is independent
#    of the order of the sets.
#
# The strategy is, for each endpoint case, enumerate the different possible
# sets of x and y, figure out how many ways to get to that point, then multiply
# by the number of different ways to order the x+y sets, then multiply by the
# number of ways to finish filling the x+y sets.
#
# Q.  With h open end seats.
# ------------------------------    [ ][o] ...... [o][ ] h=2
#                                   [o][ ] ...... [o][ ] h=1
#                                   [o][ ] ...... [ ][o] h=0
# There are x seats in alone blocks, 2y seats in blocks of two, and x+y-1 seats
# dividing these blocks.
#         x + 2y + (x+y-1) + h + 2 = n
#         2x + 3y + h + 1 = n
# Clearly y has the same parity as n-h-1, and runs from 0 to (n-h-1)//3.
#
# For any given y, there are x+y+1 blocks filled to get to this point which can
# be filled in any order.  There are (x+y) Choose y ways to order the blocks.
# The number of ways to fill the blocks is calculated as follows. There are
# (y+h)! ways to order the y blocks of two plus the h end seats.  For each
# block of two, there are two choices to fill, creating block of one.  This
# gives a factor of 2^y.  Finally the last x+y blocks of one can be filled in
# any order
#
#   Q(n,h) = sum_over_possible_y (  (x+y+1)! Choose(x+y,y) (y+h)! 2^y (x+y)! )
#
# T.  Total
# --------------
#   T(n) = Q(n,2) + 2Q(n,1) + Q(n,0)
###############################################################################
import numpy as np

MOD = 100000007

class FactorialMOD(object):
    ''' A factorial object which returns n! % MOD, and caches the calculated
        results for future use. '''
    def __init__(self, MOD):
        self.MOD = MOD
        self.cache = {0 : 1, 1 : 1}

    def __call__(self, n):
        try:
            return self.cache[n]
        except KeyError:
            pass
        m = max(self.cache.keys())
        x = self.cache[m]
        for i in xrange(m+1, n+1):
            x *= i
            x %= self.MOD
            self.cache[i] = x
        return self.cache[n]
fact = FactorialMOD(MOD)

def chooseMOD(n,k):
    num = fact(n)
    den = (fact(k)*fact(n-k))%MOD
    return (num * pow(den,MOD-2,MOD))%MOD

def Q(n,h):
    ans = 0
    ymin = (n+h+1)%2
    for y in xrange(ymin, (n-1-h)//3+1, 2):
        x = (n-1-h-3*y)/2
        # (x+y+1)! Choose(x+y,y) (y+h)! 2^y (x+y)!
        term = (fact(x+y+1) * chooseMOD(x+y,y) * fact(y+h))%MOD
        term *= pow(2,y,MOD) * fact(x+y)
        term %= MOD
        #print 'Q:\tx=%d\ty=%d\tterm=%d'%(x,y,term)
        ans += term
        ans %= MOD
    return ans
    

def T(n):
    ''' Calculates the ways to fill the seats.  The seats can fill until there
    are only blocks of size one or two empty seats in three different ways:
    with 2 open endpoint seats (Q(n)), with 1 open endpoint seat (R(n)) or with
    no open endpoint seats (S(n)). '''
    return (Q(n,0) + 2*Q(n,1) + Q(n,2))%MOD

if __name__ == '__main__':
    print 'T(%d) = %d mod %d'%(4,T(4),MOD)
    print 'T(%d) = %d mod %d'%(10,T(10),MOD)
    print 'T(%d) = %d mod %d'%(1000,T(1000),MOD)
    print 'T(%d) = %d mod %d'%(1000000,T(1000000),MOD)
