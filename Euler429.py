#Euler 429 - Unitary divisors
# Kelvin Blaser

import Primes

def get_r(p,n):
    r = 0
    d = p
    while d <= n:
        r += n / d
        d *= p
    return r

def pow_mod(base, exp, mod):
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod

    x = pow_mod(base, exp/2, mod)
    if exp%2 == 0:
        return (x*x) % mod
    else:
        return (((x*x) % mod) * base) % mod


MOD = 1000000009
n = 10**5
p_list = Primes.MakePrimeList(n)
print 'Primes Built',
print ' '
r_list = [get_r(p,n) for p in p_list]
print 'Exponents Built'
ans = 1
for i in range(len(p_list)):
    ans *= (pow_mod(p_list[i], 2*r_list[i], MOD) + 1)
    ans %= MOD
print 'S('+str(n)+'!) = ', ans
