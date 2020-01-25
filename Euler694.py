"""Euler 694: Cubefull Divisors"""

from Euler import restrictedPrimeFactorizations

def IntCubeRoot(n):
    r = int(n**(1.0 / 3))
    while (r+1)**3 <= n:
        r += 1
    while r**3 > n:
        r -= 1
    return r


def IntSquareRoot(n):
    r = int(n**0.5)
    while (r+1)**2 <= n:
        r += 1
    while r**2 > n:
        r -= 1
    return r


def BaseSquareFree(n):
    root = IntCubeRoot(n)
    is_square_free = [True] * (root + 1)
    is_square_free[0] = False
    prime_divisors = [[] for _ in range(root+1)]
    for p in range(2, root + 1):
        if prime_divisors[p]: continue
        for x in range(p, root+1, p):
            prime_divisors[x].append(p)
        for x in range(p*p, root+1, p*p):
            is_square_free[x] = False
    return {x: prime_divisors[x] for x in range(root+1) if is_square_free[x]}

def Euler694(N):
    ret = 0
    for base, primes in BaseSquareFree(N).items():
        #print('--', base, primes)
        for x in restrictedPrimeFactorizations(primes, N // base**3 + 1):
            #print(x, base**3 * x, N // (base**3 * x))
            ret += N // (base**3 * x)
    return ret

if __name__ == '__main__':
    print(BaseSquareFree(20**3))
    print(Euler694(16))
    print(Euler694(100))
    print(Euler694(10000))
    print(Euler694(10**18))
