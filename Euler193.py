#------------------------------------------------------------------------------
# Euler 193 - Squarefree Numbers
#             http://projecteuler.net/problem=193
#
# Kelvin Blaser     2013-07-20
#------------------------------------------------------------------------------

import Primes           # For MakePrimeList()
import scipy as sp
import itertools        # For combinations()

#------------------------------------------------------------------------------
# Attempt 1 - Count the squareful numbers less than N and subtract them from N
# Result - Slow and some error somewhere for 2**20 and 2**50.  Took about 10
#          minutes for 2**50, and the result was not correct.  Not sure why.
#          I have verified it works correctly for all N up to 10000.
#------------------------------------------------------------------------------
def ix_combo(last, primes, root):
    n = len(last)
    ix_max = len(primes)
    i = 0
    while i < n and last[n-i-1] == ix_max - i - 1:
        i += 1
    if i == n:
        return False
    last[n-i-1] += 1
    for j in range(n-i, n):
        last[j] = last[j-1]+1
    while sp.product([primes[x] for x in last]) > root:
        i += 1
        if i == n:
            return False
        last[n-i-1] += 1
        for j in range(n-1, n):
            last[j] = last[j-1]+1
    return True

def Euler193(N):
    '''
    Calculates the number of squarefree numbers less than N
    '''
    root = round(sp.sqrt(N))
    primes = Primes.MakePrimeList(root)
    num = 0
    
    n = 1
    min_prod = 2
    #---------------------------------------#
    # Loop over the number of primes to use #
    # in the inclusion-exclusion principle. #
    #---------------------------------------#
    while min_prod <= root:
        #-----------------------------------------#
        # Iterate over all the combinations of n  #
        # primes, adding or subtracting according #
        # to the inclusion-exclusion principle.   #
        #-----------------------------------------#
        ix_list = range(n)
        done = False
        while not done:
            # Calculate the number of square including numbers
            p = sp.product([primes[ix]*primes[ix] for ix in ix_list])
            #print [primes[i] for i in ix_list]
            if n % 2 == 0:
                num -= (N-1) / p
                #print '-'+str(N / p)
            else:
                num += (N-1) / p
                #print '+'+str(N/p)
            done = not ix_combo(ix_list, primes, root)
            
        n += 1
        min_prod = sp.product(primes[:n])
        
    num = N - num - 1
    #print 'Number of squarefree numbers below '+str(N)+': '+str(num)
    return num

def Euler193_slow(N):
    primes = Primes.MakePrimeList(round(sp.sqrt(N)))
    x = range(N)
    for p in primes:
        x = [i for i in x if i%(p**2) != 0]
    return len(x)

#------------------------------------------------------------------------------
# Attempt 2 - Use equation 5 on SquareFree entry at Wolfram mathworld
#             http://mathworld.wolfram.com/Squarefree.html
#             I need to be able to calculate the mobius function for all values
#             up to sqrt(N-1)
# Result - Almost worked.  There's an off by 1 error somewhere.
#------------------------------------------------------------------------------
def calc_mobius(n):
    primes = Primes.MakePrimeList(n)
    mu = [1]*(n+1)
    mu[0] = 0
    mu[1] = 1
    for p in primes:
        mu[p] = -1
        i = 2
        while p * i <= n:
            mu[p*i] *= -1
            i += 1
        i = 1
        while p*p*i <= n:
            mu[p*p*i] = 0
            i += 1
    return mu

def Euler193_2(N):
    mu = calc_mobius(int(sp.sqrt(N-1)))
    Q = 0
    for d in range(1,int(sp.sqrt(N-1))):
        Q += mu[d] * int((N-1)/(d*d))
    print 'Number of squarefree integers below '+str(N)+': '+str(Q)
    return Q
