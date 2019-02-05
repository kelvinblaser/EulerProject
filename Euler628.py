# Euler 628
#
# 8-15-2018
#  I think this patter holds, but I haven't proved it
#  f(n) = n! - 2(n-1)! - (n-2)! + 2*(n-3)! + (n-4)! - 1
#  
#  Nope, I guess not
#
#  New formula
#  f(n) = n! - [1 + sum( [3q+3-n] q!; 0 <= q <= n-2

class Euler628:
    def __init__(self, n):
        self.MOD = 1008691207
        self.n = n
        
    def solve(self):
        if self.n == 4:
            return 24-2*6 - 2 + 2 + 1 - 1
        if self.n == 3:
            return 6 - 2*2 - 1 + 2  - 1
        if self.n < 3:
            return 1
            
        fm = [0]*5
        fm[0] = 1
        for x in range(2, self.n-3):
            if x % 1000000 == 0: print x
            fm[0] *= x
            fm[0] %= self.MOD
        fm[1] = (fm[0] * (self.n-3)) % self.MOD
        fm[2] = (fm[1] * (self.n-2)) % self.MOD
        fm[3] = (fm[2] * (self.n-1)) % self.MOD
        fm[4] = (fm[3] * self.n) % self.MOD
        
        return (fm[4] - 2*fm[3] - fm[2] + 2*fm[1] + fm[0] - 1) % self.MOD
        
def solve(n):
    MOD = 1008691207
    s = 1
    q = 0
    f = 1
    while q <= n-2:
        s += (3*q + 3 - n) * f
        s %= MOD
        q += 1
        f *= q
        f %= MOD
    while q < n:
        q += 1
        f *= q
        f %= MOD
    return (f - s)%MOD
        
if __name__ == '__main__':
    #print '{0}, {1}'.format(1,2)
    #print 'f({0}) = {1}'.format(5, Euler628(5).solve())
    #print 'f({0}) = {1}'.format(10**8, Euler628(10**8).solve())
    print 'f({0}) = {1}'.format(5, solve(5))
    print 'f({0}) = {1}'.format(10**8, solve(10**8))