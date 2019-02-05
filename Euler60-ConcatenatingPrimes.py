# Euler 60 Concatinating Primes
# Kelvin Blaser 11-09-2012
"""Concatenating Primes

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
import Primes
import Networks
import NetGraphics
reload(NetGraphics)

def concatenateIntegers(n1,n2,base=10):
    """Concatenates two integers in the base of your choice.
    concatenateIntegers(n1=114, n2=215, base=10)
    returns 114215

    n1 - Integer 1
    n2 - Integer 2
    base - Can concatenate in any integer base.
    """
    numDigits2 = 0
    temp = n2
    while temp > 0:
        temp /= base
        numDigits2 += 1
    n1 *= base**numDigits2
    
    return n1+n2

def listIntersection(list1,list2):
    return filter(list1.__contains__,list2)

def Program(nMax=100, GRAPHICS=False):
    primes = Primes.MakePrimeList(nMax)
    primeGraph = Networks.UndirectedGraph()

    for p in primes:
        primeGraph.AddNode(p)
        for p2 in primeGraph.GetNodes():
            if Primes.isPrime(concatenateIntegers(p,p2),primes):
                if Primes.isPrime(concatenateIntegers(p2,p),primes):
                    primeGraph.AddEdge(p,p2)

    for p1 in primes:
        possibles = primeGraph.GetNeighbors(p1)
        for p2 in possibles:
            possibles2 = listIntersection(possibles,
                                          primeGraph.GetNeighbors(p2))
            for p3 in possibles2:
                possibles3 = listIntersection(possibles2,
                                              primeGraph.GetNeighbors(p3))
                for p4 in possibles3:
                    possibles4 = listIntersection(possibles3,
                                                  primeGraph.GetNeighbors(p4))
                    for p5 in possibles4:
                        print (p1,p2,p3,p4,p5), p1+p2+p3+p4+p5
    
    if GRAPHICS:
        NetGraphics.DisplayCircleGraph(primeGraph)

    return primeGraph
"""
    group = [3, 7, 109, 673]
    for p in primes:
        pFits = True
        for g in group:
            if not g in primeGraph.GetNeighbors(p):
                pFits = False
            else:
                group.append(p)
        if pFits:
            return group
    return False
"""







    
