# Euler 81 - Matrix Path Easy
# Kelvin Blaser     11-17-2012
from numpy import inf
import scipy

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
