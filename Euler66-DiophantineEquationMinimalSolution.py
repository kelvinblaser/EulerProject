"""Euler 66 - Diophantine Equation
Kelvin Blaser 11-16-2012
"""
import scipy as sp
from ContinuedFractions import sqrtContFrac
from fractions import Fraction

def getNthCoefficient(contFrac,n):
    length = len(contFrac) - 1
    if n < length:
        return contFrac[n]
    repeatPart = contFrac[-1]
    lenRep = len(repeatPart)
    return repeatPart[(n-length)%lenRep]

def getMinSol(contFrac,d):
    n = 0
    foundSol = False
    xLast = 0
    xNow = 1
    yLast = 1
    yNow = 0
    while not foundSol:
        b = getNthCoefficient(contFrac,n)
        x = b*xNow + xLast
        y = b*yNow + yLast
        if x*x == (1 + d*y*y):
            foundSol = True
        xLast = xNow
        xNow = x
        yLast = yNow
        yNow = y
        n += 1
    return (xNow,d) 

def Euler66(n):
    D = range(n+1)
    D.remove(0)
    D.remove(1)
    squares = range(int(sp.sqrt(n))+1)
    for n,s in enumerate(squares):
        squares[n] = s*s
    for d in D:
        if d in squares:
            D.remove(d)

    minSol = []
    for d in D:
        contFrac = sqrtContFrac(d)
        minS = getMinSol(contFrac, d)
        minSol.append(minS)

    minSol.sort(key=lambda pair: pair[0])
    return minSol[-1]
