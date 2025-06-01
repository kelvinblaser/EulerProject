"""Euler 944 - Sum of Elevisors

S(n) = sum(x in subsets(E(n)), sev(x))
     = sum(k in 1..n, k * "Number of subsets that contain k and at least one other multiple of k")
     = sum(k in 1..n, k * (2^n - 2^(n-1) - 2^(n - n//k)))
     = sum(k in 1..n, k * (2^(n-1) - 2^(n - n//k)))

T(n) = n * (n + 1) / 2 - The nth triangle number

S(n) = T(n) * 2^(n-1) - sum(k in 1..n, k * 2^(n - n//k)) = T(n) * 2^(n - 1) - Q(n)

Let r = floor(sqrt(n))
Q(n) = sum(k in 1..r, k * 2^(n - n//k)) + sum(k in r+1..n, k * 2^(n - n//k)) = R(n) + P(n)

R(n) is straight forward.  We can just do the sum directly.  The sum in P(n) has too many terms,
but we can group them into groups with the same value of n//k.

P(n) = sum(j in 1..r, sum(k in lj..hj, k * 2^(n - j)))
     = sum(j in 1..r, 2^(n-j) * sum(k in lj..hj, k))
     = sum(j in 1..r, 2^(n-j) * T(hj) - T(lj - 1))

lj = max(r+1, n//(j+1) + 1) = max(r, n//(j+1)) + 1
hj = n//j

P(n) = sum(j in 1..r, 2^(n-j)  * (T(n//j) - T(max(r, n//(j+1)))))

"""
from typing import Any
MOD = 1234567891
verbose: bool = False

def print_v(*args: Any):
    """Prints only if verbose global is set to True."""
    if verbose:
        print(*args)


def triangle(n: int) -> int:
    """Returns the nth triangle number: n * (n + 1) / 2."""
    return n * (n + 1) // 2

def _q_sum(n: int) -> int:
    """Returns the sum Q(n) as defined above."""
    print_v(f'Calculating Q({n})...')
    return _r_partial_sum(n) + _p_partial_sum(n)
    
def _r_partial_sum(n: int) -> int:
    """Returns the sum R(n) as defined above."""
    print_v(f'Calculating R({n})...')
    r = sqrt_int(n)
    s = 0
    for k in range(1, r + 1):
        s += k * pow(2, n - n//k, MOD)
    return s

def _p_partial_sum(n: int) -> int:
    """Returns the sum P(n) as defined above."""
    print_v(f'Calculating P({n})...')
    r = sqrt_int(n)
    s = 0
    for j in range(1, r + 1):
        l = max(r, n//(j + 1))
        h = n // j
        s += pow(2, n-j, MOD) * (triangle(h) - triangle(l))
    return s

def sqrt_int(n: int) -> int:
    """Returns the square root of n truncated down to the nearest integer."""
    r = int(n**0.5)
    while (r + 1) * (r + 1) < n:
        r += 1
    while r * r > n:
        r -= 1
    return r

def S(n: int) -> int:  # pylint: disable=invalid-name
    """Returns the sum of the elevisors of all subsets of {1, 2, 3, ... n}."""
    print_v(f'Calculating S({n})...')
    s = triangle(n) * pow(2, n - 1, MOD)
    return (s - _q_sum(n)) % MOD

def main():
    global verbose
    for N, Nstr, v in [(10, '10', False), (10**14, '10^14', True)]:
        verbose = v
        print(f'S({Nstr}) = {S(N)}')

if __name__ == '__main__':
    main()
