# Euler 81 - Matrix Path Easy
# Kelvin Blaser     11-17-2012
from numpy import inf
import scipy
from time import clock

def getMatrix(fileName):
    fin = open(fileName,'r')
    rows = fin.readlines()
    M = []
    for row in rows:
        row = row.split(',')
        for n,num in enumerate(row):
            row[n] = int(num)
        M.append(row)
    fin.close()
    return scipy.array(M)

def checkNeighbor(site1, site2, M, minPath, nextShell):
    l = minPath[site1] + M[site2]
    if l < minPath[site2]:
        minPath[site2] = l
        nextShell.append(site2) 
        
def Euler81(fileName):
    M = getMatrix(fileName)
    size = len(M)
    for x in range(size):
        for y in range(size):
            if not (x==0 and y==0):
                if x==0:
                    M[x,y] += M[x,y-1]
                elif y==0:
                    M[x,y] += M[x-1,y]
                else:
                    M[x,y] = min(M[x,y] + M[x-1,y], M[x,y] + M[x,y-1])

    return M[-1,-1]

def Euler82(fileName):
    start = clock()
    M = getMatrix(fileName)
    minPath = M * inf
    size = len(M)

    # Initialize the current Shell to be the top left corner
    currentShell = []
    for x in range(size):
        currentShell.append((x,0))
        minPath[x,0] = M[x,0]

    # Move out shell by shell, adding a location to a shell if its minPath is
    # changed
    while len(currentShell) > 0:
        nextShell = []   
        for site in currentShell:
            x = site[0]
            y = site[1]
            # Check up
            if not x==0:
                site2 = (x-1, y)
                checkNeighbor(site, site2, M, minPath, nextShell)
            # Check down
            if not x==size-1:
                site2 = (x+1, y)
                checkNeighbor(site, site2, M, minPath, nextShell)
            # Check right
            if not y==size-1:
                site2 = (x, y+1)
                checkNeighbor(site, site2, M, minPath, nextShell)
        currentShell = nextShell
    print clock()-start
    return min(minPath[:,-1])

def Euler83(fileName):
    start = clock()
    M = getMatrix(fileName)
    minPath = M * inf
    size = len(M)

    # Initialize the current Shell to be the left side
    currentShell = [(0,0)]
    minPath[0,0] = M[0,0]

    # Move out shell by shell, adding a location to a shell if its minPath is
    # changed
    while len(currentShell) > 0:
        nextShell = []   
        for site in currentShell:
            x = site[0]
            y = site[1]
            # Check up
            if not x==0:
                site2 = (x-1, y)
                checkNeighbor(site, site2, M, minPath, nextShell)
            # Check down
            if not x==size-1:
                site2 = (x+1, y)
                checkNeighbor(site, site2, M, minPath, nextShell)
            # Check left
            if not y==0:
                site2 = (x, y-1)
                checkNeighbor(site, site2, M, minPath, nextShell)
            # Check right
            if not y==size-1:
                site2 = (x, y+1)
                checkNeighbor(site, site2, M, minPath, nextShell)
        currentShell = nextShell
    print clock()-start
    return minPath[-1,-1]
    
