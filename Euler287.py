###############################################################################
# Euler 287 - Quadtree Encoding
# Kelvin Blaser         2015.4.3
#
###############################################################################

def allBlack(xmin,ymin,xmax,ymax,N):
    points = [(xmin,ymin),(xmin,ymax),(xmax,ymin),(xmax,ymax),
              ((xmin+xmax)/2,(ymin+ymax)/2)]
    m = 2**(N-1)
    R2 = 2**(2*N-2)
    for x,y in points:
        if (x-m)**2 + (y-m)**2 > R2:
            return False
    return True

def allWhite(xmin,ymin,xmax,ymax,N):
    points = [(xmin,ymin),(xmin,ymax),(xmax,ymin),(xmax,ymax),
              ((xmin+xmax)/2,(ymin+ymax)/2)]
    m = 2**(N-1)
    R2 = 2**(2*N-2)
    for x,y in points:
        if (x-m)**2 + (y-m)**2 <= R2:
            return False
    return True

def squareSeq(xmin,ymin,xmax,ymax,N):
    if xmax - xmin > 2**(N-5):
        print xmax - xmin
    if allBlack(xmin,ymin,xmax,ymax,N):
        return 2
    if allWhite(xmin,ymin,xmax,ymax,N):
        return 2
    xmid = (xmin+xmax)/2
    ymid = (ymin+ymax)/2
    return (1 +
            squareSeq(xmin,ymid+1,xmid,ymax,N) +
            squareSeq(xmid+1,ymid+1,xmax,ymax,N) +
            squareSeq(xmin,ymin,xmid,ymid,N) +
            squareSeq(xmid+1,ymin,xmax,ymid,N) )

def Euler287(N):
    s = squareSeq(0,0,2**N-1,2**N-1,N)
    return s

if __name__ == '__main__':
    print Euler287(5)
