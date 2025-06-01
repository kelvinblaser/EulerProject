# Euler 926 - Total Roundness

import collections
from collections.abc import Collection, Mapping

import Primes


MOD = 10**9 + 7
INF = 2**63 - 1

def roundness(n: int, /) -> int:
    """Returns the total roundness of the input - R(n)."""
    r = 0
    for divisor in range(2, n + 1):
        m, pow = n, 0
        while m % divisor == 0:
            m //= divisor
            pow += 1
        r += pow
    return r

def factorial_roundness(n: int, /) -> int:
    """Returns the total roundness of the input factorial - R(n!)."""
    primes = Primes.MakePrimeList(n)
    prime_factorization = _prime_factorization_of_factorial(n, primes)

    factor_roundness: dict[int, Mapping[int, int]] = {}
    for p, exponent in prime_factorization.items():
        factor_roundness[p] = _roundness_for_multiplicity(exponent)
    
    roundness_distribution: Mapping[int, int] = {INF: 1}
    for p in sorted(factor_roundness.keys(), reverse=True):
        roundness_distribution = _convolve_roundness_distributions(factor_roundness[p], roundness_distribution)
    ans = 0
    for r, count in roundness_distribution.items():
        # INF was used for book keeping, but the one value left over should not be counted.
        if r != INF:
            ans += r * count
    return ans % MOD

def _prime_factorization_of_factorial(n: int, /, primes: Collection[int]) -> Mapping[int, int]:
    factors: Mapping[int, int] = collections.defaultdict(int)
    for p in primes:
        prime_power = p
        while prime_power <= n:
            factors[p] += n // prime_power
            prime_power *= p
    return factors

def _roundness_for_multiplicity(exponent: int, /) -> Mapping[int, int]:
    """Returns the distribution of roundness of p^exponent."""
    roundness_dist: dict[int, int] = collections.defaultdict(int)
    roundness_dist[INF] = 1
    # This loop will be slow for large exponents.  Since it is itself called
    # in a loop, this is a candidate for optimization if the program is too slow.
    for power in range(1, exponent + 1):
        roundness_dist[exponent // power] += 1 
    return roundness_dist

def _convolve_roundness_distributions(dist1: Mapping[int, int], dist2: Mapping[int, int], /) -> Mapping[int, int]:
    """Returns the (almost) convolution of two distributions.
    
    In a normal convolution, (key1, key2) contribute to key1 + key2 or key1 - key2.
    For roundness though, (key1, key2) contributes to min(key1, key2).
    """
    # We can use a two pointer approach to do the convolution.
    # For some r1, if we know the sum of the dist2[r2] where r1 <= r2, then
    # we don't have to multiply and add for each r2 >= r1, we can just multiply
    # and add the cumulative value.
    #
    # Likewise for a given r2, we can sum up for all r1 >= r2.
    #
    # So the trick here is to do both of these, and take care that we don't
    # double count when r1 == r2.
    convolved: dict[int, int] = collections.defaultdict(int)
    keys1 = sorted(dist1.keys())
    keys2 = sorted(dist2.keys())
    # The cumulative lists will be indexed parallel to the keys lists.
    cumulative1 = [0] * (len(keys1) + 1)
    for ix, r1 in enumerate(keys1):
        cumulative1[ix+1] = cumulative1[ix] + dist1[r1]
    cumulative2 = [0] * (len(keys2) + 1)
    for ix, r2 in enumerate(keys2):
        cumulative2[ix+1] = cumulative2[ix] + dist2[r2]
    total1 = cumulative1[-1]
    total2 = cumulative2[-1]

    ix1, ix2 = 0, 0
    while ix1 < len(keys1) and ix2 < len(keys2):
        # Process values
        r1, r2 = keys1[ix1], keys2[ix2]
        if r1 <= r2:
            convolved[r1] += dist1[r1] * (total2 - cumulative2[ix2])
        if r1 >= r2:
            convolved[r2] += (total1 - cumulative1[ix1]) * dist2[r2]
        if r1 == r2:
            # Oops, we double counted.
            convolved[r1] -= dist1[r1] * dist2[r2]
        # Update indices
        if r1 <= r2:
            ix1 += 1
        if r1 >= r2:
            ix2 += 1
    for r in convolved.keys():
        convolved[r] %= MOD
    return convolved


if __name__ == '__main__':
    print(f'R(20) = {roundness(20)}')
    print('Prime factorization of 10!:')
    print(f'\t{_prime_factorization_of_factorial(10, [2, 3, 5, 7])}')
    print(f'R(10!) = {factorial_roundness(10)}')
    for n in [10, 100, 1000, 10000]:
        print(f'R({n}!) MOD {MOD} = {factorial_roundness(n)}')
    print(f'R(10,000,000!) MOD {MOD} = {factorial_roundness(10000000)}')