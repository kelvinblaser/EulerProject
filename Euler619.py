# Euler 619
# Square subsets


from Primes import MakePrimeList, Prime_Pi
from collections import defaultdict

class SquareSubset:
    def __init__(self, N=None):
        if not N: N = 1000
        self.N = 0
        self.primes = []
        self.squareFreePrimeList = defaultdict(list)
        self.squareFreeNumber = []
        self._updatePrimeList(N)
        self.MOD = 10**9+7
        
    def _updatePrimeList(self,N):
        if N <= self.N: return
        self.primes = MakePrimeList(N)
        self.squareFreeNumbers = list(range(N+1))
        self.squareFreePrimeList = defaultdict(list)
        for p in self.primes:
            pp = p*p
            if p > N: break
            for x in range(p, N+1, p):
                while self.squareFreeNumbers[x] % pp == 0:
                    self.squareFreeNumbers[x] /= pp
                if self.squareFreeNumbers[x] % p == 0:
                    self.squareFreePrimeList[x].append(p)
        #self.squareFree = set()
        #for x in range(1, N+1):
        #    self.squareFree.add(tuple(squareFreePrimeList[x]))
        
    def _multiplyPrimeTuples(self, t1, t2):
        primeCount = defaultdict(int)
        for p in t1:
            primeCount[p] += 1
        for p in t2:
            primeCount[p] += 1
        newPrimes = [p for p in primeCount.keys() if primeCount[p]%2 == 1]
        newPrimes.sort(reverse=True)
        return tuple(newPrimes)
                    
    def __call__(self, a, b):
        ''' Returns C(a,b) '''
        assert(a > 0)
        assert(b >= a)
        self._updatePrimeList(b)
        ans = 0
        # build list of prime tuples for sorting
        squareFreePrimeTuples = []
        for x in range(a,b+1):
            squareFreePrimeTuples.append(tuple(self.squareFreePrimeList[x][::-1]))
        squareFreePrimeTuples.sort()
        #print squareFreePrimeTuples
        
        # Consider each number in turn based on its largest prime
        ppi = Prime_Pi()
        tuplesSeen = defaultdict(bool)
        tuplesSeen[tuple([])] = True
        maxNumTuples = 1
        for p in self.primes[ppi(b,self.primes)-1::-1]:
            print a,b,p, maxNumTuples, len(tuplesSeen)
            # Go through all tuples with largest prime
            while squareFreePrimeTuples and len(squareFreePrimeTuples[-1]) > 0 and p == squareFreePrimeTuples[-1][0]:
                t = squareFreePrimeTuples.pop()
                # If seen it, count it.
                if tuplesSeen[t]:
                    ans += 1
                # Otherwise, create new tuples we've seen
                else:                    
                    for t1 in tuplesSeen.keys():
                        newTuple = self._multiplyPrimeTuples(t,t1)
                        tuplesSeen[newTuple] = True
            # Remove all tuples with p, because now we know we will never get rid of p anyways
            maxNumTuples = max(maxNumTuples, len(tuplesSeen))
            for t in tuplesSeen.keys():
                if len(t) > 0 and t[0] == p:
                    del tuplesSeen[t]
        # Don't forget the empty tuples at the end
        ans += len(squareFreePrimeTuples)
        print maxNumTuples
                
        return ans, pow(2, ans, self.MOD)-1
        
        #seen = [False]*(b+1)
        #seen[1] = True
        #for x in range(a,b+1):
        #    if seen[self.squareFreeNumbers[x]]:
        #        ans += 1
        #    else:
        #        for y in range(b+1):
        #            if seen[self.squareFreeNumbers[y]]:
        #                mult = defaultdict(int)
        #                for p in self.squareFreePrimeList[x]:
        #                    mult[p] += 1
        #                for p in self.squareFreePrimeList[y]:
        #                    mult[p] += 1
        #                z = 1
        #                for p in mult.keys():
        #                    if mult[p] % 2 == 1:
        #                        z *= p
        #                if z <= b:
        #                    seen[self.squareFreeNumbers[z]] = True
        #lreturn ans, pow(2,ans,self.MOD)-1
        #for sfTuple in self.squareFree:
        #    x = 1
        #    for p in sfTuple:
        #        x *= p
        #    xx = x*x
        #    d = (b//x - (a-1)//x) - (b//xx - (a-1)//xx)
        #    delta = (-1)**len(sfTuple) * pow(2,b-a,self.MOD)
        #    ans += delta
        #    print sfTuple, x, d, delta, ans
        #return ans
        
if __name__ == '__main__':
    C = SquareSubset(10)
    print 'C(5,10)      = 2^{0}-1\t= {1}'.format(*C(5,10))
    print 'C(40,55)     = 2^{0}-1\t= {1}'.format(*C(40,55))
    print 'C(100,123) = 2^{0}-1\t= {1}'.format(*C(100,123))
    print 'C(1000,1234) = 2^{0}-1\t= {1}'.format(*C(1000,1234))
    print 'C(10000,12345) = 2^{0}-1\t= {1}'.format(*C(10000,12345))
    print 'C(100000,123456) = 2^{0}-1\t= {1}'.format(*C(100000,123456))
    print 'C(1000000,1234567) = 2^{0}-1\t= {1}'.format(*C(1000000,1234567))    