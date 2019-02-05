# Euler 575
#
# Only 3 types of rooms, corners, edges and interiors

from fractions import Fraction

class ShipRooms:
    def __init__(self, eps):
        self.eps = eps
        
    def __call__(self, n):
        tA = Fraction(1, 12 + 16*(n-2) + 5*(n-2)**2)
        pCornerA, pEdgeA, pInteriorA = 3*tA, 4*tA, 5*tA
        tB = Fraction(1, 8 + 12*(n-2) + 4*(n-2)**2)
        pCornerB, pEdgeB, pInteriorB = 2*tB, 3*tB, 4*tB
        
        corners, edges, interiors = 0, 0, 0
        for x in range(1, n+1):
            x2 = x*x
            row = (x2-1) % n
            col = (x2-1) // n
            
            numEdges = 0
            if row == 0 or row == n-1: numEdges += 1
            if col == 0 or col == n-1: numEdges += 1
            
            if numEdges == 0: interiors += 1
            elif numEdges == 1: edges += 1
            else: corners += 1
            
        pA = corners * pCornerA + edges * pEdgeA + interiors * pInteriorA
        pB = corners * pCornerB + edges * pEdgeB + interiors * pInteriorB
        
        print 'tA = {0}, pCA = {1}, pEA = {2}, pIA = {3}'.format(tA, pCornerA, pEdgeA, pInteriorA)
        print 'tB = {0}, pCB = {1}, pEB = {2}, pIB = {3}'.format(tB, pCornerB, pEdgeB, pInteriorB)
        print 'Corners: {0}, Edges: {1}, Interiors: {2}'.format(corners, edges, interiors)
        print 'pA = {0}, pB = {1}'.format(pA, pB)
        p = (pA + pB) / 2
        print 'p = {0} = {1}'.format(p, float(p))
        return p
                
    def steadyStates(self, n):
        pRoomsA = [[1.0 for col in range(n)] for row in range(n)]
        pRoomsB = [[1.0 for col in range(n)] for row in range(n)]
        pTransA = [[1.0 / (self.numNeighbors(row, col, n) + 1.0) for col in range(n)] for row in range(n)]
        pTransB = [[1.0 / (2.0 * self.numNeighbors(row, col, n)) for col in range(n)] for row in range(n)]
        #print pTransA
        #print pTransB
        done = False
        iters = 0
        while not done:
            iters += 1
            done = True
            newRoomsA = [[0.0 for col in range(n)] for row in range(n)]
            newRoomsB = [[0.0 for col in range(n)] for row in range(n)]
            for row in range(n):
                for col in range(n):
                    oldA = pRoomsA[row][col]
                    newRoomsA[row][col] = pTransA[row][col] * oldA
                    oldB = pRoomsB[row][col]
                    newRoomsB[row][col] = 0.5 * oldB
                    if row != 0: 
                        newRoomsA[row][col] += pTransA[row-1][col] * pRoomsA[row-1][col]
                        newRoomsB[row][col] += pTransB[row-1][col] * pRoomsB[row-1][col]
                    if row != n-1: 
                        newRoomsA[row][col] += pTransA[row+1][col] * pRoomsA[row+1][col]
                        newRoomsB[row][col] += pTransB[row+1][col] * pRoomsB[row+1][col]
                    if col != 0: 
                        newRoomsA[row][col] += pTransA[row][col-1] * pRoomsA[row][col-1]
                        newRoomsB[row][col] += pTransB[row][col-1] * pRoomsB[row][col-1]
                    if col != n-1: 
                        newRoomsA[row][col] += pTransA[row][col+1] * pRoomsA[row][col+1]
                        newRoomsB[row][col] += pTransB[row][col+1] * pRoomsB[row][col+1]
                    if (not done) or abs(oldA - newRoomsA[row][col]) > self.eps or abs(oldB - newRoomsB[row][col]) > self.eps: done = False
            pRoomsA = newRoomsA
            pRoomsB = newRoomsB
        print 'iters : ', iters
        return pRoomsA, pRoomsB
        
                    
    def numNeighbors(self, row, col, n):
        numNeighbors = 4
        if row == 0: numNeighbors -= 1
        if row == n-1: numNeighbors -= 1
        if col == 0: numNeighbors -= 1
        if col == n-1: numNeighbors -= 1
        return numNeighbors
        
if __name__ == '__main__':
    sr = ShipRooms(1e-12)
    for n in range(2,9):
        print '------ n : {0} ------'.format(n)
        sr(n)
        print ''
        
    print '------ n : 1000 ------'
    sr(1000)