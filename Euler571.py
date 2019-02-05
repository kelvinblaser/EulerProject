#----------------------------------------------------------------------------
# Euler 571
#
# Create 12-pandigital numbers in order
# Test if they are pandigital in 2-11
# Find the first ten such
#----------------------------------------------------------------------------
from itertools import permutations

def isPandigital(n, b):
    digitFound = [False]*b
    while n > 0:
        digitFound[n%b] = True
        n //= b
    return all(digitFound)
    
def pandigitalGen(b):
    digits = [1,0] + list(range(2,b))
    n = 0
    for perm in permutations(digits, b):
        if perm[0] == 0:
            continue
        x = 0
        for d in perm:
            x *= b
            x += d
        yield x
        if n %100000 == 0:
            print n
        n += 1
    
    
if __name__ == '__main__':
    #print isPandigital(4,2)
    #print isPandigital(1234567890, 10)
    #print isPandigital(1093265784, 7)
    #print isPandigital(123456789, 10)
    
    #n = 0
    #for perm in pandigital12():
    #    print perm, n
    #    n += 1
    #    if n == 10:
    #        break
    
    superPandigitalsFound = 0
    spSum = 0
    for x in pandigitalGen(12):
        s = [isPandigital(x,b) for b in range(2,12)]
        if all(s):
            spSum += x
            superPandigitalsFound += 1
            print superPandigitalsFound, x, spSum 
        if superPandigitalsFound == 10:
            break
    print spSum