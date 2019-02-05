# Euler 87 - Prime Power Partition

import Primes
import scipy

def Euler87(n):
    ps = Primes.MakePrimeList(int(scipy.sqrt(n))*2)
    nF = 0
    nums = []
    count = 0
    while ps[nF]**4 <= n:
        nC = 0
        while ps[nF]**4 + ps[nC]**3 <= n:
            nS = 0
            while ps[nF]**4 + ps[nC]**3 + ps[nS]**2 <= n:
                a = ps[nF]**4 + ps[nC]**3 + ps[nS]**2
                count += 1
                nums.append(a)
                nS += 1
            nC += 1
        nF += 1

    nums.sort()
    for x in range(1,len(nums)):
        if nums[x]==nums[x-1]:
            count -= 1
        
    return count


