# Euler 177 - Integer Angled Quadrilaterals
# projecteuler.net/problem=177
# Kelvin Blaser     2014.11.21

from scipy import cos, sin, arccos, pi,sqrt
import pylab as pl
d2r = pi / 180
r2d = 180 / pi

SIN = [sin(x*d2r) for x in range(181)]

def plot_segment(A,B,c):
    pl.plot([A[0],B[0]],[A[1],B[1]],c)

def plot_triangle(t,c1='k',c2='r',down=False):
    a,b,c,Bx,By
    if down:
        By = -By
    A = [0,0]
    B = [Bx,By]
    C = [1,0]
    plot_segment(A,B,c1)
    plot_segment(A,C,'--'+c2)
    plot_segment(B,C,c1)

def plot_quad(q, col1='k', col2='r'):
    at,bt,ct,dt = q
    a,a1,a2 = at
    b,b1,b2 = bt
    c,c1,c2 = ct
    d,d1,d2 = dt
    r1 = SIN[c2]/SIN[b]
    r2 = SIN[c1]/SIN[d]
    A = [0,0]
    B = [r1*cos(a1*d2r), r1*sin(a1*d2r)]
    C = [1,0]
    D = [r2*cos(a2*d2r), r2*sin(a2*d2r)]
    plot_segment(A,B,col1)
    plot_segment(A,C,'--'+col2)
    plot_segment(A,D,col1)
    plot_segment(B,C,col1)
    plot_segment(B,D,'--'+col2)
    plot_segment(C,D,col1)
    
def make_triangles():
    tris = []
    for a1 in range(1,178):
        for b in range(2,180-a1):
            c2 = 180 - a1 - b
            r = SIN[c2] / SIN[b]
            tris.append((a1,b,c2,r*cos(a1*d2r),r*SIN[a1]))
    return tris

def rotate_quad(q,n):
    a,b,c,d = q
    if n == 1:
        return b,c,d,a
    if n == 2:
        return c,d,a,b
    if n == 3:
        return d,a,b,c
    return q

def flip_quad(q):
    at,bt,ct,dt = q
    a,a1,a2 = at
    b,b1,b2 = bt
    c,c1,c2 = ct
    d,d1,d2 = dt
    at = (a,a2,a1)
    bt = (d,d2,d1)
    ct = (c,c2,c1)    
    dt = (b,b2,b1)
    return at,bt,ct,dt

def fix_quad(q):
    f = flip_quad(q)
    reps = [rotate_quad(q,x) for x in range(4)]+[rotate_quad(f,x) for x in range(4)]
    return min(reps)

def Euler177():
    tris = make_triangles()
    v_dict = {}
    quads = set()
    for n,t in enumerate(tris):
        a,b,c,Bx,By = t
        r = SIN[c]/SIN[b]
        if n%1000==0:
            print 'Calculating Values: %d of %d'%(n,len(tris))
        for b2 in range(1,b):
            v = round(r*SIN[b2],9)
            try:
                v_dict[v].append(n)
            except KeyError:
                v_dict[v] = [n]
                
    for n,v in enumerate(v_dict):
        if n%1000 == 0:
            print 'Calculating Matches: %d of %d \t%d Quads found'%(n,len(v_dict),len(quads))
        for m,n1 in enumerate(v_dict[v]):
            a1,b,c2,Bx,By = tris[n1]
            for n2 in v_dict[v][m:]:
                a2,d,c1,Dx,Dy = tris[n2]
                a = a1+a2
                c = c1+c2
                if a > 179 or c > 179:
                    continue
                diffx = Bx-Dx
                diffy = By+Dy
                b2 = arccos((Bx*diffx+By*diffy)/
                        sqrt((Bx*Bx+By*By)*(diffx*diffx+diffy*diffy))) * r2d
                if b2 <= 0 or int(b2) >= b:
                    continue
                if abs(round(b2)-b2) < 1e-9:
                    b2 = int(b2+0.1)
                    b1 = b-b2
                    d1 = 180 - a - b2
                    d2 = d - d1
                    at = (a,a1,a2)
                    bt = (b,b1,b2)
                    ct = (c,c1,c2)
                    dt = (d,d1,d2)
                    quads.add(fix_quad((at,bt,ct,dt)))
    return quads

if __name__ == '__main__':
    quads = Euler177()
    print len(quads)
    pass
