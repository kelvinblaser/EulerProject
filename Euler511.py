#------------------------------------------------------------
# Euler 511
#
#------------------------------------------------------------

MOD = 10**9

class SequenceCounter:
    def __init__(self, n, k, factors):
        self.cache = {}
        self.n = n
        self.k = k
        self.factors = factors
        
    def __call__(self, m, r):
        try:
            return self.cache[(m,r)]
        except KeyError:
            pass
            
        if m == 0:
            if r == 0: return 1
            else: return 0
        
        if m == 1:
            c = 0
            for f in self.factors:
                if f%self.k == r: c += 1
            self.cache[(m,r)] = c
            return c
        
        c = 0
        x = m // 2
        for i in range(self.k):
            c += self(x,i) * self(m-x, (r-i)%self.k)
        self.cache[(m,r)] = c % MOD
        if len(self.cache) % 1000 == 0:
            maxkey = max(self.cache.keys())
            print len(self.cache), maxkey, self.cache[maxkey]
        return self.cache[(m,r)]
        
def isPow10TimesSingleDigit(n):
    while n >= 10:
        if not n%10 == 0:
            return False
        n /= 10
    return True
        
if __name__ == '__main__':
    sc1 = SequenceCounter(1111, 24, [1,11,101,1111])
    print 'Last 9 digits of Seq(1111,24) = {0}'.format(sc1(1111, (-1111)%24))
    sc2 = SequenceCounter(1234567898765, 4321, [1,5,41,205,25343,126715,237631,1039063,1188155,5195315,9742871,48714355,6022282433,30111412165,246913579753,1234567898765])
    print 'Last 9 digits of Seq(1234567898765,4321) = {0}'.format(sc2(1234567898765, (-1234567898765)%4321))   