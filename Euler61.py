# Euler Project 61 - Triangle, Square , Pentagonal etc. numbers
import scipy

def triangleNum(n):
    """
    Calculates the nth Triangle number
    """
    return n*(n+1)/2

def squareNum(n):
    """
    Calculates the nth square number
    """
    return n*n

def pentagonalNum(n):
    """
    Calculate the nth pentagonalNumber
    """
    return n * (3*n-1)/2

def hexagonalNum(n):
    """
    Calculates the nth hexagonal number.
    """
    return n * (2*n-1)

def heptagonalNum(n):
    """
    Calculates teh nth heptagonal number.
    """
    return n*(5*n-3)/2

def octagonalNum(n):
    """
    Calculate the nth octagonal number.
    """
    return n * (3*n-2)

def createPolyDict(triangleNums,
                   squareNums,
                   pentagonalNums,
                   hexagonalNums,
                   heptagonalNums,
                   octagonalNums):
    """
    Creates a dictionary with keys being tuples (x, yy) where x signifies
    the type of polygonal number and yy is the first two digits of the number.
    The values at key (x, yy) are lists with the last two digits of the
    polygonal numbers of type x with first two digits yy.
    """
    poly = {}
    superList = [triangleNums, squareNums, pentagonalNums,
                 hexagonalNums, heptagonalNums, octagonalNums]

    for x in range(6):
        for num in superList[x]:
            if 1000 <= num < 10000:
                key = (x, int(num/100))
                if not poly.has_key(key):
                    poly[key] = []
                poly[key].append( int(num % 100))

    return poly

def search(notSearched, polydict, keyNum, firstKey):
    # If searched to the end, return something if completed sequence
    # return empty list if not completed sequence
    if not notSearched:
        if keyNum == firstKey:
            return [keyNum]
        else:
            return []

    # Since the types can be in any order, have to search each type separately
    for x in notSearched:
        newNotSearched = notSearched[:]
        newNotSearched.remove(x)
        key = (x,keyNum)
        if polydict.has_key(key):
            for newKeyNum in polydict[key]:
                answer = search(newNotSearched, polydict, newKeyNum, firstKey)
                if answer:
                    answer[-1] += 100*keyNum
                    answer[-1] = (x, answer[-1])
                    answer.append(keyNum)
                    return answer[:]

    # No solution
    return []

def main61():
    # Calculate all the polygonal numbers below 10000
    n = scipy.array(range(142))
    triangleNums    = triangleNum(n)
    squareNums      = squareNum(n)
    pentagonalNums  = pentagonalNum(n)
    hexagonalNums   = hexagonalNum(n)
    heptagonalNums  = heptagonalNum(n)
    octagonalNums   = octagonalNum(n)

    # Create a dictionary with all the polygonal numbers
    polynums = createPolyDict(triangleNums,
                              squareNums,
                              pentagonalNums,
                              hexagonalNums,
                              heptagonalNums,
                              octagonalNums)

    # Search for sequence
    notSearched = range(5)
    for firstKey in range(10,100):
        key = (5, firstKey)
        if polynums.has_key(key):
            for keyNum in polynums[key]:
                sequence = search(notSearched, polynums, keyNum, firstKey)
                if sequence:
                    # Process for printing and returning
                    sequence[-1] += 100 * firstKey
                    sequence[-1] = (5, sequence[-1])
                    summ = 0
                    for pair in sequence:
                        summ += pair[1]
                    return [sequence, summ]

    # Not found
    return 0

    
    
