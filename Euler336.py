################################################################################
# Euler 336 - Maximix Arrangements
# Kelvin Blaser      2015.02.20
#
# Think of a maximix arrangement with letters B,C,D,.... We want all
# arrangments which place an 'A' somewhere where it will take to rotations to
# get the 'A' to the beginning and we will be left with a maximix arrangement
# of the rest of the letters.
#
# Can start with small arrangements and build up to large. Think of [1..2] and
# [3..4] as pieces of a maximix string.  The larger maximix string will rotate
# into
#           'A'[1..2][3..4]  from
#           [4..3][2..1]'A'  from
#           [4..3]'A'[1..2]
# Thus from each smaller arrangement, we can build a number of larger
# arrangements depending on where we split the smaller arrangement and place the
# 'A'
################################################################################
from string import ascii_uppercase

def letter2index(letter):
    return ascii_uppercase.find(letter)

class MaximixArrangements:
    def __init__(self):
        self.arrangements = [['A'],['BA']]

    def __call__(self, n, m):
        ''' Finds the mth lexicographical maximix arrangement for n letters'''
        if n > len(self.arrangements):
            self.calcArrangements(n)
        if m > len(self.arrangements[n-1]):
            raise KeyError
        return self.arrangements[n-1][m-1]

    def calcArrangements(self, n):
        for nn in range(len(self.arrangements),n):
            new_arrangements = []
            for arr in self.arrangements[nn-1]:
                new_arrangements += self.newArrange(arr)
            new_arrangements.sort()
            self.arrangements.append(new_arrangements)
        return

    def newArrange(self, arr):
        new_arr = ''.join([ascii_uppercase[letter2index(c)+1] for c in arr])
        return [new_arr[len(arr):n-1:-1]+'A'+new_arr[:n] for n in range(1,len(arr))]
        
if __name__ == '__main__':
    x = MaximixArrangements()
    print x(6,10)
    print x(11,2011)
