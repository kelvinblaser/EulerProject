###############################################################################
# Euler 213 - Flea Circus
# Kelvin Blaser     2014.12.30
#
# Calculate the probability distribution for each ant, then note that the
# probability of a particular square being empty is the product of the
# probabilities that each ant is not on that sqaure, independent of what is
# going on on the other squares
#
# Takes about 5 minutes to run.  A faster method would be to make a 900x900
# transition matrix, exponentiate M^50, multiply by a vector of ones to get p,
# and then sum 1-p(j).
###############################################################################
import scipy as sp
import pylab as pl

class FleaDist(object):
    ''' Probability distribution of a particular flea on the board. '''
    def __init__(self,n,i,j):
        ''' Initial position of the flee is i,j. Size of board is n. '''
        self.board = sp.zeros((n,n),dtype=float)
        self.board[i%n,j%n] = 1.0
        self.n = n
        self.i = i
        self.j = j

    def ringBell(self):
        ''' Update the distribution when the flea jumps due to the bell. '''
        n = self.n
        new_board = sp.zeros((n,n),dtype=float)
        for i in range(n):
            for j in range(n):
                p = self.board[i,j]
                neighbors = self.getNeighbors(i,j)
                num_neighbors = len(neighbors)
                for x,y in neighbors:
                    new_board[x,y] += p / num_neighbors
        self.board = new_board

    def getNeighbors(self,i,j):
        neighbors = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
        n = self.n
        if i == 0:
            neighbors.remove((i-1,j))
        if i == n-1:
            neighbors.remove((i+1,j))
        if j == 0:
            neighbors.remove((i,j-1))
        if j == n-1:
            neighbors.remove((i,j+1))
        return neighbors

def calcExpUnoccupied(flea_dists, n):
    e = 0.0
    for i in range(n):
        for j in range(n):
            eplus = 1.0
            for fd in flea_dists:
                eplus *= 1-fd.board[i,j]
            e += eplus
    return e

def Euler213(n, bell_rings=50, to_plot=[]):
    flea_dists = [FleaDist(n,x/n,x%n) for x in range(n*n)]
    for fd in flea_dists:
        print fd.i, fd.j
        for x in range(bell_rings):
            fd.ringBell()
    z = 1
    for i,j in to_plot:
        pl.figure(z)
        pl.imshow(flea_dists[i*n+j].board)
        z += 1
    pl.show()
    return calcExpUnoccupied(flea_dists, n)

if __name__ == '__main__':
    print Euler213(8, 50, [(1,1), (3,3)])#(29,14), (14,14)])
