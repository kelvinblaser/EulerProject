################################################################################
# Euler 517 - A Real Recursion
# Kelvin Blaser      2015.07.07
#
# 
################################################################################
from Primes import Miller_Rabin
#import numpy as np

MOD = 1000000007 # Must be prime
MIN = 10000000
MAX = 10010000
#factorials = np.ones(MAX,dtype=np.int64)
factorials = [1] * MAX
for x in range(1,MAX):
    factorials[x] = (factorials[x-1]*x) % MOD 
def G(n,MOD=MOD):
    rt = n**0.5
    ret = 0
    for k in range(int(rt)):
        m = int(n - (k+1)*rt + k + 1)
        #print m,k+1
        ret += choose(m,k+1,MOD)
        ret %= MOD
    return (ret+1) % MOD

def choose(n,k,MOD=MOD):
    if k > n or k < 0:
        return 0
    if k > n//2:
        k = n-k
    num = factorials[n]
    den = (factorials[k]*factorials[n-k]) % MOD
##    try:
##        return memo[(n,k)]
##    except KeyError:
##        pass
##    num, den = 1,1
##    for kk in range(1,k+1):
##        num *= n-kk+1
##        den *= kk
##        num %= MOD
##        den %= MOD
    return (num * pow(den,MOD-2,MOD)) % MOD
##    memo[(n,k)] = (num * pow(den,MOD-2,MOD)) % MOD
##    return memo[(n,k)]

if __name__ == '__main__':
    ans = 0
    for p in range(MIN+1,MAX):
        if Miller_Rabin(p):
            g = G(p)
            ans += g
            ans %= MOD
            print p,g,ans
    print ans
