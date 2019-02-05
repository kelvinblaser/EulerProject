################################################################################
# Euler 508 - Integers in Base i-1
# Kelvin Blaser      2015.03.25
#
################################################################################

def square(a0,b0,a1,b1,memo):
    if (a0,b0,a1,b1) == (0,0,0,0):
        return 0
    key = (a0,b0,a1,b1,'s')
    try:
        return memo[key]
    except KeyError:
        pass

    if a0 == a1:
        ret = 0
        for b in xrange(b0,b1+1):
            ret += f(a1,b)
        memo[key] = ret
        return ret
    if b0 == b1:
        ret = 0
        for a in xrange(a0,a1+1):
            ret += f(a,b1)
        memo[key] = ret
        return ret
    a = a1-a0+1
    b = b1-b0+1
    memo[key] = ((a*b+(a0+b0)%2)//2 + diamond(b1-a1,-b1-a1,b0-a0,-b0-a0,memo) +
                 diamond(b1-a1+1,-b1-a1+1,b0-a0+1,-b0-a0+1,memo))
    return memo[key]

def diamond(a0,b0,a1,b1,memo):
    key = (a0,b0,a1,b1,'d')
    try:
        return memo[key]
    except KeyError:
        pass

    if a0%2 == 0:
        A0,B0 = a0/2,b0/2
        if (A0+B0)%2 == 0:
            A0,B0 = A0,B0+1
    else:
        A0,B0 = (a0+1)/2,(b0+1)/2
        if (A0+B0)%2 == 0:
            A0,B0 = A0-1,B0

    A1,B1 = a1/2,b1/2
    if a1%2 == 0:
        if (A1+B1)%2 == 0:
            A1,B1 = A1,B1-1
    else:
        if (A1+B1)%2 == 0:
            A1,B1 = A1+1,B1

    l = (A0-A1-B0+B1)/2 + 1
    w = (A1+B1-A0-B0)/2 + 1
    
    memo[key] = (l*w +
                 square((b0-a0+3)//4,
                        (-b1-a1+3)//4,
                        (b1-a1)//4,
                        (-b0-a0)//4, memo) +
                 square((b0-a0+5)//4,
                        (-b1-a1+5)//4,
                        (b1-a1+2)//4,
                        (-b0-a0+2)//4, memo))
    return memo[key]

def div2zero(a,b):
    return -(-a//b) if (a<0) ^ (b<0) else a//b

def B(L,memo={}):
    return square(-L,-L,L,L,memo)

def f(a,b):
    if a==0 and b==0:
        return 0
    return (a+b)%2 + f((b-a+1)//2,-((b+a)//2))

def Balt(L):
    ret = 0
    for a in xrange(-L,L+1):
        for b in xrange(-L,L+1):
            ret += f(a,b)
    return ret
