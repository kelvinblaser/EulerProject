import Primes
import scipy as sp

def Euler122(N):
    primes = Primes.MakePrimeList(N+2)
    m = {}
    m[1] = 0
    for x in range(2, N+1):
        if x in primes:
            #print x, m[x-1]
            m[x] = m[x-1] + 1
        else:
            m[x] = 0
            y = x+0
            for p in primes:
                while y%p == 0 and y > 0:
                    m[x] += m[p]
                    y /= p
    ans = 0
    for x in range(1, N+1):
        ans += m[x]

    print 'Sum: ', ans
    print m
    return ans

class Node:
    def __init__(self, value, level, parent=None):
        self.children = []
        self.level = level
        self.value = value
        self.parent = parent

def solve(cur, m, N):
    if cur.value in m:
        if m[cur.value] > cur.level:
            m[cur.value] = cur.level
    else:
        m[cur.value] = cur.level
        
    if cur.value*2 <= N:
        cur.children.append(Node( cur.value*2, cur.level+1, cur))

    par = cur.parent
    while par != None:
        if cur.value + par.value <= N:
            if cur.value+par.value not in m:
                cur.children.append(Node(cur.value+par.value, cur.level+1, cur))
            elif m[cur.value+par.value] > cur.level:
                cur.children.append(Node(cur.value+par.value, cur.level+1, cur))
        par = par.parent
    for child in cur.children:
        solve(child, m, N)
        
    

def Euler122a(N):
    root = Node(1,0)
    m = {1 : 0}
    solve(root, m, N)
    ans = 0
    for x in range(1, N+1):
        ans += m[x]
    print ans
    return m, ans

def Euler131(N):
    primes = Primes.MakePrimeList(int(sp.sqrt(N))+4)
    x = 1
    p = 3*x*x+3*x+1
    count = 0
    while p <= N:
        if Primes.isPrime(p, primes):
            count += 1
        x += 1
        p = 3*x*x + 3*x + 1
    return count
