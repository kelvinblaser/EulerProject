###############################################################################
# Euler 219 - Skew-cost Coding
# Kelvin Blaser     2014.12.31      Happy New Years!  Good riddance 2014.
#
# Think about a minimum cost coding of size n-1.  To get a prefix-free coding of
# length n, pick one of the strings and add a 0 and a 1 to it.  If you choose
# the string of smallest cost, then this will be the minimum cost coding of size
# n.
#
# The algorithm is to start with the min-cost coding of size 2, then increase
# the size by adding one string.  Only need to keep track of the cost of each
# string, since the actual string doesn't matter, just the total cost.  I will
# keep track of how many strings of cost x I have, keeping the memory
# requirement O(log n).  For each step, just subtract one from the minimum cost
# pool of strings and add one to min_cost + cost_zero and add one to
# min_cost + cost_one.
###############################################################################
from fractions import gcd
import scipy as sp

def minSkewCost(N, cost_zero=1, cost_one=4):
    g = gcd(cost_zero, cost_one)
    cost_zero /= g
    cost_one /= g
    strings = sp.zeros((int(sp.log(N)/sp.log(2))+1)*max(cost_zero, cost_one),
                       dtype=int)
    strings[cost_zero] = 1
    strings[cost_one] = 1
    min_cost = min(cost_zero, cost_one)
    n_strings = 2
    while n_strings < N:
        while strings[min_cost] == 0:
            min_cost += 1
        to_move = min(strings[min_cost], N-n_strings)
        strings[min_cost] -= to_move
        strings[min_cost+cost_one] += to_move
        strings[min_cost+cost_zero] += to_move
        n_strings += to_move
    cost = 0L
    for x in xrange(len(strings)):
        cost += long(x)*strings[x]
    return cost

if __name__=='__main__':
    print minSkewCost(6,1,4)
    print minSkewCost(10,1,4)
    print minSkewCost(10**9,1,4)
