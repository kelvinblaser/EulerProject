#--------------------------------------------
#   Euler 366
#   12-13-2017
#--------------------------------------------

def nthLosingPosition(n):
    return 2 + n*(n+1)/2
    
def nearestLosingPosition(n):
    r = int(((8*n-15)**0.5 - 1) / 2)
    while nthLosingPosition(r+1) <= n:
        r += 1
    return r
    
#def Euler366(n):
#    j = nearestLosingPosition(n)
#    Kj = nthLosingPosition(j)
#    d = n - Kj
#    return j*(j-1)*(j+1) // 6 + d*(d+1) // 2    

def losingPositions(n):
    lps = [2]
    while lps[-1] <= n:
        lp = lps[-1]
        if lp % 2 == 0:
            lps.append(3*(lp//2))
        else:
            lps.append(3*((lp-1)//2) + 2)
    return lps
    
def differences(lps):
    diffs = []
    for i in range(len(lps)-1):
        diffs.append(lps[i+1] - lps[i] - 1)
    return diffs
    
def T(n):
    return n*(n+1)//2
    
def Euler366(n):
    lps = losingPositions(n)
    diffs = differences(lps)
    return sum(T(j) for j in diffs)
    