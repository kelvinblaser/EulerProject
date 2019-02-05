##############################################################################
# Euler 405 - A Rectangular Tiling
# Kelvin Blaser      2014.12.25    Merry Christmas ya filthy animal!
#
# This problem has a closed form solution.  Let
#       g(m) = (2^(4m+2) - 2^(2m+2))/3 - 14(2^4m-1)/15
# Then,
#       f(2m)   = g(m)
#       f(2m+1) = 4g(m) + (2^(2m+3)-8)/3
#
# The trick is doing the huge modular exponential when n=2m = 10^10^18.
#
# I found the closed form solution by considering what happens when I take
# four rectangles of rank n-1 and arrange them as a rectangle of rank n.
##############################################################################

def g(m):
    ans = 2**(4*m+2) - 2**(2*m+2)
    ans /= 3
    ans -= 14 * (2**(4*m) - 1) / 15
    return ans

def f(n):
    if n%2 == 0:
        return g(n//2)
    ans = 4*g(n//2)
    ans += (2**(n+2) - 8) / 3
    return ans

def f10(k):
    ''' Solving f(n) % 17**7 where n = 10**k '''
    # Want to solve for g(10**k / 2)  m shows up as 2m everywhere, so let
    # 2m = 10**k and rewrite g(m)

    # Some working values
    MOD1 = 17**7
    MOD2 = 2**4 * 17**6             # Euler's totient phi(17^7)
    inv3 = pow(3,MOD2-1,MOD1)       # Inverse of 3 mod 17^7
    inv15 = pow(15, MOD2-1, MOD1)   # Inverse of 15 mod 17^7

    # (2^(2*10^k+2) - 2^(10^k+2))/3
    ans1 = pow(2,(2*pow(10,k,MOD2)+2)%MOD2,MOD1)
    ans1 -= pow(2,(pow(10,k,MOD2)+2)%MOD2,MOD1)
    ans1 *= inv3
    ans1 %= MOD1

    # 14 (2^(2*10^k) - 1) / 15
    ans2 = pow(2, (2*pow(10,k,MOD2))%MOD2, MOD1)
    ans2 -= 1
    ans2 *= 14 * inv15
    ans2 %= MOD1

    return (ans1 - ans2)%MOD1
    

if __name__ == '__main__':
    print 'f(%d) = %d'%(1,f(1))
    print 'f(%d) = %d'%(2,f(2))
    print 'f(%d) = %d'%(3,f(3))
    print 'f(%d) = %d'%(4,f(4))
    print 'f(10^%d) = %d MOD 17^7'%(9,f10(9))
    print 'f(10^10^%d) = %d MOD 17^7'%(18,f10(10**18))
