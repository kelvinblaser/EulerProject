# Euler 643

from Primes import Mobius, Mertens, Mertens2, intRoot
import time

def T(n):
    return (n*(n-1)) // 2

class Euler643:
    def __init__(self, n):
        self.mertens = Mertens(n)
        self.mobius = Mobius(intRoot(n))
        
    def f(self, n):
        ans = 0
        p2 = 2
        while p2 <= n:
            ans += self.sumTotient(n//p2)
            p2 *= 2
        return ans
    
    def sumTotient(self, n):
        if n == 1: return 0
        if n == 2: return 1
        r = intRoot(n)
        ans = 0
        for k in range(1, r+1):
            ans += self.mobius(k) * T(n//k)
            ans += T(k)*(self.mertens(max(r, n//k)) - self.mertens(max(r, n//(k+1))))
        return ans
    
if __name__ == '__main__':
    e = Euler643(100)
    print e.f(100)
    e = Euler643(10**6)
    print e.f(10**6)
    print e.f(10**6) % (10**9+7)
    e = Euler643(10**11)
    start = time.time()
    print e.f(10**11)
    end = time.time()
    print(end - start)
    print e.f(10**11) % (10**9 + 7)