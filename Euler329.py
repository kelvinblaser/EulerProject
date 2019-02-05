###############################################################################
# Euler 329 - Prime Frog
# Kelvin Blaser     2015.2.6
#
# Frog is at some given square.  Calculate probability he will make the
# correct croak.  Then multiply by the probability he will make the rest of the
# croaks correct, calculated by recursion. Average over starting positions.
#
# Memoized for speed.
###############################################################################
import Primes
from fractions import Fraction

def calcCroakProbability(N,position,croak_string,ps,memo):
    if len(croak_string) == 0:
        return 1
    key = (N,position,croak_string)
    try:
        return memo[key]
    except KeyError:
        pass
    
    prob_croak_correct = Fraction(1,3)
    is_prime = Primes.isPrime(position,ps)
    if ((is_prime and croak_string[0] == 'P') or
        (not is_prime and croak_string[0] == 'N')):
        prob_croak_correct *= 2
        
    if position == 1:
        memo[key] = calcCroakProbability(N,2,croak_string[1:],ps,memo)
    elif position == N:
        memo[key] = calcCroakProbability(N,N-1,croak_string[1:],ps,memo)
    else:
        memo[key] =(calcCroakProbability(N,position-1,croak_string[1:],ps,memo)+
                    calcCroakProbability(N,position+1,croak_string[1:],ps,memo))
        memo[key] /= 2

    memo[key] *= prob_croak_correct
    return memo[key]

def primeFrogProbability(N,croak_string):
    ps = Primes.MakePrimeList(N)
    ans = Fraction(0)
    memo = {}
    for position in range(1,N+1):
        ans += calcCroakProbability(N,position,croak_string,ps,memo)
    return ans / N

if __name__ == '__main__':
    print float(primeFrogProbability(500,'NP'))
    print float(primeFrogProbability(500,'PN'))
    p = primeFrogProbability(500,'PPPPNNPPPNPPNPN')
    print p, float(p)
    print primeFrogProbability(500,'NPNPPNPPPNNPPPP')
    
