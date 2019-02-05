from Primes import MakePrimeList
from fractions import Fraction
from bisect import bisect
import scipy as sp

def Euler500(N,MOD=500500507):  # Num divisors = 2^N
    ps = MakePrimeList(N*sp.log(N)*2)[:N]
    a = [0]*N
    ans = 1
    # least_ix[y] is the smallest index in a[:] which has value y
    least_ix = [0]*int(2+sp.log(1+sp.log(ps[-1])/sp.log(2))/sp.log(2))
    for x in xrange(N):
        m = [(ps[least_ix[y]]**(2**y),y)
             for y in range(sum(z != 0 for z in least_ix)+1)]
        m.sort()
        #if x%1000 == 0:
        #    print x, least_ix, [z[0] for z in m]
        multiplier, y = m[0]  # y is the index in least_ix with the smallest multiplier
        least_ix[y] += 1
        ans *= multiplier
        ans %= MOD
    return ans

if __name__ == '__main__':
    print Euler500(4)
    print Euler500(500500)
