#! /home/kjb249/Enthought/Canopy_64bit/System/bin/python
import fractions as fr
import scipy as sp

def T(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 10
    # Build recursive list 
    to_calc = [n]
    while to_calc:
        m = to_calc[-1]
        if not m/2 in memo:
            to_calc.append(m/2)
        elif not m/2-1 in memo:
            to_calc.append(m/2-1)
        else:
            if m%2==0:
                memo[m] = (memo[m/2]**2 + memo[m/2-1]**2) % 987898789
            else:
                memo[m] = (memo[m/2]*(memo[m/2]*10 + memo[m/2-1]*2)) % 987898789
            to_calc.pop()
    return memo[n]

def mod_exp_mat(A, e, mod=987898789):
    if e == 1:
        return A
    if e == 0:
        return sp.eye(A.shape())
    X = mod_exp_mat(A, e/2, mod)
    if e%2 == 0:
        ans = X.dot(X)
        ans %= mod
        return ans
    ans = X.dot(X.dot(A))
    ans %= mod
    return ans

def mod_exp(b, e, mod=987898788):
    if e == 1:
        return b % mod
    if e == 0:
        return 1
    x = mod_exp(b, e/2, mod)
    x *= x
    x %= mod
    if e%2==1:
        x *= b
        x %= mod
    return x

def Tca(c, a):
    A = sp.array([[10,1],[1,0]])
    e = mod_exp(c, a)
    A = mod_exp_mat(A, e)
    return A[0,0]
    
def sn_gcd(a,b):
    # gcd(c**a + 1, c**b + 1)
    if a < b:
        a,b = (b,a)
    sn_a = 1
    sn_b = 1
    k = a / b
    r = a % b
    while r > 0:
        a,b = (b,r)
        if sn_a == 1 and sn_b == 1 and k%2 == 1:
            sn_b = -1
        elif sn_a == -1 and sn_b == 1:
            sn_a = 1
            if k%2 == 0:
                sn_b = -1
        else:
            sn_a = -1
            sn_b = 1
        k = a / b
        r = a % b
    if k%2 == 0:
        sn_k = -1
    else:
        sn_k = 1
    if sn_b == -1 or sn_a*sn_k == -1:
        return b, False
    else:
        return b, True

def S(L, memo):
    count_dict = {}
    N = 0
    for a in range(1,L+1):
        for b in range(1, a):
            g, T_bool = sn_gcd(a,b)
            if T_bool:
                if not g in count_dict:
                    count_dict[g] = 0
                count_dict[g] += 1
            else:
                N += 1
    s = 0
    for a in range(1,L+1):
        if a in count_dict:
            mul = 1 + 2*count_dict[a]
        else:
            mul = 1
        s += sum([mul * Tca(c,a) for c in range(1, L+1)])
        s %= 987898789
        print a, s
        
    return (s+ 2*N*((L+1)/2 + 10*(L/2))) % 987898789

memo = {0:1, 1:10}
print S(long(3), memo)

