################################################################################
# Euler 516 - 5-Smooth Totients
# Kelvin Blaser      2015.05.18
#
################################################################################
from Primes import Miller_Rabin, combProdLessThan

def base_hamming_nums(b,N):
    ''' Generates all numbers less than or equal to N of the form b * h
    where h is a Hamming number.'''
    x = b
    while x <= N:
        y = x
        while y <= N:
            z = y
            while z <= N:
                yield z
                z *= 2
            y *= 3
        x *= 5
    return

def prod(itt):
    x = 1
    for y in itt:
        x *= y
    return x

def Euler516(N):
    bhn = [x for x in base_hamming_nums(1,N)]
    ret = sum(bhn)
    #ret_vec = []
    #ret_vec.extend(bhn)
    hamming_primes = [x+1 for x in bhn if Miller_Rabin(x+1) and x > 5]
    hamming_primes.sort()

    for r in range(1,len(hamming_primes)):
        for c in combProdLessThan(hamming_primes,r,N):
            #print c
            #ret_vec.extend([x for x in base_hamming_nums(prod(c),N)])
            ret += sum([x for x in base_hamming_nums(prod(c),N)])
    return ret#, ret_vec
        
