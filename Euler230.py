# Euler 230 - Fibonacci Words
# Kelvin Blaser     2013-10-19

def D(A, B, n, G=[]):
    # G is the list of lengths of the strings (fibonacci x 100)
    if len(G) < 2:
        G = [len(A), len(B)]
    if G[-1] >= n:
        ix = len(G) - 1
        while G[ix-1] >= n and ix >= 1:
            ix -= 1
        if ix == 1:
            return d(A, B, n, 0, G)
        else:
            return d(A, B, n, ix, G)
    while G[-1] < n:
        G.append(G[-2] + G[-1])
    return d(A, B, n, len(G)-1, G)

def d(A, B, n, m, G):
    if m == 0:
        return A[n-1]
    if m == 1:
        return B[n-1]
    if n > G[m-2]:
        return d(A, B, n-G[m-2], m-1, G)
    return d(A, B, n, m-2, G)
    

A = '14159265358979323846264338327950288419716939937510'+ \
    '58209749445923078164062862089986280348253421170679'

B = '82148086513282306647093844609550582231725359408128'+ \
    '48111745028410270193852110555964462294895493038196'

s = ''
G = [len(A), len(B)]
for n in range(18):
    s = D(A, B, (127 + 19*n)*7**n, G) + s
    print s
print s

    
