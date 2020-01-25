'''
Project Euler - Problem 412
'''

MOD = 76543217
def LC(m, n):
    num = 1
    for x in range(1, m*m - n*n + 1):
        num *= x
        num %= MOD
    den = 1
    for d in range(1, 2*(m-n)):
        den *= pow(d+2*n, min(d, 2*(m-n)-d, m-n), MOD)

    for d in range(1, m):
        den *= pow(d, 2 * min(d, m-d, m-n, n), MOD)
        den %= MOD

    return (num * pow(den, MOD-2, MOD)) % MOD

if __name__ == '__main__':
    fmt_str = 'LC{} = {}'
    cases = [(3, 0), (5, 3), (6, 3), (10, 5), (10000, 5000)]
    for m, n in cases:
        print(fmt_str.format((m, n), LC(m, n)))
