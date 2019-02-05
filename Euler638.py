# Euler 638

def C(a,b,k,MOD):
    print k
    num, den = 1,1
    for n in range(1, b+1):
        num *= pow(k, a+n, MOD) - 1
        num %= MOD
        den *= pow(k, n, MOD) - 1
        den %= MOD
    return (num * pow(den, MOD-2, MOD)) % MOD
    
if __name__ == '__main__':
    choose22_11 = (22*21*20*19*18*17*16*15*14*13*12)/(11*10*9*8*7*6*5*4*3*2)
    ans = choose22_11 + sum(C(10**k+k, 10**k+k, k, 10**9+7) for k in range(2,8))
    print ans % (10**9+7)