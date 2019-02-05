################################################################################
# Euler 507 - Shortest Lattice Vector
# Kelvin Blaser      2015.03.15
#
################################################################################
import scipy as sp

def tribGen(N):
    t, t1, t2 = 1,0,0
    yield 0
    yield 1
    for n in xrange(3,N+1):
        t,t1,t2 = (t+t1+t2)%10000000,t,t1
        yield t

def vecPairGen(N):
    V = sp.zeros(3,dtype=sp.int64)
    W = 0*V
    tGen = tribGen(12*N)
    for _ in xrange(N):
        r = [next(tGen) for n in range(12)]
        V[0] = r[0] - r[1]
        V[1] = r[2] + r[3]
        V[2] = r[4] * r[5]
        W[0] = r[6] - r[7]
        W[1] = r[8] + r[9]
        W[2] = r[10]*r[11]
        yield V,W

def vecMod(WW,V,w,wmv):
    W = 1*WW
    while w > wmv:
        x = min([z for z in W//V if z >= 0])
        W -= x*V
        w,wmv = manhattan(W),manhattan(W-V)
        if w > wmv:
            W -= V
            w,wmv = manhattan(W),manhattan(W-V)
        else:
            break
    return W,w
    

def manhattan(V):
    return abs(V[0])+abs(V[1])+abs(V[2])

def S(V,W):
    w,v,wmv,wpv = manhattan(W),manhattan(V),manhattan(W-V),manhattan(W+V)
    if w < v:
        V,W = W,V
        v,w = w,v
    while (w > wmv or w > wpv):
        if wmv < wpv:
            W,w = vecMod(W,V,w,wmv)
        else:
            W,w = vecMod(W,-V,w,wpv)
        if w < v:
            V,W = W,V
        w,v,wmv,wpv = manhattan(W),manhattan(V),manhattan(W-V),manhattan(W+V)
    return min(w,v)

def SS(N):
    ret = 0
    n = 1
    for V,W in vecPairGen(N):
        if n % 1000 == 0:
            print '%d/%d\t%d'%(n,N,ret)
        ret += long(S(V,W))
        n += 1
    return ret
