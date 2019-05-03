# Euler 571
import itertools

def super_pandigitals(bMax):
    for p in pandigitals(bMax):
        if all([is_pandigital(p, b) for b in range(2, bMax)]):
            yield p

def pandigitals(b):
    for perm in itertools.permutations(range(b), b):
        if perm[-1] != 0:
            yield pandigital_from_digit_list(perm, b)

def pandigital_from_digit_list(digit_list, b):
    return sum(d * b**n for n,d in enumerate(digit_list))

def is_pandigital(n, b):
    digits = [False] * b
    while n > 0:
        digits[n%b] = True
        n //= b
    return all(digits)


if __name__ == '__main__':
    # is_pandigital tests
    ip_str = '{0} is pandigital base {1} : {2}'
    print(ip_str.format(4, 2, is_pandigital(4, 2)), bin(4)) # True
    print(ip_str.format(7, 2, is_pandigital(7, 2)), bin(7)) # False
    n = 0o10234567
    print(ip_str.format(n, 8, is_pandigital(n, 8)), oct(n)) # True
    n = 0o11234567
    print(ip_str.format(n, 8, is_pandigital(n, 8)), oct(n)) # False
    print(ip_str.format(1023456789, 10, is_pandigital(1023456789, 10))) # True
    print(ip_str.format(1123456789, 10, is_pandigital(1123456789, 10))) # False
    n = 0x1023456789abcdef
    print(ip_str.format(n, 16, is_pandigital(n, 16)), hex(n)) # True
    n = 0x1123456789abcdef
    print(ip_str.format(n, 16, is_pandigital(n, 16)), hex(n)) # False
    print(ip_str.format(0, 10, is_pandigital(0, 10))) # False
