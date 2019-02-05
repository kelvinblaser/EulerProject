# Euler 432 Big Totient
# Kelvin Blaser   6-21-2013

import Primes

def sum_range(lower, upper):
    return (upper*(upper+1) - lower*(lower-1))/2

def weird_sum_tot(m, ix, primes, level=1):
    #print 'm = '+str(m)+', pr = '+str(primes[ix])+', Level: '+str(level)
    ans = sum_range(primes[ix], m)
    jx = ix
    second_sum_flag = False

    #print 'Hi', ans
    while primes[jx] <= m:
        if m / primes[jx] < primes[jx+1]:
            upper = m / primes[jx]
            if not second_sum_flag:
                #print ans, primes[jx]
                second_sum_flag = True
        else:
            upper = primes[jx+1]-1
            ans -= weird_sum_tot(m/primes[jx], jx+1, primes, level+1)
        ans -= sum_range(1,upper)
        jx += 1
    #print ans
    return ans

def get_pq_ix(m, primes):
    ix_l = 0
    ix_u = len(primes)-1
    root = m**(1./2)
    if int(round(root))**2 == m:  # In case m is square, but numerical errors 
        root = int(round(root))   # make root not an integer.
    while ix_u - ix_l > 1:
        ix_test = (ix_u + ix_l) / 2
        if primes[ix_test] > root:
            ix_u = ix_test
        if primes[ix_test] < root:
            ix_l = ix_test
        if primes[ix_test] == root:
            ix_l = ix_test
            ix_u = ix_l + 1
    if m / primes[ix_l] < primes[ix_u]:
        return ix_l
    return ix_u

def get_lx(m,k,primes):
    ix_l = 0
    ix_u = len(primes)-1
    piv = float(m)/k
    if int(piv)*k == m:
        piv = int(piv)
    if int(piv+1)*k == m:
        piv = int(piv+1)
    while ix_u - ix_l > 1:
        ix_test = (ix_u + ix_l) / 2
        if primes[ix_test] > piv:
            ix_u = ix_test
        if primes[ix_test] < piv:
            ix_l = ix_test
        if primes[ix_test] == piv:
            ix_l = ix_test
            ix_u = ix_l + 1
    while primes[ix_l] > (m / primes[ix_l])*float(primes[ix_l])/ k:
        ix_l -= 1
        print 'Whoa!'
    return ix_l
    

def func(m, ix, primes, prime_pi):
    '''
    Requires primes to be calculated upto a bit further than sqrt(m).
    '''
    ans = sum_range(primes[ix],m)
    q = get_pq_ix(m, primes)      # primes[q] is the first prime for which
                                  # m / primes[q] < primes[q+1]
 #   print ans
    #print 'Hi', ans, primes[q]
    if ix < q:
        for k in range(1,primes[q]):
            ans -= k*( q+1 )
            if primes[ix-1] >= k:
                ans += k * ix
            else:
                ans += k * prime_pi(k, primes)
        for jx in range(ix,q):
            ans -= func(m/primes[jx], jx+1, primes, prime_pi)
    if m / primes[ix] >= primes[ix+1]:
        ans += sum_range(1,primes[ix]-1)
    #print ans
    for k in range(1, min(m / primes[q], m / primes[ix])+1):
        #lx = get_lx(m, k, primes)
        #ans -= k*( prime_pi(primes[lx], primes) -
        #           prime_pi(max(primes[q], primes[ix]), primes) + 1 )
        ans -= k*( prime_pi(m/k, primes) -
                   prime_pi(max(primes[q], primes[ix]), primes) + 1 )
    #print ans
#        print ans
    # Voodoo fix
    #if Primes.isPrime(m, primes):
    #    ans -= 1
    #    print 'Hi'
    return ans

def old_432(m):
    primes = Primes.MakePrimeList(int(m*2))
    ans = sum_range(1,18)
    ans += weird_sum_tot(m,7, primes)
    ans *= 510510
    for ix in range(7):
        ans *= (primes[ix] - 1)
        ans /= primes[ix]

    return ans

def new_432(m):
    #primes = Primes.MakePrimeList(int(1.2*m**(1./2))+100)
    primes = Primes.MakePrimeList(int(1.2*m**(1./2))+120)
    prime_pi = Primes.Prime_Pi()
    ans = sum_range(1,18) + func(m, 7, primes, prime_pi)
    ans *= 510510
    for ix in range(7):
        ans *= (primes[ix] - 1)
        ans /= primes[ix]
    return ans

                
