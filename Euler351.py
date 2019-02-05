# Euler 351 - Hexagonal Orchards
# projecteuler.net/problem=351
# Kelvin Blaser   2014.11.21

from scipy import prod
import Primes

def combProdLessThan(iterable, r, N):
    '''Yields all combinations of r elements from list l whose product is
    less than or equal to N.

    INPUT:
        iterable - list of numerical elements, needs to be sorted.
        r - number of elements to choose from
        N - maximum product

    YIELD:
        combinations as a tuple
    '''
    count = 0
    pool = tuple(iterable)
    n = len(pool)
    if r > n:   # No combinations with r > n
        return

    indices = list(range(r))  # Set up the list of indicies
    if prod(tuple(pool[i] for i in indices)) <= N:
        yield tuple(pool[i] for i in indices)
    else:
        return

    while True:
        for i in reversed(range(r)):
            if indices[i] != i+n-r:  # Not done condition
                break
        else:   # Done
            return
        n = len(pool)  # If pool was reduced, return it to full size
        indices[i] += 1  # i is now the active pointer
        for j in range(i+1,r):
            indices[j] = indices[j-1]+1
        c = tuple(pool[k] for k in indices)
        if prod(c) <= N:
            yield tuple(pool[i] for i in indices)
        else:   # If product too large, temporarily reduce the pool
            n = indices[i]+r-i

def Euler351(N):
    M = N/2
    primes = Primes.MakePrimeList(M)
    ans = 0
    r = 1
    while r < len(primes) and prod(primes[:r]) <= M:
        sign = int((-1)**(r+1))
        count = 0
        for c in combProdLessThan(primes, r, M):
            count += 1
            x = prod(c)
            p = int(N//x)
            q = int(N//(2*x))
            ans += sign * (p*q - q*(q+1))
        print '%d from list of len %d: %d times; \ttotal %d'%(r,len(primes),
                                                            count, ans)
        r += 1
    return 6*(2*ans + M + N - 2)

def Euler351a(N):
    phi = range(N+1)
    for x in range(2,N+1):
        if phi[x] == x-1:
            for y in range(x,N+1,x):
                phi[y] *= x-1
                phi[y] /= x

    return 6*((N*N+N)/2 + sum(phi[1:]))

if __name__ == '__main__':
    print Euler351a(5)
    print Euler351a(10)
    print Euler351a(1000)
    #print Euler351a(10**8)
