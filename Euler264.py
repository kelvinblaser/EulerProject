# Euler 264
# Kelvin Blaser     2019-02-26

from __future__ import division, print_function
from collections import defaultdict

def sumSquares(N):
    ssqrs = defaultdict(list)
    r = int(N**0.5)+1
    for x in range(r+1):
        for y in range(x+1):
            n = x*x + y*y
            if n % 5 != 0: continue
            if n > N: break
            ssqrs[n].append((x,y))
    return ssqrs
