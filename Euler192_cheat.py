from math import sqrt
import fractions
from fractions import Fraction

def is_square (n):
	m = int_sqrt (n)
	return m * m == n

def int_sqrt (n):
    return int (sqrt (n + 0.5))

def inverse (x):
    a = x [0] * x [3]
    b =-x [1] * x [3]
    d = x [0] ** 2 - x [1] ** 2 * x [2]
    d1 = fractions.gcd (a, fractions.gcd (b, d))
    return (a / d1, b / d1, x [2], d / d1)

def integer (x):
    if x [0] == 0 and x [3] == 1:
        n = x [1] ** 2 * x [2]
        m = int_sqrt (n)
        if n >= m * m:
            while True:
                m += 1
                if n <m * m:
                    return m - 1
        else:
            while True:
                m -= 1
                if n> m * m:
                    return m + 1
    else:
        if x [1]> 0:
            return (x [0] + integer ((0, x [1], x [2], 1))) / x [3]
        else:
            return (x [0] - integer ((0,-x [1], x [2], 1)) - 1) / x [3]

def sub (x, n):
    return (x [0] - n * x [3], x [1], x [2], x [3])
def approx_sqrt (n):
    p = [int_sqrt (n)]
    a = [1, p [0]]
    b = [0, 1]
    r = (-p [0], 1, n, 1) # sqrt (n) - m
    k = 2
    while b [-1] <= N:
        c = inverse (r)
        m = integer (c)
        p.append (m)
        r = sub (c, m)
        a.append (a [k-1] * p [k-1] + a [k-2])
        b.append (b [k-1] * p [k-1] + b [k-2])
        k += 1
   
    while b [k-1]> N:
        p [k-2] -= 1
        if p [k-2] == 0:
            return (a [k-2], b [k-2])
        a [k-1] = a [k-2] * p [k-2] + a [k-3]
        b [k-1] = b [k-2] * p [k-2] + b [k-3]
   
    if b [k-1]> N:
        return (a [k-2], b [k-2])
   
    f1 = Fraction (a [k-2], b [k-2])
    f2 = Fraction (a [k-1], b [k-1])
    mean = (f1 + f2) / 2
    if mean * mean <n:
        f = max (f1, f2)
    else:
        f = min (f1, f2)
    return (f.numerator, f.denominator)
N = 10**12
M = 10
s = 0
for n in range (2, M + 1):
    if is_square (n):
        continue
    t = approx_sqrt (n)
    p,q = t
    print 'sqrt(%d) => %d / %d  \t\t %f => %f' % (n,p,q, sqrt(n), float(p)/q)
    s += t [1]
print s