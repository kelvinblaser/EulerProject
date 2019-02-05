# Euler 226 - A Scoop Of Blancmange
# http://projecteuler.net/problem=226
#
# Kelvin Blaser 2014.02.25

from math import sqrt, asin, pi

def nearest_int(x):
    ''' Distance to nearest integer'''
    y = x - int(x)
    if y > 0.5:
        return 1-y
    else:
        return y

def blanc(x):
    ''' Blancmange function of x '''
    return sum(nearest_int(2**n * x) / 2**n for n in range(40))
    
def blancInt(x, count=0):
    ''' Integral or Blancmange function from 0 to x 
    Don't use abs(x) > max_recursion_depth 
    '''
    if x >= 1.0:
        return 0.5 + blancInt(x-1,count)
    if x > 0.5:
        return 0.5 - blancInt(1-x, count)
    if x >= 0:
        if count == 40:
            return 0.0
        return x*x / 2.0 + blancInt(2*x, count+1) / 4.0
    return -blancInt(-x, count)

# Find intersection between circle and Blancmange curve.
tol = 1e-14
xu = 0.25    # Upper bound
xl = 0.0     # Lower bound
while xu - xl > tol:
    xm = (xu + xl)/2.0
    yc = 0.5 - sqrt(1.0/16.0 - (xm - 0.25)**2)
    yb = blanc(xm)
    if yb > yc:
        xu = xm
    else:
        xl = xm
x0 = (xu + xl) / 2.0

# Now insert into analytical results
print x0
area = 0.25 - blancInt(x0)
a1 = 0.25 - x0 / 2.0 - 1.0 / 32.0 * (pi / 2 - asin(4*x0-1) - (4*x0-1)*sqrt(8*x0*(1-2*x0)))
area -= a1
print area