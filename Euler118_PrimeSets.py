#-------------------------------------------------------------------------------
# Euler 118 - Pandigital Prime Sets
#             http://projecteuler.net/problem=118
#
# Finds the sets of primes which use each digit 1-9 exactly once.
# Kelvin Blaser     2013-07-20
#-------------------------------------------------------------------------------

import itertools    # For permutations()
import Primes       # For MakePrimeList() and isPrime()

#-------------------------------------------------------------------------------
# Attempt 1 - Make all permutations of 123456789 and insert commas to make sets
#
# Result - Takes way too long.  Must be the 92,897,280 permutations. =)
#-------------------------------------------------------------------------------
def make_num_from_list(digit_list):
    num = 0
    for d in digit_list:
        num *= 10
        num += d
    return num
    
def find_prime_sets(digit_list, current_set, prime_sets, primes):
    '''
    Recursively finds the prime sets.

    digit_list:  The digits to make primes of
    current_set: The set of primes found so far
    prime_sets:  The set of all the pandigital prime_sets found so far
    primes:      A list of primes
    '''
    if len(digit_list) != 9:  # Nine digit lists are composite.  Don't check.
        num = make_num_from_list(digit_list)
        if Primes.isPrime(num):
            current_set.add(num)
            prime_sets.add(frozenset(current_set))

    for ix in range(1,len(digit_list)):
        num = make_num_from_list(digit_list[:ix])
        if Primes.isPrime(num):
            next_set = current_set.copy()
            next_set.add(num)
            find_prime_sets(digit_list[ix:], next_set, prime_sets, primes)
    return

def Euler118_1():
    permutes   = itertools.permutations([1,2,3,4,5,6,7,8,9])
    primes     = Primes.MakePrimeList(10000)
    prime_sets = set()
    
    for digit_list in permutes:
        find_prime_sets(digit_list, set(), prime_sets, primes)
    print 'Number of Pandigital Prime Sets: '+str(len(prime_sets))
    return prime_sets

#-------------------------------------------------------------------------------
# Attempt 2 - Find all primes that don't repeat any digits.  Try to use them to
#             create sets
#-------------------------------------------------------------------------------
def repeats_digits(num):
    digits = []
    while num > 0:
        d = num % 10
        if d in digits:
            return True
        if d == 0:        # Not a repeated digit, but 0's not allowed either.
            return True
        else:
            digits.append(d)
        num /= 10
    return False

def build_sets(ix, digits_used, primes):
    if len(digits_used)==9:
        return 1
    num_sets = 0
    while ix < len(primes) and primes[ix] < 10**(9-len(digits_used)):
        p = primes[ix]
        new_digits = digits_used[:]
        use_p = True
        while p > 0:
            if p % 10 not in new_digits:
                new_digits.append(p%10)
                p /= 10
            else:
                p = 0
                use_p = False
        if use_p:
            num_sets += build_sets(ix+1, new_digits, primes)
        ix += 1
    return num_sets
    
def Euler118_2():
    primes = Primes.MakePrimeList(100000000)
    print 'Primes Calculated'
    primes = [p for p in primes if not repeats_digits(p)]
    print 'Primes with repeated digits eliminated'
    num_sets = build_sets(0,[], primes)
    print 'Number of Pandigital Prime Sets: '+str(num_sets)
    return num_sets
    
