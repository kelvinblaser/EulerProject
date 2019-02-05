#! /usr/bin/python

import numpy as np
from math import log, ceil, factorial

def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)

def p(i,j,memo={}):
    if j > 99:
        return 1.0
    if i == 100:
        return 0.0

    if (i,j) in memo:
        return memo[(i,j)]

    n = int(ceil(log(100-j,2)))+1
    memo[(i,j)] = max([(p(i,j+2**(T-1),memo) + p(i+1,j+2**(T-1),memo) + (2**T-1)*p(i+1,j,memo)) / (2**T+1) for T in range(1,n+1)])

    return memo[(i,j)]

if __name__ == '__main__':
    memo = {}
    print 0.5 * (p(1,0, memo) + p(0,0, memo))
