################################################################################
# Euler 523 and 524 - First Sort I and II
# Kelvin Blaser      2015.09.22
#
#===============================================================================
# Euler 523
#
# If the first i-1 elements are sorted and element i needs to be inserted at
# position j < i, it takes 2^(j-1) moves to do that.  Then there are at least
# i sorted elements.  Thus the expectation value E(n) should be the expectation
# value of sorting the first n-1 elements plus the expected number of moves to
# sort the final value.
#
#       E(n) = E(n-1) + 1/n * sum(2^(k-1), k = 1..n-1)
#            = E(n-1) + 1/n * (2^(n-1)-1)
#
# E(n-1) can then extended to get a  
#===============================================================================
# Euler 524
#
# The solution will proceed in two steps.
#   1. Explicitly build the lexicographically smallest permutation that takes n
#      steps to sort.
#   2. Calculate the lexicographical index of that permutation.
#
# 1. Determine the permutation.
#-----------------------------------
# k has a binary representation.  The ones in its binary representation
# determine which values j we need to insert the first unsorted element into as
# the sort progresses to get exactly k moves.  We can create the permutation by
# starting with the sorted permutation and working backwards.  Trial and error
# has convinced me that to get the lexicographically smallest permutation, the
# valued which is to be inserted in slot j needs to be in slot j+1.
#
# The solution is to simply swap perm[b] with perm[b+1] (indexing starting with
# 1) for each bit position b that is a 1 in the binary representation of k,
# starting with the highest order bit and working down.
#
# 2. Calculate index
#-----------------------------------
# If a permutation has n items, then there are (n-1)! permutations that start
# with item 1, (n-1)! that start with item 2, etc.  Thus the first item in the
# permutation tells you roughly how many permutations are before it.  The
# remaining permutation refines that estimate until the final item gives you the
# correct index.
#
#----------------------------------
# Hmmmmm, something's wrong with my method.  Gives correct answer for 5 and 7,
# but apparently not for 12^12
################################################################################
from scipy import prod

def expected_moves(n):
    s = 0.0
    for j in range(1, n+1):
        s += (2**(j-1)-1)/float(j)
    return s

def create_permutation(k):
    # Create the initial sorted permutation and get the 
    # binary representation of k.
    b = 1
    binary_rep = []
    while k > 0:
        if k%2==1:
            binary_rep.append(b)
        k /= 2
        b += 1
    perm = list(range(1,b+1))
    # permute the permutation 
    for b in binary_rep[::-1]:
        perm[b-1],perm[b] = perm[b],perm[b-1]
    return perm

def permutation_index(perm):
    n = len(perm)
    nMinus1Fact = 1
    for k in range(2,n):
        nMinus1Fact *= k
    ix = 1  # Indices start with 1
    while len(perm) > 1:
        p = perm[0]
        ix += (p-1)*nMinus1Fact
        perm = perm[1:]
        for j in range(len(perm)):
            if perm[j] > p:
                perm[j] -= 1
        n -= 1
        nMinus1Fact /= n
        
    return ix

def min_index(k):
    if k == 0:
        return 1
    return permutation_index(create_permutation(k))
    

if __name__ == '__main__':
    print 'E(4) = %f'%(expected_moves(4),)
    print 'E(10) = %f'%(expected_moves(10),)
    print 'E(30) = %f'%(expected_moves(30),)
    print ''
    print 'R(5) = %d'%(min_index(5),)
    print 'R(7) = %d'%(min_index(7),)
    print 'R(12^12) = %d'%(min_index(12**12),)
