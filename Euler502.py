# Euler 502
import numpy as np
MOD = 100000

def F1(w,h):
    return e(w,h) - e(w,h-1)

def e(w,h):
    E = np.zeros(h, dtype=np.int64)
    O = np.zeros(h, dtype=np.int64)
    for i in range(h):
        if (h-i)%2 == 0:
            E[i] = 1
        else:
            O[i] = 1

    for x in xrange(w-1):
        Enext = 0*E
        Onext = 0*O
        for i in range(h):
            Enext[i] = E[:i+1].sum()
            Onext[i] = O[:i+1].sum()
            for j in range(i+1,h,2):
                Enext[i] += O[j]
                Onext[i] += E[j]
            for j in range(i+2,h,2):
                Enext[i] += E[j]
                Onext[j] += O[j]
        print Enext
        E = Enext 
        O = Onext
    print ''
    return E.sum()

def parity(n):
    b = 0
    while n > 0:
        if n%2 == 0:
            while n%2==0:
                n/=2
        else:
            b += 1
            while n%2 ==1 :
                n/=2
    return b%2

def F2(w,h):  # Works for w <= 13
    E = np.zeros(2**w, dtype = np.int64)
    O = 0*E
    O[-1] = 1
    
    for x in xrange(h-1):
        for n in xrange(2**w):
            p = parity(n)
            if p == 1:
                E[n],O[n] = O[n],E[n]
                for m in xrange(n+1,2**w):
                    if n & m == n:
                        E[n] += O[m]
                        O[n] += E[m]
            else:
                for m in xrange(n+1,2**w):
                    if n & m == n:
                        E[n] += E[m]
                        O[n] += O[m]
        #print E,O

    return sum(E) - E[0]

def F3(w,h):  # Works for w <= 4
    co = [[2**w-1]]
    for x in xrange(h-1):
        cn = []
        for c in co:
            for m in xrange(2**w):
                if m&c[-1] == m:
                    cn.append(c+[m])
        co = cn
    return [c for c in co if sum(parity(n) for n in c)%2 == 0 and c[-1] != 0]

def F4(w,h):
    E = np.zeros(w+1, dtype = np.int64)
    O = np.zeros(w+1, dtype = np.int64)
    E[0] = 1
    O[1] = 1
    for ww in xrange(2,w+1):
        for g in xrange(ww):
            for l in xrange(1,ww-g):
                O[ww] += E[ww-g-l-1]
                E[ww] += O[ww-g-l-1]
            O[ww] += 1
        E[ww] += 1
    print E,O
    for x in xrange(h-1):
        En = 0*E
        On = 0*O
        En[0] = 1
        if x%2 == 0:
            En[1] = 1
        else:
            On[1] = 1
        for ww in xrange(2,w+1):
            for g in xrange(ww):
                for l in xrange(1,ww-g):
                    On[ww] += E[l]*En[ww-l-g-1] + O[l]*On[ww-l-g-1]
                    En[ww] += O[l]*En[ww-l-g-1] + E[l]*On[ww-l-g-1]
                On[ww] += E[ww-g]
                En[ww] += O[ww-g]
        E = En
        O = On
        print E,O
    return O[w]

