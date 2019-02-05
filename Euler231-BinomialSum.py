# Euler 231 - Binomial Prime Factorization Sum
import Primes

def Number_Ps_in_N_factorial(N,P):
    p = P
    num = 0
    while P <= N:
        num += int(N/P)
        P *= p
    return num

def Euler231(n,m):
    """ n choose m
    """
    pList = Primes.MakePrimeList(n+1)
    summ = 0
    for p in pList:
        summ += p * (Number_Ps_in_N_factorial(n,p) -
                    Number_Ps_in_N_factorial(m,p) -
                    Number_Ps_in_N_factorial(n-m,p) )
        
    return summ
