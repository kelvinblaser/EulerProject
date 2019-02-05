# Euler 479 - Roots on the Rise
# https://projecteuler.net/problem=479
# Kelvin Blaser   2014.11.11
#
# Use Vieta's formulas to recognize that abc = k^2, ab+bc+ac = 1/k, and
# a+b+c = k.  Then show that f = (a+b)(b+c)(a+c) = 1-k^2
#
# Finally S(n) = sum(k=1..n sum(p=1..n) f_k^p))
#              = sum(k=1..n  f_k (f_k^n-1)/(f_k-1))
#              = sum(k=1..n  (k^2-1)[(1-k^2)^n](k^2)^(q-2)) mod q
#                    where q = 1000000007 is prime

def Euler479(n,q=1000000007):
    ans = 0
    for k in range(1,n+1):
        ans += (k*k-1) * (pow(1-k*k,n,q)-1) * pow(k*k,q-2,q)
        ans %= q
    return ans

if __name__ == '__main__':
    print Euler479(4)
    print Euler479(10**6)
