# Euler 160 - Factorial Trailing Digits
from scipy import log

def modexp(b, e, m):
    if e==0:
        return 1
    if e==1:
        return b % m
    x = modexp(b, e/2, m)
    if e%2 == 1:
        return (x*x*b) % m
    return (x*x) % m

def p_in_factorial(N,p):
    q = p
    factors = 0
    while q <= N:
        factors += N / q
        q *= p
    return factors

N = 20
n = 2  # Last n digits
ten_n = 10**n

x = 3
F = 1
while x < min(N, ten_n):
    if x%5 == 0:
        x += 2
    num_xs = 0
    for i in range(int(log(N/x)/log(5))+1):
        num_xs += int(log((N/x)/(5**i)) / log(2)) +1
    F *= modexp(x, num_xs, ten_n)
    F %= ten_n
    x += 2

num_twos  = p_in_factorial(N,2)
num_fives = p_in_factorial(N,5)

F *= modexp(2, num_twos - num_fives, ten_n)
F %= ten_n

print F
