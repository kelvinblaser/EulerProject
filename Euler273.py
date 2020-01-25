""" Euler 273

2032447591196869022
35255681025958902285
"""

from Primes import MakePrimeList

def get_primes():
    return [p for p in MakePrimeList(150) if p % 4 == 1]

def square_sums(primes):
    return [square_sum(p) for p in primes]

def square_sum(p):
    for x in range(1, p):
        r = int_root(p - x * x)
        if x * x + r * r == p:
            return (min(x, r), max(x, r))

def int_root(n):
    r = int(n**0.5)
    while (r+1) * (r+1) <= n:
        r += 1
    return r

def square_sum_gen(prime_squares, index=None):
    if index == -1:
        yield [(0, 1)]
        return
    if index is None:
        index = len(prime_squares) - 1
    for square_sums in square_sum_gen(prime_squares, index - 1):
        yield square_sums
        new_square_sums = set()
        for a1, b1 in square_sums:
            for a, b in compose_squares((a1, b1), prime_squares[index]):
                new_square_sums.add((min(a,b), max(a,b)))
        yield new_square_sums

def compose_squares(s1, s2):
    a, b = s1
    c, d = s2
    yield (a*c + b*d, abs(a*d - b*c))
    yield (a*d + b*c, abs(a*c - b*d))


def Euler273():
    ans = 0
    ss = square_sums(get_primes())
    count = 0
    for s in square_sum_gen(ss):
        for a, b in s:
            ans += a
            count += 1
            if count % 1000000 == 0:
                print(f'After {count} values: {ans}')
    return ans

if __name__ == '__main__':
    print(f'Sum of Squares: {Euler273()}')
