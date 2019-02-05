###############################################################################
# Euler 497 - Drunken Tower of Hanoi
# Kelvin Blaser     2015.1.13
#
# This problem can be broken into two sub-problems.
#  1.  Find the number of times Bob has to move from a to b, a to c, etc.
#   -  Only depends on n, the number of discs in the tower.
#  2.  Figure out the expected number of moves to get from a to b, etc.
#   -  Depends on a, b, c, and k, but not n
#
# The solution will be the solution to part 1, multiplied by the solution to
# part two.
#
#------------------------------------------------------------------------------
# 1. Let M(n,a,b) be the act of moving a tower of size n from a to b. Then
#       M(n+1,a,c) = M(n,a,b) + 1ba + 1ac + 1cb + M(n,b,c)
#       M(n+1,a,b) = M(n,a,c) + 1ca + 1ab + 1bc + M(n,c,b)
#       M(n+1,b,c) = M(n,b,a) + 1ab + 1bc + 1ca + M(n,a,c)
#           etc.
#   I will write a function M(n,x,y) which returns Nab, Nac, Nba, Nbc, Nca, Ncb
#   where Npq is the number of moves from p to q required when moving a stack
#   of size n from x to y.  x,y,p,q take the values a,b,c
#
#------------------------------------------------------------------------------
# 2. To solve for the expected number of moves to get from slot x to slot y
#    when x < y, there is a linear system of equations to solve
#
#       E1y = E2y + 1
#       E2y = 1/2 E1y + 1/2 E3y + 1
#           ...
#       Eiy = 1/2 Ei-1,y + 1/2 Ei+1,y + 1
#           ...
#       Ey-1,y = 1/2 Ey-2,y + 1
#
#    After solving these for a few different y, I figured out the pattern and
#    found the solution
#       Exy = y(y-2) - x(x-2)
#
#    When x > y, it is just a mirror image with slot k corresponding to slot 1.
#    Just replace x with k-x+1 and y with k-y+1.
#------------------------------------------------------------------------------
# My method gets the right answer for the examples given on the project Euler
# page, but for some reason the final answer is incorrect.  I thought it might
# be overflow errors, but I'm using python's big integers everywhere.
#
# As far as I can reason, the general algorithm is correct. It's possible I
# have fence-post errors somewhere, but I was really careful about that.
#
# AH-HA, I figured it out.  When calculating Exy, I use the test x > y to see
# if I need to change x and y to k-x+1 and k-y+1.  But with the modular math,
# there is no gaurantee that x%MOD > y%MOD is the same as x > y.
###############################################################################
MOD = 10**9
cache = {}

def M(n, start, end, cache={}):
    # Answer order is (Nab, Nac, Nba, Nbc, Nca, Ncb)
    other = (2*(start+end)) % 3
    if n == 1:
        ans = [0,0,0,0,0,0]
        ix = 2*start + (end > other)
        ans[ix] += 1
        return tuple(ans)
    
    key = (n, start, end)
    try:
        return cache[key]
    except KeyError:
        pass

    N = list(M(n-1,start,other,cache))
    N[2*other+(start > end)] += 1
    N[2*start+(end > other)] += 1
    N[2*end+(other > start)] += 1
    N = [(N[i]+list(M(n-1,other,end,cache))[i])%MOD for i in range(6)]

    cache[key] = tuple(N)
    return cache[key]

def Exy(x,y,k,left=False):
    if left:
        x,y = k-x+1,k-y+1
    return (y*(y-2) - x*(x-2))%MOD

def Eabck(a,b,c,k):
    return [Exy(a,b,k,left=False), Exy(a,c,k,left=False), Exy(b,a,k,left=True),
            Exy(b,c,k,left=False), Exy(c,a,k,left=True),  Exy(c,b,k,left=True)]

def E(n,k,a,b,c):
    NN = list(M(n,0,2,cache))
    NN[2] += 1
    EE = Eabck(a,b,c,k)
    ans = 0
    for i in range(6):
        ans += (NN[i]*EE[i])%MOD
    return ans%MOD

def Euler497():
    ans = 0
    for n in xrange(1,10001):
        ans += E(n,pow(10,n,MOD),pow(3,n,MOD),pow(6,n,MOD),pow(9,n,MOD))
    return ans % MOD

if __name__ == '__main__':
    print 'E(2,5,1,3,5) = %d'%(E(2,5,1,3,5),)
    print 'E(3,20,4,9,17) = %d'%(E(3,20,4,9,17),)
    print 'Euler 497: %d'%(Euler497(),)
