# Euler 246

# 810834388

from math import sqrt, cos, pi

def intRoot(n):
    r = int(n**0.5)
    while (r+1)*(r+1) <= n:
        r += 1
    while r*r > n:
        r -= 1
    return r
    
def isSquare(n):
    r = intRoot(n)
    return r*r == n
    
class Euler246:
    def __init__(self):
        self.a2 = 7500*7500
        self.b2 = (15000*15000 - 4*5000*5000) // 4
        
    def solve(self):
        ans = 0
        x = 1
        while self.isInsideEllipse(x,0) or self.tangentsGreaterThan45(x,0):
            if x % 1000 == 0:
                print x, ans
            maxInEllipse = self.findMaxInEllipse(x)
            maxInLocus = self.findMaxInLocus(x, max(0, maxInEllipse))
            ans += 2*maxInLocus
            if maxInEllipse == -1:
                ans += 1
            else:
                ans -= 2*maxInEllipse
            x += 1
            
        ans *= 2
        maxInEllipse = self.findMaxInEllipse(0)
        maxInLocus = self.findMaxInLocus(0, maxInEllipse)
        ans += 2*maxInLocus
        ans -= 2*maxInEllipse
        return ans
    
    def findMaxInEllipse(self, x):
        ybot, ytop = 0,1
        while self.isInsideEllipse(x,ytop):
            ybot, ytop = ytop, 2*ytop
        while ytop - ybot > 1:
            ymid = (ytop +ybot) // 2
            if self.isInsideEllipse(x,ymid):
                ybot = ymid
            else:
                ytop = ymid
        if ybot == 0 and not self.isInsideEllipse(x,0):
            return -1
        else:
            return ybot
            
    def findMaxInLocus(self, x, ybot):
        ytop = ybot+1
        while self.tangentsGreaterThan45(x,ytop):
            ybot, ytop = ytop, 2*ytop
        while ytop - ybot > 1:
            ymid = (ytop +ybot) // 2
            if self.tangentsGreaterThan45(x,ymid):
                ybot = ymid
            else:
                ytop = ymid 
        return ybot       
            
        
    def tangentsGreaterThan45(self, u,v):
        if self.isInsideEllipse(u,v):
            return True
            
        w2 = self.b2*u*u + self.a2*v*v
        p = float(self.a2*self.b2) / w2
        q = sqrt(w2 - self.a2*self.b2) / w2
        
        vector1 = (u*p - self.a2*v*q - u, v*p + self.b2*u*q - v)
        vector2 = (u*p + self.a2*v*q - u, v*p - self.b2*u*q - v)
        
        numerator = vector1[0]*vector2[0] + vector1[1]*vector2[1]
        denominator = (vector1[0]**2 + vector1[1]**2) * (vector2[0]**2 + vector2[1]**2)
        denominator = sqrt(denominator)
        c = numerator / denominator
        return c < cos(pi/4)
            
        
    def isInsideEllipse(self, u, v):
        if self.b2*u*u + self.a2*v*v <= self.a2*self.b2:
            return True
        
if __name__ == '__main__':
    e = Euler246()
    print e.solve()