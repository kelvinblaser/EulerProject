# Euler 474
#
# Dynamic programming solution.
#
# Using F(12!, 12) as an example.  We care about the divisors modulo 100 in this
# case because 12 is a two digit number.
# 
# First note that 12! = 2^10 x 3^5 x 5^2 x 7 x 11.  The prime factorization of 
# a factorial is easily calculated given a list of primes up to that factorial's
# base.
#
# We start to build all possible factors 1 prime at a time.  The base case is
# no primes.  The only factor with no primes is 1.  Let 'factors' be a vector
# that counts the number of factors.  I.e. factors[i] is the number of factors
# of 12! that whose last two digits are i.
#
# To begin, factors = [0, 1, 0, .... 0] with 100 possible values
# Now we have 11 possible powers of 2: 2^0, 2^1, 2^2, ... 2^10 =
#    1,2,4,8,16,32,64,128, ... 1024 = 1,2,4,8,32,64,28, ... 24 mod 100
#
# Thus we create a new factors vector by adding factors[i] to 
# newFactors[(i*pp)%10] for each prime power (pp) and for each i.  Do this for
# each prime and you have a solution

from Primes import MakePrimeList

def F(n, d):
    MOD = 10**16+61
    # Count digits
    numDigs = 0
    dd = d # have to preserve d
    while dd > 0:
        numDigs += 1
        dd //= 10
    
    # Set up dynamic programming
    pow10 = 10**numDigs
    if d == 0: pow10 = 10
    factors = [0]*pow10
    factors[1] = 1
    primes = MakePrimeList(n)
    
    # Dynamic programing loop
    pLast = 1
    for p in primes:
        if p//10000 > pLast//10000:
            print p, factors[:10]
        print p,
        newFactors = [0]*pow10
        exponent = 0
        pp = p
        while pp <= n:
            exponent += n//pp
            pp *= p
        # Exponent is ~10^6 for p=2
        # Need to decouple the exponent loop from the factor loop
        ppCount = [0]*pow10
        for e in range(exponent+1):
            ppCount[pow(p,e,pow10)] += 1
        print ppCount[:10],
        nulls = 0
        for pp in range(pow10):
            if ppCount[pp] == 0: 
                nulls += 1
                continue
            for i in range(pow10):
                newFactors[(i*pp)%pow10] += ppCount[pp]*factors[i]
        print pow10-nulls
        factors = newFactors
        for i in range(pow10):
            factors[i] %= MOD
        pLast = p
        
    return factors[d]
    
if __name__ == '__main__':
    print 'F(12!, 12) = {0}'.format(F(12,12))
    print 'F(50!, 123) = {0}'.format(F(50, 123))
    print 'F(10^6!, 65432) = {0}'.format(F(10**6, 65432))