# Euler 641 

from Primes import MakePrimeList

class DiceCounter:
    def __init__(self, N):
        self.N = N
        self.primes = MakePrimeList(int(N**0.25) // 16 + 1)
        
        
if __name__ == '__main__':
    dc = DiceCounter(10**8)
    print 'Num Primes: {0}'.format(len(dc.primes))
    print 'Largest Prime: {0}'.format(dc.primes[-1])
    