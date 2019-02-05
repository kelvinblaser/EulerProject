# Euler 509 - Divisor Nim
#
# Grundy score for a single pile of size n is the number of factors of 2 in the
# prime factorization of n.  Suppose n = 2^a (2k+1).  Can show that any divisor
# d = 2^b (2l+1) will admit n-d = 2^b * ( 2^(a-b) (2j + 1) - 1)
# if b < a, then n-d has b factors of 2 because the second term is odd.  If 
# b - a, then n-d has more than a factors of 2 because the second term is even.
# Thus, the minimum excluded number of factors of 2 is a.

from collections import defaultdict
from math import log

def grundyDistribution(N):
    maxPowerTwo = int(log(N)/log(2)) + 1
    gd = [0]*(maxPowerTwo+1)
    for exponent in range(maxPowerTwo+1):
        p2 = 2**exponent
        gd[exponent] = (N // p2) - (N // (p2*2))
    return gd
        
def S(N):
    gd = grundyDistribution(N)
    totalDistribution = defaultdict(int)
    for x1 in range(len(gd)):
        for x2 in range(len(gd)):
            for x3 in range(len(gd)):
                totalDistribution[x1^x2^x3] += gd[x1]*gd[x2]*gd[x3]
    #print gd
    #print totalDistribution
    return N*N*N - totalDistribution[0]
    
if __name__ == '__main__':
    print 'S(10) = {0}'.format(S(10))
    print 'S(100) = {0}'.format(S(100))
    s = S(123456787654321)
    print 'S(123456787654321) = {0} = {1} MOD 1234567890'.format(s, s%1234567890)