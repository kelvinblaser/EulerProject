# Euler 51 - Number Changing Primes

import Primes
import itertools as IT

def Has3sameDigits(N):
    # Note, first digit doesn't count
    N /= 10
    digits = {}
    # Count the occurences of each digit
    while N > 0:
        last = N%10
        if not digits.has_key(last):
            digits[last] = 0
        digits[last]+= 1
        N/=10

    # If one is greater than or equal to 3, return true
    for key in digits.keys():
        if digits[key] >= 3:
            return True

    return False

def digitsList(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n /= 10
    return digits

def PossiblePrimesList(N):
    # Get all the candidates for primes changing 3 digits
    ps = Primes.PrimeList(N)
    possList = []
    for p in ps:
        if Has3sameDigits(p):
            possList.append(p)

    return possList

def findSet(N):
    poss = PossiblePrimesList(N)
    possDict = {}
    for prime in poss:
        digits = digitsList(prime)
        comb = IT.combinations(range(1,len(digits)),3)
        while True:
            try:
                mask = comb.next()
            except:
                break
            if (digits[mask[0]]==digits[mask[1]] and
                digits[mask[1]]==digits[mask[2]]):
                otherDigits = []
                for x in range(len(digits)):
                    if not x in mask:
                        otherDigits.append(digits[x])
                key = (tuple(mask),tuple(otherDigits))
                if not possDict.has_key(key):
                    possDict[key] = 0
                possDict[key] += 1
                if possDict[key]==8:
                    print mask
                    print otherDigits

    return possDict,poss


