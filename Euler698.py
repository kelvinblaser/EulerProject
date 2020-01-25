"""Euler 698 - 123 Numbers"""

from Euler import memoize

SMALL123 = [0,1,2,3,11,12,13,21,22,23,31,32,33,111,112,113,121,122,123,131,132,
133,211,212,213,221,222,223,231,232,233,311,312,313,321,322,323,331,332,333]

class CountError(Exception):
    """Not enough N digit 123 numbers"""

def is123(n):
    s = str(n)
    return (all([s.count(c) in SMALL123 for c in '123'])
             and all([s.count(c) == 0 for c in '0456789']))

@memoize
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

@memoize
def CountNDigit(n, used1=0, used2=0, used3=0):
    ret = 0
    for ones in range(n+1):
        if ones + used1 not in SMALL123: continue
        for twos in range(n - ones + 1):
            if twos + used2 not in SMALL123: continue
            threes = n - ones - twos
            if threes >= 0 and threes + used3 in SMALL123:
                ret += factorial(n) // (factorial(ones) * factorial(twos) *
                                        factorial(threes))
    return ret

@memoize
def MthNDigit(m, n, used1=0, used2=0, used3=0):
    if n == 0:
        used = [used1, used2, used3]
        if m == 1 and all([u in SMALL123 for u in used]):
            return ''
        raise CountError(f'There are fewer than {m} {n}-digit 123 numbers prepended by {used1} ones, {used2} twos, and {used3} threes.')
    m_orig = m
    if CountNDigit(n-1, used1+1, used2, used3) >= m:
        return '1' + MthNDigit(m, n-1, used1+1, used2, used3)
    m -= CountNDigit(n-1, used1+1, used2, used3)
    if CountNDigit(n-1, used1, used2+1, used3) >= m:
        return '2' + MthNDigit(m, n-1, used1, used2+1, used3)
    m -= CountNDigit(n-1, used1, used2+1, used3)
    if CountNDigit(n-1, used1, used2, used3+1) >= m:
        return '3' + MthNDigit(m, n-1, used1, used2, used3+1)
    raise CountError(f'There are fewer than {m_orig} {n}-digit 123 numbers prepended by {used1} ones, {used2} twos, and {used3} threes.')

@memoize
def OneTwoThree(m):
    n = 1
    while CountNDigit(n) < m:
        m -= CountNDigit(n)
        n += 1
    return MthNDigit(m, n)


if __name__ == '__main__':
    for n in range(1,40):
        print(f'CountNDigit({n}) = {CountNDigit(n)}')

    MOD = 123123123
    domain = [1, 2, 3, 4, 10, 40, 1000, 6000, 111_111_111_111_222_333]
    for m in domain:
        s = OneTwoThree(m)
        s_mod = int(s) % MOD
        print(f'F({m}) = {s} = {s_mod} MOD {MOD}')
