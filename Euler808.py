"""Euler 808 - Reversible Prime Squares
"""

import Primes

class NotEnoughPrimesError(Exception):
    def __init__(self, n: int, max_prime: int, rps_count: int):
        super().__init__(f'Not enough primes less than {max_prime} to find {n} reversible prime squares.  Found {rps_count}.' )

def reverse(n: int, /) -> int:
    r = 0
    while n:
        r *= 10
        r += n % 10
        n //= 10
    return r

def euler808(n: int, *, max_prime: int = 10**6) -> int:
    """max_prime must be a power of 10.  Otherwise, we might miss a smaller
    prime square's reverse."""
    primes = Primes.MakePrimeList(max_prime)  # Hopefully that's enough primes?
    prime_squares = set(p * p for p in primes)
    rps_count, rps_sum = 0, 0
    for p in primes:
        p2 = p * p
        r = reverse(p2)
        if r in prime_squares and r != p2:
            print(f'{p}: {p2}')
            rps_count += 1
            rps_sum += p2
            if rps_count == n:
                return rps_sum
    raise NotEnoughPrimesError(n, max_prime, rps_count)

if __name__ == '__main__':
    s = euler808(50, max_prime=10**8)
    print(s)