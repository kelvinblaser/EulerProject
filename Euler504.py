################################################################################
# Euler 504 - Square on the Inside
# Kelvin Blaser      2015.02.21
#
################################################################################
import scipy as sp
from fractions import gcd

N = 100
triangle = sp.zeros((N+1,N+1), dtype=int)
g = 0*triangle
for a in range(1,N+1):
    for b in range(1,N+1):
        g[a,b] = gcd(a,b)
        for x in range(a):
            triangle[a,b] -= (b*(x-a))//a

def num_lattice(a,b,c,d):
    ret = triangle[a,b]+triangle[b,c]+triangle[c,d]+triangle[d,a]
    return ret-a-b-c-d+1

def isSquare(l):
    r = int(l**0.5)
    return r*r == l or (r+1)**2 == l

def Euler504(n = N):
    ret = 0
    for a in range(1,n+1):
        print 'a =',a
        for b in range(1,n+1):
            lb = triangle[a,b] + 1 - a - b
            for c in range(1,n+1):
                lc = lb + triangle[b,c] - c
                for d in range(1,n+1):
                    l = lc + triangle[c,d] + triangle[d,a] - d
                    #l = num_lattice(a,b,c,d)
                    if isSquare(l):
                        ret += 1
    return ret

def Euler504a(n=N):
    ret = 0  
    for a in range(1,n+1):
        print 'a =',a
        for b in range(1,n+1):
            #lb = triangle[a,b] + 1 - a - b
            for c in range(1,n+1):
                #lc = lb + triangle[b,c] - c
                for d in range(1,n+1):
                    #l = lc + triangle[c,d] + triangle[d,a] - d
                    #l = num_lattice(a,b,c,d)
                    if isSquare( ((a+c)*(b+d)-g[a,b]-g[b,c]-g[c,d]-g[d,a])/2 + 1 ):
                        ret += 1
    return ret

if __name__ == '__main__':
    print Euler504a()
