#---------------------------------------------------------------
#  Divisibility Multipliers
#
#  Key observation - 
#       m must preserve divisibility by p under f(n).
#       In particular it must preserve divisibility of f(4p)
#       I use 4p instead of p to ensure that there are at least
#       two digits in the the argument of f() [Cases p = 3, 7]
#       This ensures that there is only one solution for m
#
#  Observation from others
#       m = 10^-1 mod p  (Avoids the 4p trick and is a little more elegant)
#---------------------------------------------------------------
from Primes import MakePrimeList

def divisibilityMultiplier(p):
    # Precondition - p must be prime
    x = (4*p)//10
    y = (4*p)%10
    return (pow(y, p-2, p)*(p-x))%p
#    return pow(10, p-2, p) # Alternative method
    
def Euler274(N):
    # Sum of divisibility multipliers for all primes less than
    # N and coprime to 10
    primes = MakePrimeList(N)
    primes = primes[1:2] + primes[3:] # remove 2 and 5
    return sum(divisibilityMultiplier(p) for p in primes)
    
if __name__ == '__main__':
    fmtstr = 'Sum of divisibility multipliers for primes less than {0} is {1}'
    print fmtstr.format('1000', Euler274(1000))
    print fmtstr.format('10^7', Euler274(10**7))