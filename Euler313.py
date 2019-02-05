################################################################################
# Euler 313 - Sliding Game
# Kelvin Blaser      2015.03.07
#
# Let m >= n
# Case m = n, takes 8m - 11 moves
# Case m > n, takes 6m + 2n - 13 moves
# This is shown by moving the red stone diagonally as far as possible, then
# along the long direction.
#
# So we have for each p, twice the number of solutions p^2 + 13 = 6m + 2n with
# m > n and n > 1 plus the number of solutions to p^2 + 11 = 8m
#
# For p = 2, there are no solutions, since the RHS of both equations is odd,
# while the left hand side is even.  For odd primes, p = 1,3,5 or 7 mod 8 and
# 1,3,5 mod 6
#   mod 8   p   p^2   p^2+11    p^2+13        mod 6   p   p^2    p^2+13
#           1    1      4           6                 1    1        2
#           3    1      4           6                 3    3        4
#           5    1      4           6                 5    1        2
#           7    1      4           6
#
# We see that there are no solutions to p^2 + 11 = 8m.  The solutions to
# p^2 + 13 = 6m + 2n with m > n and n > 1 are given when
#    (p^2+13)/8 < m <= (p^2+9)/6
#
# There are (p^2+9)//6 - (p^2+13)//8 such solutions.
################################################################################
from Primes import MakePrimeList

def Euler313(N):
    primes = MakePrimeList(N)
    ret = 0
    for p in primes[1:]:
        ret += (p*p+9)//6 - (p*p+13)//8
    return 2*ret

if __name__ == '__main__':
    print Euler313(100)
    print Euler313(1000000)
