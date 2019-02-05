# Project Euler 268 - Counting numbers with at least 4 distinct factors less
#                     than 100
# Kelvin Blaser     2014.10.15
import Primes
#from scipy import prod
from scipy.misc import comb
from itertools import combinations

def f(lis, m, N):
    if m == 0:
        return N
    if m > len(lis):
        return 0
    if prod(lis[:m]) > N:
        return 0

    new_lis = lis[1:]
    p = lis[0]
    return f(new_lis, m, N) + f(new_lis, m-1, N//p)

def prod(lis):
    x = 1
    for j in lis:
        x *= j
    return x

def Euler268(N,M=100):
    primes = Primes.MakePrimeList(M)
    #return f(primes, 4, N)
    added = [0]*(len(primes)+1)
    ans = 0
    for r in range(4,len(primes)+1):
        print N,r,ans
        if prod(primes[:r]) > N:
            break
        multiplier = 1 - added[r]  
        # Update how many times we have added numbers divisible by
        # exactly x primes in the list.
        for x in range(r,len(primes)+1):
            added[x] += multiplier * comb(x,r,True)
        # Actually add them
        ans += multiplier*sum(N//prod(c) for c in combinations(primes,r))
    return ans

if __name__ == '__main__':
    print Euler268(1000)
    print Euler268(10**16)
