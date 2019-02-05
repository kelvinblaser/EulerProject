# Euler 337 - Totiend Stair-step Sequences
# projecteuler.net/problem=337
#
# Kelvin Blaser 2014.02.24
from collections import defaultdict

def seq_calc(n, phi, phi_inv, memo):
    if n in memo:
        return memo[n]
    ans = 1
##    for phi_next in range(n-1, phi[n], -1):
##        try:
##            for x in phi_inv[phi_next][::-1]:
##                if x <= n:
##                    break
##                ans += seq_calc(x, phi, phi_inv, memo)
##                ans %= 10**8
##        except KeyError:
##            continue

    p = n-1
    while p not in phi_inv:
        p -= 1
    x_max = phi_inv[p][-1]
    for x in range(x_max, n, -1):
        if phi[x] <= phi[n] or phi[x] >= n:
            continue
        ans += seq_calc(x, phi, phi_inv, memo) % 10**8
    memo[n] = ans
    if n % 100000 == 0:
        print n, ans
    return ans

def calc_phi_inv(phi):
    phi_inv = {}
    for n, p in enumerate(phi):
        try:
            phi_inv[p].append(n)
        except KeyError:
            phi_inv[p] = [n]
        if n%100000==0:
            print 'Calc Inverse: ', n
    return phi_inv

def calc_phi(N):
    phi = list(range(N+1))
    for i in range(2,N+1):
        if i%1000 == 0:
            print 'Calc Totient: ', i
        if phi[i] != i:
            continue
        # i is prime
        for j in range(1, N/i + 1):
            phi[i*j] *= i-1
            phi[i*j] /= i
    return phi

def Euler337(N):
    # Sieve for totient function
    phi = calc_phi(N)
    #print 'Totients Calculated.'
    
    # Create inverse totient dictionary
    phi_inv = calc_phi_inv(phi)
    #print 'Inverse Dictionary Created'

    # Calculate number of sequences
##    seq = [0] * (N+1)
##    for x in range(N,5,-1):
##        seq[x] = 1
##        if x%1000==0:
##            print 'Calc Seq: ', x
##        for phi_next in range(phi[x]+1, x):
##            try:
##                x_next = phi_inv[phi_next]
##                seq[x] += sum(seq[y] for y in x_next if y > x) % 10**8
##                seq[x] %= 100000000
##            except KeyError:
##                continue
    #print 'Sequences Calculated'
            
    #print phi_inv
    #print phi
    #print seq
    memo = {}
    return seq_calc(6, phi, phi_inv, memo)

if __name__ == '__main__':
    print Euler337(10)
    print Euler337(100)
    print Euler337(1000)
    print Euler337(10000)
    #print Euler337(100000)
    #print Euler337(20000000)

