# Euler 84 - Monopoly Markov Process

import scipy
from scipy.linalg import eig, solve
from numpy.linalg import matrix_power

JAIL = 10
GO = 0

def createFairDice(n):
    diceProbabilities = [min(x,2*n-x) for x in range(1,2*n)]
    return scipy.array(diceProbabilities, float)/n**2
    
def buildRawMonopoly(diceProbabilities=None):
    M = scipy.zeros((40,40))
    if diceProbabilities == None:
        diceProbabilities = scipy.array([1.0,2.0,3.0,4.0,3.0,2.0,1.0])/16.0
    for x in range(40):
        for n,p in enumerate(diceProbabilities):
            M[(x+n+2)%40,x] += p
    return M

def accountForCommunity(M):
    """
    # Landing on community chest gives a  1/16 chance of going to JAIL and
    # 1/16 chance of going to GO
    """
    # Locations of community chest spots
    community = [2, 17, 33]
    cardProb = 1.0/16.0
    
    # Every spot that leads to community chest has 1/8 chance of not staying
    for c in community:
        for x in range(40):
            probToAdd = cardProb * M[c,x]
            M[JAIL,x] += probToAdd  # 1 card go to JAIL
            M[GO,x] += probToAdd    # 1 card go to GO
    for c in community:
        for x in range(40):
            M[c,x] *= 7.0/8.0
    

def accountForChance(M):
    """
    Landing on Chance gives a 1/16 chance of moving to various locations
    on the board
    """
    # Locations of Chance spots
    chance = [7, 22, 36]
    nextRR = [15, 25, 5]
    nextUtility = [12, 28, 12]
    cardProb = 1.0/16.0

    for n,c in enumerate(chance):
        for x in range(40):
            probToAdd = cardProb * M[c,x]
            # 1 card to GO, JAIL, C1, E3, H2, R1
            M[GO,x] += probToAdd
            M[JAIL,x] += probToAdd
            M[11,x] += probToAdd
            M[24,x] += probToAdd
            M[39,x] += probToAdd
            M[5,x] += probToAdd            
            # 2 cards to next RR
            M[nextRR[n],x] += 2*probToAdd
            # 1 card to next Utility
            M[nextUtility[n],x] += probToAdd
            # 1 card, go back three squares
            M[c-3,x] += probToAdd
    for c in chance:
        for x in range(40):
            M[c,x] *= 3.0/8.0

def goToJail(M):
    # No turn can end on Go To Jail.  
    for x in range(40):
        M[JAIL,x] += M[30,x]
        M[30,x] = 0

def tripleDouble(M,n):
    """ Rolling doubles 3 times in a row sends the player to Jail.
    All probabilities of ending on a spot which is not jail must be reduced
    by the probability of rolling 3 doubles in a row.
    The probability of ending in jail must be increased by the same.

    M is the Markov Matrix
    n is the number of faces on a die (weighted dice not implemented yet)
    """
    probTripDoub = (1.0 / float(n))**3
    notJail = [x for x in range(40) if not x==JAIL]
    for x in notJail:
        for y in range(40):
            M[JAIL,y] += probTripDoub * M[x,y]
            M[x,y] *= (1-probTripDoub)
    

def calcSteadyState(M):
    b = scipy.ones(40) / 40.0
    A = matrix_power(M,50000)
    return scipy.dot(A,b)

def Euler84(diceSize=4, diceProbabilities=None):
    if diceProbabilities == None:
        diceProbabilities = createFairDice(diceSize)
    M = buildRawMonopoly(diceProbabilities)
    accountForCommunity(M)
    accountForChance(M)
    goToJail(M)
    tripleDouble(M,diceSize)
    p = calcSteadyState(M)
    pList = [(i,x) for i,x in enumerate(p)]
    pList.sort(key = lambda x: x[1])

    print pList[-1], pList[-2], pList[-3]
    return p, M
