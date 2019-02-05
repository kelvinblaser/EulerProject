################################################################################
# Euler 284 - Steady Squares
# Kelvin Blaser      2015.03.15
#
################################################################################

def baseBrep(n,b):
    '''Gives the representation of integer n in base b with b <= 36'''
    digs = '0123456789abcdefghijklmnopqrstuvwxyz'
    if n == 0:
        return '0'
    if n < 0:
        n = -n
        sign = '-'
    else:
        sign = ''

    s = ''
    while n > 0:
        s = digs[n%b] + s
        n /= b
    return sign+s

def sumDigsB(n,b):
    ''' Sum of the digits of n in base b '''
    s = 0
    while n > 0:
        s += n%b
        n /= b
    return s

def steadySquares(N,b):
    steadies = [[0]]
    for n in xrange(1,N+1):
        new_steadies = []
        for x in steadies[-1]:
            for d in range(b):
                z = d*b**(n-1) + x
                if (z*z)%(b**n) == z:
                    new_steadies.append(z)
        steadies.append(new_steadies)
    for n in xrange(1,N+1):
        z = b**(n-1)
        steadies[n] = [x for x in steadies[n] if x >= z]
    s = 0
    for d in steadies:
        for x in d:
            #print baseBrep(x,b)
            s += sumDigsB(x,b)
    return baseBrep(s,b)
