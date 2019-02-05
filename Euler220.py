###############################################################################
# Euler 220 - Heighway Dragon
# Kelvin Blaser     2014.12.31      Happy New Years!  Welcome 2015
#
# One can show that p_2^n = (I-R)p_2^(n-1) where R = [[0,-1],[1,0]].
# Likewise, one can show that for 2^n-1 < m < 2^n, p_m = p_2^n - Rp_(2^n-m).
# This forms the basis for calculating the postion of the mth step in the
# Heighway Dragon.
###############################################################################
import pylab as pl

class HeighwayDragon(object):
    # Cache the points for plotting.
    cache = {}

    def __call__(self, n):
        return self.pm(n)

    def pm(self, m):
        try:
            return self.cache[m]
        except KeyError:
            pass
        if m == 1:
            return (0,1)
        if m == 0:
            return (0,0)
        # Find n such that 2^(n-1) < m <= 2^n
        x = m
        n = 0
        while x > 0:
            x /= 2
            n += 1
        # If m is a power of 2
        if m == 2**(n-1):
            return self.p2n(n-1)
        x2n, y2n  = self.p2n(n)
        x2nm,y2nm = self.pm(2**n-m)
        x,   y    = x2n - y2nm, y2n + x2nm
        self.cache[m] = (x,y)
        return (x,y)

    def p2n(self, n):
        try:
            return self.cache[2**n]
        except KeyError:
            pass
        if n == 0:
            return (0,1)
        x2n1,y2n1 = self.p2n(n-1)
        x,y = x2n1+y2n1, y2n1-x2n1
        self.cache[2**n] = (x,y)
        return (x,y)

    def plotHD(self,n, color='r'):
        ''' Plots Heighway Dragon of order n. '''
        x = [self(i)[0] for i in range(2**n+1)]
        y = [self(i)[1] for i in range(2**n+1)]
        pl.plot(x,y, color)

if __name__ == '__main__':
    hd = HeighwayDragon()
    #for n in range(20):
    #    print '%d:'%(n,), hd(n)
    print hd(500)
    c = ['r','k','g','b']
    for x in range(18,0,-1):
        hd.plotHD(x,c[x%4])
    print hd(10**12)
    pl.axis('equal')
    pl.show()
