###############################################################################
# Euler 242 - Odd Triplets
# Kelvin Blaser     2015.1.24
#
# Consider a recurrence relation for f(n,k).  Let g(n,k) be the number of
# size k subsets of {1,2,...,n} which sum to an EVEN number.  We can consider
# the subsets which contain n, and those which don't.
#
#       f(n,k)  =   0                       if k = 0, k < 0, k > n
#               = f(n-1, k) + f(n-1,k-1)    if n is even
#               = f(n-1, k) + g(n-1,k-1)    if n is odd
#
#       g(n,k)  = 1                         if k = 0
#               = 0                         if k < 0 or k > n
#               = g(n-1, k) + g(n-1,k-1)    if n is even
#               = g(n-1, k) + f(n-1,k-1)    if n is odd
#
# Now consider c(n,k) = f(n,k) + g(n,k)  Clearly this is the binomial
# coefficient n choose k since it is the number of size k subsets of n without
# regards to evenness or oddness.
#
# Let's apply the recursion to f(n,k) and g(n,k) twice to get new recursions.
#
#       f(n,k)  = f(n-2,k) + g(n-2,k-1) + f(n-2,k-1) + g(n-2,k-2)  if n is even
#               = f(n-2,k) + f(n-2,k-1) + g(n-2,k-1) + g(n-2,k-2)  if n is odd
#
#               = f(n-2,k) + c(n-2,k-1) + g(n-2,k-2) either way
#
#       g(n,k)  = g(n-2,k) + c(n-2,k-1) + f(n-2,k-2)
#
# Now apply this new recurrence relation to itself along with the binomial
# coefficient recursion twice
#
#       f(n,k)  =   f(n-4,k) + c(n-4,k-1) + g(n-4,k-2)
#                 + c(n-4,k-1) + 2c(n-4,k-2) + c(n-4,k-3)
#                 + g(n-4,k-2) + c(n-4,k-3) + f(n-4,k-4)
#
#               = f(n-4,k) + f(n-4,k-4)
#                 + 2[ g(n-4,k-2) + c(n-4,k-1) + c(n-4,k-2) + c(n-4,k-3) ]
#
#               = f(n-4,k) + f(n-4,k-4) mod 2
#
# We see that the parity of f(4q+x,4p+y) follows a binomial coefficient pattern
# in q and p.  Thus the parity of f(n,k) depends on the parity of c(q,p) and
# and the base case f(x,y).  If the base case is even, the whole Pascal's
# triangle associated with it is even.
#
# We are interested in the 4 cases where n and k are both odd.
#       f(1,1) = 1
#       f(1,3) = 0
#       f(3,1) = 2 = 0 mod 2
#       f(3,3) = 0
#
# Thus there are only odd triplets for n = k mod 4 = 1 mod 4.  Further more,
# the number of these with n <= N is the number of odd entries in Pascal's
# triangle below row (N+3)/4
#
#------------------------------------------------------------------------------
#   Calculating the number of odd entries in Pascal's triangle.
#   ----------------------------------------------------------
# We know based on Lucas' theorem that Pascal's triangle has a self similar
# structure modulo a prime.  In particular, modulo 2.
#
# Let Pm be Pascal's triangle below row m.  When m = 2^l for l = 1,2,3,4,
# P(2m) looks like a bit like a triforce composed of 3 copies of Pm and an
# upside down triangle section of zeros
#
#                           /\
#                          /  \
#                         / Pm \
#                        /      \
#                       /--------\
#                      /\        /\
#                     /  \  00  /  \
#                    / Pm \    / Pm \
#                   /      \  /      \
#                  /--------\/--------\
#
# Let h(q) be the number of odd entries below row q.
#       h(0)        = 0
#       h(1)        = 1
#       h(2^n)      = 3*h(2^(n-1))  ==> h(2^n) = 3^n
#       h(2^n + z)  = 3^n + 2*h(z)  if z < 2^n
#
# The solution to the Euler problem is simply h((10^12+3)//4)
###############################################################################

def h(q):
    if q < 2:
        return q
    x = q
    n = 0
    while x > 1:
        n += 1
        x /= 2
    return 3**n + 2*h(q%(2**n))

def h1(q):  # Non-recursive version
    ans = 0
    n = 0
    while q > 0:
        if q % 2 == 1:
            ans *= 2
            ans += 3**n
        q /= 2
        n += 1
    return ans
            

def Euler242(N):
    return h((N+3)//4)

if __name__ == '__main__':
    print Euler242(10**12)
    print h1((10**12+3)/4)
    
