###############################################################################
# Euler 333 - Special Partitions
# Kelvin Blaser     2015.1.21
#
# Only certain numbers are allowed to be in the partition.  
###############################################################################
from Primes import MakePrimeList
import time

def make23nums(n):
    twos = threes = 0
    x = 1
    nums = []
    while x < n:
        twos = 0
        while x < n:
            nums.append(x)
            twos += 1
            x *= 2
        threes += 1
        x = 3**threes
    nums.sort()
    return nums

def isValidPartitionPair(a,b,n):
    if a + b >= n:
        return False
    if a%b == 0 or b%a == 0:
        return False
    return True

def makeValidPartitions(n):
    nums = make23nums(n)
    P = [0 for x in xrange(n)]

    def _makeValidPartitions(available, total):
        P[total] += 1

        #available = [x for x in available if x < n-total]
        while available:
            x = available.pop()
            new_available = [y for y in available if
                             #isValidPartitionPair(x,y,n-total)]
                             x+y < n-total and x%y != 0 and x%y != 0]
            _makeValidPartitions(new_available, total+x)

        return
        
    _makeValidPartitions(nums, 0)
    num_parts = 0
    for x in xrange(n):
        num_parts += P[x]
    print 'Total Partitions: %d'%(num_parts,)
    return P


def Euler333(n):
    ps = MakePrimeList(n)
    parts = makeValidPartitions(n)
    return sum(long(p) for p in ps if parts[p]==1)
                      

if __name__ == '__main__':
    start = time.clock()
    print 'Sum N(P(q)==1 | q < 100) = %d\tElapsed Time: %d'%(Euler333(100),time.clock()-start)
    print 'Sum N(P(q)==1 | q < 10^6) = %d\tElapsed Time: %d'%(Euler333(10**6),time.clock()-start)

