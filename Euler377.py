# Euler 377
# Kelvin Blaser     2019.02.06
#
# For n >= 81, every digital partition has at least 9 parts. That means that for
# every partition with digit d in the first spot, there is a partition with d in 
# the second slot (might be the same partition), a partition with d in the third
# slot, etc.
#
# I only need to find how many partitions have a d in the first slot, for 
# 1 <= d <= 9. This is done by matrix exponentiation.  The number of partitions
# of n with d in the first slot is exactly the number of partitions of n-d. 
# Thus the problem is reduced to finding the number of partitions of m = n-d
#
# The number of partitions of m is equal to the sum of the number of partitions
# of m with d in the first slot, for 1 <= d <= 9.  Denoted by p(m), we have
#       p(m) = p(m-1) + p(m-2) + ... + p(m-9)
#
# If I consider the vector P(m) = (p(m), p(m-1), p(m-2), ... , p(m-8)), I see 
# that I can calculate that vector from the previous vector 
# P(m-1) = (p(m-1), p(m-2), ..., p(m-9)) by multiplying by a transition matrix T
#
#           1 1 1 1 1 1 1 1 1                   1
#           1 0 0 0 0 0 0 0 0                   0
#           0 1 0 0 0 0 0 0 0                   0
#           0 0 1 0 0 0 0 0 0                   0
#       T = 0 0 0 1 0 0 0 0 0            P(0) = 0
#           0 0 0 0 1 0 0 0 0                   0
#           0 0 0 0 0 1 0 0 0                   0
#           0 0 0 0 0 0 1 0 0                   0
#           0 0 0 0 0 0 0 1 0                   0
#
# I can get p(m) for large values of m by matrix exponentiation
#
#       P(m) = T^m * P(0)
#
# Again, this only works for n > 80. 13^i > 81 for i >= 2, so for 13^1 I need to 
# enumerate all of the partitions. There are less than 2^12 = 4096 of these, so 
# that won't take too long.

from Primes import matModPow, matModMult
import scipy as sp

MOD = 10**9

def partitionSum(n):
    if n < 81: return sum(partitions(n))%MOD
    
    # Transition matrix
    T = sp.zeros((9,9), dtype=sp.int64)
    T[0,:] = sp.ones((1,9), dtype=sp.int64)
    for x in range(8):
        T[x+1,x] = 1
    
    # Initial partition counts; 1 way to partition 0, 0 ways to partition negatives    
    p0 = sp.zeros((9,1), dtype=sp.int64)
    p0[0,0] = 1
    
    # Find p(n-1)
    p = matModMult( matModPow(T, n-1, MOD) , p0, MOD) 
    
    s = 0
    for d in range(1,10):
        s += d * p[d-1,0]
    s *= 111111111
    
    return s % MOD
    
def partitions(n):
    if n == 0:
        yield 0
        return
    for d in range(min(n,9),0,-1):
        for x in partitions(n-d):
            yield 10*x + d
            
def Euler377():
    return sum(partitionSum(13**i) for i in range(1, 18)) % MOD
        

if __name__ == '__main__':
    parts = list(partitions(5))
    parts.sort()
    print 'Partitions of 5\n{0}'.format('\n'.join('{0:5}'.format(x) for x in parts))
    print ''
    print 'f(5) = {0}'.format(partitionSum(5))
    print 'f(13) = {0}'.format(partitionSum(13))
    print ''
    print 'Sum : {0}'.format(Euler377())