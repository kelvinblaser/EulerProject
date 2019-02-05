# Euler 550 - Divisor game
#
# Strategy is divide and conquer.  A game with 10^12 piles of stones is 
# is equivalent to the nim-sum of two games with 5x10^11 piles of stones. 
#
# If I know the distribution of sprague-grundy scores among all games of x and
# all games of y piles of stones, I can calculate the distribution of scores
# for all games of x+y piles of stones.  
#
# I just need to calculate the distribution of scores for 1 pile of stones for 
# all sizes of piles
#
# A little thought will show that the sprague-grundy score for a pile of size
# n only depends on the number of prime factors.  If the two piles each have a
# subset of n's prime factors, then they are an available move to make.  Each 
# new pile will have a number of prime factors less than n's, and when a pile 
# has only one prime factor (i.e. is prime) it is done and no longer a candidate
# for a move.  (Note, the number of prime factors includes multiplicity. 9 has 
# two prime factors, 12 has three prime factors, etc.)

from collections import defaultdict
from fractions import gcd

def lcm(a,b):
    return a*b // gcd(a,b)

def mex(scores):
    s = list(scores)
    s.sort()
    for ix in range(len(s)):
        if s[ix] != ix:
            return ix
    return len(s)

class DivisorGame:
    def __init__(self, n):
        self.n = n
        self.MOD = 987654321
        self.cache = {}
        self.cache[1] = self.onePileGrundyDistribution()
        
    def onePileGrundyDistribution(self):
        grundyDistribution = defaultdict(int)
        primeDivisorDistribution = defaultdict(int)
        primeDivisors = [0]*(self.n+1)
        for x in range(2, self.n+1):
            if primeDivisors[x] == 0: # x is a prime number
                for y in range(x, self.n+1, x):
                    z = y
                    while z % x == 0:
                        primeDivisors[y] += 1
                        z //= x
            primeDivisorDistribution[primeDivisors[x]] += 1
        
        grun = defaultdict(int)
        for x in range(1, max(primeDivisorDistribution.keys())+1):
            scores = set()
            for d1 in range(1,x):
                for d2 in range(d1,x):
                    scores.add(grun[d1]^grun[d2])
            grun[x] = mex(scores)
            grundyDistribution[grun[x]] = primeDivisorDistribution[x]
        return grundyDistribution
        
    def grundyDistribution(self, k):
        try:
            return self.cache[k]
        except KeyError:
            pass
            
        gd1 = self.grundyDistribution(k//2)
        gd2 = self.grundyDistribution(k - k//2)
        gd = defaultdict(int)
        for g1 in gd1.keys():
            for g2 in gd2.keys():
                gd[g1^g2] += gd1[g1] * gd2[g2]
        for g in gd.keys():
            gd[g] %= self.MOD
        self.cache[k] = gd
        return gd
    
    def __call__(self, k):
        gd = self.grundyDistribution(k)
        return (pow(self.n-1, k, self.MOD) - gd[0])%self.MOD
        
if __name__ == '__main__':
    divGame10 = DivisorGame(10)
    print 'f(10,5) = {0}'.format(divGame10(5))
    divGame10_7 = DivisorGame(10**7)
    print 'f(10^7, 10^12) = {0}'.format(divGame10_7(10**12))
    
    