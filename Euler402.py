# Euler 402
# Kelvin Blaser
def gcd(n1, n2):
    while n2 > 0:
        temp = n2
        n2 = n1 % n2
        n1 = temp
    return n1

def M(a,b,c):
    n = 1
    m = 1+a+b+c
    while n < m:
        n += 1
        m = gcd(m, n**4 + a*n**3 + b*n**2 + c*n)
    return m
