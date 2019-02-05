# Approximate the area as a triangle, makes a simple expression for the
# area.  Good for large n.
from numpy import pi, arccos, arctan, sqrt

def pA(n):
    Ax = (sqrt(2*n)*(n-1) + 2) / (2*(1+n*n))
    Awedge = (arccos((n-1.0)/sqrt(n*n+1)) - arctan(1.0/n)) / 2.0
    A = Ax - Awedge
    return A / (1-pi/4)
    
def Euler587():
    f = 0.001
    top = 128
    bot = 0
    while pA(top) > f: top *= 2
    while top - bot > 1:
        mid = (top + bot)//2
        if pA(mid) < f:
            top = mid
        else:
            bot = mid
    print top
    
if __name__ == '__main__':
    Euler587()