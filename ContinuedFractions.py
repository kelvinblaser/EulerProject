"""Continued Fraction
Functions useful for working with continued fractions
"""
import scipy as sp
from fractions import Fraction

def sqrtContFrac(n):
    """ Computes the continued fraction of the sqrt of n
    For non-square n, returns in the form [a0,a1,a2,(a3,a4,a5)] where the
    tuple (a3, a4, a5) is the repeated part.

    No good for square n.  So don't use it. - Kelvin =)
    """
    rootn = sp.sqrt(n)
    a = []
    a.append(int(sp.floor(rootn)))
    bLast = Fraction(0)
    cLast = Fraction(1)

    abcList = []
    while not (a[-1], bLast, cLast) in abcList:
        abcList.append((a[-1], bLast, cLast))
        bNext = cLast * a[-1] - bLast
        cNext = (n - bNext**2)/cLast
        aNext = int(sp.floor((rootn + bNext)/cNext))
        a.append(aNext)
        bLast = bNext
        cLast = cNext

    repeatIndex = abcList.index((a[-1],bLast,cLast))
    a.pop()
    contFraction = a[:repeatIndex]
    repeat = tuple(a[repeatIndex:])
    contFraction.append(repeat)

    return contFraction
    
def calculateConvergent(contFraction):
    """Given a list of numbers continued fraction coefficients, returns the
    convergent as a fraction
    """
    pass
