# Euler 149 Maximum-sum subsequence
# Kelvin Blaser
import scipy as sp

def create_table():
    vec = []
    for k in range(1,56):
        vec.append((100003 - 200003*k + 300007*k*k)%1000000 - 500000)
    for k in range(56, 4000001):
        vec.append((vec[k-24] + vec[k-55] + 1000000)%1000000 - 500000)
    return sp.array(vec), sp.resize(vec, (2000,2000))

def max_sum(vec):
    maxx = -1000000
    l = len(vec)
    ix = 0
    while ix < l:
        summ = 0
        for jx in range(ix,l):
            summ += long(vec[jx])
            if summ > maxx:
                maxx = summ
            if summ < 0:
                ix = jx
                break
        ix += 1
    return maxx

def Euler149():
    v, t = create_table()
    maxx = -1000000
    # Check rows and columns
    for i in range(2000):
        n = max_sum(t[i,:])
        m = max_sum(t[:,i])
        if n > maxx:
            maxx = n
        if m > maxx:
            maxx = m
    for i in range(2000):
        n = max_sum(v[i:2000*(2000-i):2001])
        m = max_sum(v[i:2000*i+1:1999])
        p = max_sum(v[2000*i::2001])
        q = max_sum(v[2000*i+1999::1999])
        if n > maxx:
            maxx = n
        if m > maxx:
            maxx = m
        if p > maxx:
            maxx = p
        if q > maxx:
            maxx = q
    return maxx
            
