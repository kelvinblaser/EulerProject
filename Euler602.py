# Euler 602

class HeadCounts:
    def __init__(self, n):
        self.MOD = 10**9 + 7
        self.n = n
        self.binom = [1]*(n+2)
        for k in range(1,n+2):
            self.binom[k] = self.binom[k-1] * (k-n-2)
            self.binom[k] *= pow(k, self.MOD-2, self.MOD)
            self.binom[k] %= self.MOD
        
    def coeff(self, k):
        c = 0
        for x in range(k+1):
            c += pow(x, self.n, self.MOD) * self.binom[k-x]
        c %= self.MOD
        return c
        
if __name__ == '__main__':
    hc3 = HeadCounts(3)
    print 'c(3,1) = {0}'.format(hc3.coeff(1))
    print 'c(3,2) = {0}'.format(hc3.coeff(2))
    print 'c(3,3) = {0}'.format(hc3.coeff(3))
    hc100 = HeadCounts(100)
    print 'c(100,40) = {0}'.format(hc100.coeff(40))
    n = 10**7
    k = 4 * 10**6
    hcn = HeadCounts(n)
    print 'c({0},{1}) = {2}'.format(n, k, hcn.coeff(k))