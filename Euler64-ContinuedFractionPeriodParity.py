"""Euler 64 Continued Fraction Period Parity
Finds the parity of the period of the continued fractions of sqrt(n)

Kelvin Blaser       11-14-2012

"""

import scipy
from fractions import Fraction

def ContFracParity(n):
    """Finds the parity of the period of the continued fraction of
    sqrt(n).  Do not send square numbers.  They result in divide by zero
    and I don't want to check for it
    """
    rootn = scipy.sqrt(n)
    aLast = int(scipy.floor(rootn))
    bLast = Fraction(0)
    cLast = Fraction(1)

    abcList = []
    while not (aLast, bLast, cLast) in abcList:
        abcList.append((aLast, bLast, cLast))
        bNext = cLast * aLast - bLast
        cNext = (n - bNext**2)/cLast
        aNext = int(scipy.floor((rootn + bNext)/cNext))
        aLast = aNext
        bLast = bNext
        cLast = cNext

    repeatIndex = abcList.index((aLast, bLast, cLast))
    periodLength = len(abcList)-repeatIndex
    return periodLength % 2
                    
def Euler64(n):
    """ Returns the number of continued fractions of sqrt(m) for m less than
    or equal to n whose period is odd
    """
    nums = range(n+1)
    squareMax = int(scipy.floor(scipy.sqrt(n)))
    squares = range(squareMax+1)
    
    for x in squares:
        nums.remove(x**2)
    count = 0
    for m in nums:
        if m%1000 == 0:
            print m
        count += ContFracParity(m)

    return count
