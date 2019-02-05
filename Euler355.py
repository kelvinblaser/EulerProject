# Euler 335 - Gathering the Beans
# Kelvin Blaser         2015.1.7

MOD = 7**9
PHI = 6*7**8

def inv(x):
    return pow(x,PHI-1,MOD)

def Euler355(n):
    ans = 2*(pow(2,n+1,MOD)-1)*inv(2-1)
    ans -= (pow(3,n+1,MOD)-1)*inv(3-1)
    ans += (pow(4,n+1,MOD)-1)*inv(4-1)
    return ans % MOD

if __name__ == '__main__':
    print Euler355(10**18)
