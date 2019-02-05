################################################################################
# Euler 321 - Swapping Counters
# Kelvin Blaser      2015.03.07
#
# Minimum number of moves is x = n(n+2).  We need n(n+2) = m(m+1)/2 which can be
# turned into a Pell like equation by multiplying through by 8 and completing
# the square.
#
#       (8n^2 + 16n) - (4m^2 + 4m) = 0
#       8(n^2 + 2n + 1) - (4m^2 + 4m + 1) = 8-1
#       8(n+1)^2 - (2m+1)^2 = 7
#       x^2 - 8y^2 = -7  where x = 2m+1 and y = n+1
#
# Can solve this by composing the base solution (x,y) = (1,1) with the solutions
# (r,s) to r^2 - 8s^2 = 1 in the manner prescribed at wolfram math world
#   http://mathworld.wolfram.com/PellEquation.html   equations 39-42
################################################################################
from Euler import positivePell
    
def Euler321(N):
    D = 8
    p,q = 1,1
    xySols = set()
    for r,s in positivePell(D,(N+1)//2):
        xySols.add((p*r+D*q*s,p*s+q*r))
        xySols.add((D*q*s-p*r,q*r-p*s))
    nSols = [abs(y)-1 for x,y in xySols]
    nSols.sort()
    return sum(nSols[:N])


if __name__ == '__main__':
    print Euler321(5)
    print Euler321(40)
