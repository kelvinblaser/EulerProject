################################################################################
# Euler 520 - Simbers
# Kelvin Blaser      2015.06.18
#
# Consider q(n,e,o,oz,lz) which gives the number of length-n strings in which
# e symbols appear an even number of times, o symbols appear an odd number of
# times, oz symbols appear an odd number or zero times, and lz numbers can
# appear as leading zeros which do not count.  (lz can only be zero or one,
# depending on if there is a non-zero symbol to the left)
#
# By choosing the leftmost symbol (digit) we get the following recurstion:
#      q(n,e,o,oz,lz) = e * q(n-1,e-1+lz,o+1,oz,0) +
#                       o * q(n-1,e+1+lz,o-1,oz,0) +
#                       oz * q(n-1,e+1+lz,0,oz-1,0) +
#                       lz * q(n-1,e,o,oz,lz)
#
# Clearly Q(n) = q(n,4,0,5,1).  I will create a matrix which advances q(n) to
# q(n+1) where q is a vector whose indices correspond to all possible
# (e,o,oz,lz).  I can then comput Q(n) for large n quickly by fast matrix
# exponentiation.
################################################################################
import numpy as np
from Euler import matModExp
MOD = 1000000123

class SimberCounter:
    def __init__(self):
        self.createIndexMap()
        self.createMatrix()
        self.createQ0()

    def createIndexMap(self):
        self.indices = []
        for e in range(11):
            for o in range(11-e):
                self.indices.append((e,o,10-e-o))
        self.ixMap = {}
        for ix, x in enumerate(self.indices):
            self.ixMap[x] = ix

    def createMatrix(self):
        # There is only one possible set of e,o,oz when lz = 1, so leave that
        # for the end.  Start with lz = 0
        m = len(self.indices) + 1
        self.A = np.zeros((m,m), dtype=np.uint64)
        for e,o,oz in self.indices:
            if e > 0:
                self.A[self.ixMap[(e,o,oz)],self.ixMap[(e-1,o+1,oz)]] = e
            if o > 0:
                self.A[self.ixMap[(e,o,oz)],self.ixMap[(e+1,o-1,oz)]] = o
            if oz > 0:
                self.A[self.ixMap[(e,o,oz)],self.ixMap[(e+1,o,oz-1)]] = oz

        # Deal with the leading zero case. lz=1  ==>  (e,o,oz) = (4,0,5)
        self.A[m-1,self.ixMap[(4,1,5)]] = 4
        self.A[m-1,self.ixMap[(6,0,4)]] = 5
        self.A[m-1,m-1] = 1

    def createQ0(self):
        m = len(self.indices) + 1
        self.q0 = np.zeros((m,), dtype=np.uint64)
        for e,o,oz in self.indices:
            if o == 0:
                self.q0[self.ixMap[(e,o,oz)]] = oz
            if o == 1:
                self.q0[self.ixMap[(e,o,oz)]] = o
#        self.q0[self.ixMap[(10,0,0)]] = 1
        self.q0[m-1] = 5  # Is this right?  Test to make sure.

    def __call__(self, n, m=MOD):
        A = matModExp(self.A,n-1,m)
        q = A.dot(self.q0) % m
        return q[-1]

if __name__ == '__main__':
    Q = SimberCounter()
    print 'Q(7)   = %d'%(Q(7),)
    print 'Q(100) = %d'%(Q(100),)
    s = 0
    for u in range(1,40):
        ds = Q(2**u)
        print u,ds
        s += ds
        s %= MOD
    print 'Euler520 = %d'%(s,)
        
        






        
