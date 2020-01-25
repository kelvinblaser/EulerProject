# Euler 668
from Primes import MakePrimeList, intRoot, Prime_Pi

def root_smooth(N):
    r = intRoot(N)
    primes = MakePrimeList(r)

    res = sum(primes)
    pp = Prime_Pi()
    for x in range(1, r+1):
        #print(pp(N//x, primes), pp(max(r, N//(x+1)), primes))
        res += x * (pp(N//x, primes) - pp(max(r, N//(x+1)), primes))
    return N - res

if __name__ == '__main__':
    print('Root smooths under {}: {}'.format(100, root_smooth(100)))
    print('Root smooths uner 10^10: {}'.format(root_smooth(10**10)))
