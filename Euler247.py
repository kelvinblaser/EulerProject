################################################################################
# Euler 247 - Squares Under a Hyperbola
# Kelvin Blaser      2015.03.16
#
################################################################################
from Queue import PriorityQueue
class Gap:
    def __init__(self,key):
        x,y,left,bottom = key
        self.x = x
        self.y = y
        self.a = (-(x+y)+((x-y)**2+4)**(0.5))/2.0
        self.left = left
        self.bottom = bottom

    def key(self):
        return (self.x,self.y,self.left,self.bottom)

def aa(x,y):
    return (2.0-2.0*x*y) / (x+y+((x-y)**2+4)**0.5)

def Euler247():
    q = PriorityQueue()
    q.put((1.0-aa(1.0,0.0),(1.0,0.0,0,0)))
    c = 1
    n = 0
    ret = 0
    while c > 0:
        a,key = q.get()
        n += 1
        x,y,left,bottom = key
        if left == 3 and bottom == 3:
            print n,x,y
            ret = n
        if left <= 3 and bottom <= 3:
            c -= 1
        a = aa(x,y)
        ra = aa(x+a,y)
        ta = aa(x,y+a)
        q.put((1-ra,(x+a,y,left+1,bottom)))
        if left+1 <= 3 and bottom <= 3:
            c += 1
        q.put((1-ta,(x,y+a,left,bottom+1)))
        if left <= 3 and bottom+1 <= 3:
            c += 1
    return ret
