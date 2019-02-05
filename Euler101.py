# Euler 101
# Kelvin Blaser  2013-03-20

import fractions
import scipy as sp
import numpy.polynomial
import scipy.linalg as la

class RationalPoly:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        for i in range(len(coeffs)):
            self.coeffs[i] = fractions.Fraction(coeffs[i])
        self.d = len(coeffs)-1

    def __call__(self, n):
        ans = self.coeffs[-1]
        for x in range(self.d):
            ans *= n
            ans += self.coeffs[self.d-x-1]
        return ans

def generatingPoly(n):
    coeffs = [1,-1,1,-1,1,-1,1,-1,1,-1,1]
    u = numpy.polynomial.polynomial.Polynomial(coeffs)
    x = sp.array(range(1,n+1), dtype=int)
    y = u(x)
    return x,y

def make_op(k, x, y):
    b = sp.array(y[:k])
    A = sp.array([sp.ones(k)])
    xx = sp.array([x[:k]])
    xx = xx.transpose()
    A = A.transpose()
    for i in range(1,k):
        A = sp.concatenate((A, xx**i),1)
    c = la.solve(A,b)
    return numpy.polynomial.polynomial.Polynomial(c)

u = RationalPoly([1,-1,1,-1,1,-1,1,-1,1,-1,1])
print u(1), u(2), u(3)
x,y = generatingPoly(13)
c = make_op(10,x,y)
print c(x)
print y

