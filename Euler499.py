###############################################################################
# Euler 499 - St. Petersburg Lottery
# Kelvin Blaser     2015.1.26
#
# Much trial, error and scratch paper went into this.
#
# Rather than calculate the probability pm(s) that the gambler never runs out
# of funds, I will calculate the probability qm(s) = 1-pm(s) that he eventually
# runs out of funds.  The two follow the same recurrence, but the second is
# easier for me to think about.
#
# Suppose the gambler has s funds.  If s < m, the gambler cannot play and
# qm(s) = 1.  With s >= m, he can pley.  After one game, the gambler will have
# s-m+1 funds with probability 1/2, s-m+2 with probability 1/4, s-m+4 with
# probability 1/8, ... s-m+2^k with probability 1/2^(k+1), ....
# Thus the probability of never running out of funds given he has s is the sum
# of the probabilities of never running out of funds given he has s-m+1, s-m+2,
# s-m+4, s-m+8, etc multiplied by the respective probabilities 1/2, 1/4, 1/8,
# 1/16, ... etc.
#
#       qm(s) = sum( 1/2^(k+1) qm(s-m+2^k) ) k = 0,1,2,3,...
#
# This looks like some sort of linear infinite difference equation.  Try to
# solve with the exponential solution common to finite difference equations.
#
#       qm(s) = r^s
#       ==>  r^s = sum( 1/2^(k+1) r^s*r^(2^k-m) )   k = 0,1,2,3,...
#       ==>  r^m = sum( 1/2^(k+1) r^(2^k) )         k = 0,1,2,3,...
#       ==>  r^(m-1) = sum( 1/2^(k+1) r^(2^k-1) )   k = 0,1,2,3,...
#
# Playing around with this function a bit, I see that there are exactly m-1
# roots in the complex unit circle.  I don't know exactly why this is, but it
# is perfect because it gives me m-1 independent solutions which I can use to
# match the m-1 boundary conditions qm(s) = 1 for 1 <= s < m.
#
# The solution is as follows.
#   1. Calculate the m-1 r values using an iterative method.
#   2. Calculate the coefficents of the independent solutions using the m-1
#       initial values.
#   3. Return pm(s) = 1-qm(s) = 1 - sum( coefficient_i * r_i^s )
#
# Iterative Method
#   Let r_n+1 = ( sum( 1/2^(k+1) r_n^(2^k-1) )^1/(m-1).
#   Iterate and use the different branches of the (m-1)th root to get the
#   different roots.
#------------------------------------------------------------------------------
# One thing to note, it does run into roundoff problems.  I had to try a few
# different values in the 7th decimal point at projecteuler.net to get it
# right.
#
# Might have to look into higher precision floats.
###############################################################################
import scipy as sp
import scipy.linalg as la

class StPetersburgLottery(object):
    def __init__(self,m):
        self.m = m
        self.roots = self.calcRoots()
        self.c = self.calcCoeff()

    def __call__(self,n):
        return 1-sum(self.c[i]*pow(self.roots[i],n)
                     for i in range(self.m-1)).real

    def calcRoots(self):
        m = self.m
        kCutoff = 60
        def f(z):
            w = z**(m-1)
            for k in range(kCutoff):
                w -= 0.5**(k+1) * pow(z,2**k-1)
            return w
        def fp(z):
            w = (m-1)*z**(m-2)
            for k in range(1,kCutoff):
                w -= 0.5**(k+1) * (2**k-1) * pow(z,2**k-2)
            return w

        def it(z):
            w = 0
            for k in range(kCutoff):
                w += 0.5**(k+1) * pow(z,2**k-1)
            return w

        rts = [0]*(m-1)

        for n in range(m-1):
            z = 0.7
            zl = 0
            while abs(zl-z) > 1e-15 or abs((zl-z)/(1-z)) > 1e-9:
                zl = z
                z = it(z)**(1./(m-1)) * sp.exp(1j*2*sp.pi*n/(m-1))
            rts[n] = z
        
        return rts

    def calcCoeff(self):
        m,r = self.m, self.roots
        M = sp.zeros((m-1,m-1),dtype=complex)
        for i in range(m-1):
            for j in range(m-1):
                M[i,j] = r[j]**(i+1)
        b = sp.ones((m-1))
        return la.solve(M,b)

if __name__ == '__main__':
    p2 = StPetersburgLottery(2)
    p6 = StPetersburgLottery(6)
    p15 = StPetersburgLottery(15)

    print 'p2(2) =', p2(2)
    print 'p2(5) =', p2(5)
    print 'p6(10000) =', p6(10000)
    print 'p15(10^9) =', p15(10**9)


    

    
    
