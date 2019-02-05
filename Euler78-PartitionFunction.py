# Euler 78 - Partition Function mod n
# Kelvin Blaser 11-17-21
import scipy as sp

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, arg, modder=None):
        if arg not in self.cache:
            self.cache[arg] = self.func(arg, modder)
        return self.cache[arg]

def Euler78(modder):
    n = 0
    while partitionMod(n, modder):
        n+=1
    return n

@Memoize
def partitionMod(n, modder):
    """ Calculates the partition function of n modulo modder
    """
    if n < 0:
        return 0
    if n==0:
        return 1
    if n==1:
        return 1

    p = 0
    kMax = int(sp.floor((1+sp.sqrt(1+24*n))/2))
    for k in range(1,kMax+1):
        first = n - ((3*k-1)*k)/2
        second = n - ((3*k+1)*k)/2
        sign = 2*(k%2) - 1
        p += sign * (partitionMod(first, modder) +
                     partitionMod(second, modder))
        p = p % modder
    return p
    


