# Euler 625
#
#   ans = 551614306


def T(n):
    return n*(n+1)//2

class OClass:
    def __init__(self, m):
        self.cache = {1:1, 2:2, 3:4}
        self.MOD = m
    def __call__(self, n):
        try:
            return self.cache[n]
        except KeyError:
            pass
        
        ans = T(n) - n + n//2
        r = int(n**(0.5))
        while (r+1)*(r+1) <= n:
            r += 1
        
        for k in range(2, r):
            ans -= self(n//k)
            ans -= (n//k - n//(k+1))*self(k)
        
        ans -= self(n//r)
        ans -= (n//r - r)*self(r)
        
        self.cache[n] = ans % self.MOD  
        return self.cache[n]
        
class GClass:
    def __init__(self, m):
        self.ones = OClass(m)
        self.MOD = m
    def __call__(self, n):
        r = int(n**(0.5))
        while (r+1)*(r+1) <= n:
            r += 1
            
        ans = 0
        for k in range(1,r):
            ans += k*self.ones(n//k)
            ans += (T(n//k) - T(n//(k+1)))*self.ones(k)
        ans += r*ones(n//r)
        ans += (T(n//r) - T(r))*self.ones(r)
        return ans % self.MOD
        
if __name__ == '__main__':
    ones = OClass(998244353)
    for x in range(1,11):
        print x, ones(x)
        
    G = GClass(998244353)
    print 'G(10)    = {0};\t cache length: {1}'.format(G(10), len(G.ones.cache))
    print 'G(100)   = {0};\t cache length: {1}'.format(G(100), len(G.ones.cache))
    print 'G(10000) = {0};\t cache length: {1}'.format(G(10000), len(G.ones.cache))
    print 'G(10^8)  = {0};\t cache length: {1}'.format(G(10**8), len(G.ones.cache))
    print 'G(10^11) = {0};\t cache length: {1}'.format(G(10**11), len(G.ones.cache))