# Euler 199 - Iterative Circle Packing
# projecteuler.net/problem=199
# Kelvin Blaser     2014.11.21

# A faster way would have been to know about Soddy Circles
#  =(

from scipy.optimize import root
import scipy as sp
import pylab as pl

def new_circ(gap, main_gap=False):
    c1,c2,c3 = gap
    x1,y1,r1 = c1
    x2,y2,r2 = c2
    x3,y3,r3 = c3
    w1,w2,w3 = 1/r1,1/r2,1/r3
    x0 = (x1*w1+x2*w2+x3*w3)/(w1+w2+w3)
    y0 = (y1*w1+y2*w2+y3*w3)/(w1+w2+w3)
    r0 = 1/(w1+w2+abs(w3))
    #if main_gap:
    #    r3 = -r3
    def f(x):
        y = [(x[0]-x1)**2 + (x[1]-y1)**2  - (x[2]+r1)**2,
             (x[0]-x2)**2 + (x[1]-y2)**2  - (x[2]+r2)**2,
             (x[0]-x3)**2 + (x[1]-y3)**2  - (x[2]+r3)**2]
        return y
    def jac(x):
        J = sp.array([[2*(x[0]-x1), 2*(x[1]-y1), -2*(x[2]+r1)],
                      [2*(x[0]-x2), 2*(x[1]-y2), -2*(x[2]+r2)],
                      [2*(x[0]-x3), 2*(x[1]-y3), -2*(x[2]+r3)]])
        return J
    sol = root(f,[x0,y0,r0],jac=jac)
    return tuple(sol.x)

def plot_circle(circ,color='k'):
    phi = sp.linspace(0,2*sp.pi,100)
    xc,yc,r = circ
    x = r*sp.cos(phi)+xc
    y = r*sp.sin(phi)+yc
    pl.plot(x,y,color)

def Euler199(iterations=3,plot=False):
    colors = ['r','g','b']
    # Initial Circles
    r = 1. / (1 + 2/sp.sqrt(3))
    x1,y1 = 0,1-r
    x2,y2 = r,-r/sp.sqrt(3)
    x3,y3 = -x2,y2
    circles = [(x1,y1,r),(x2,y2,r),(x3,y3,r)]

    # Initial Gaps
    main_circle = (0.,0.,-1.)
    gaps = [(circles[0],circles[1], main_circle),
            (circles[0],circles[2], main_circle),
            (circles[1],circles[2], main_circle),
            (circles[0],circles[1],circles[2])]
    if plot:    
        for circ in circles:
            plot_circle(circ,'b')


    # In each iteration
        # For each gap in the iteration (2 types of gaps)
            # Calculate biggest circle in gap
            # Add the biggest circle in gap to circles
            # Add three new gaps to next iterations gaps
                # (Should end up with 4*3^iterations gaps)

    new_gaps = []
    for i in range(iterations):
        for gap in gaps:
            circ = new_circ(gap)
            if plot:
                plot_circle(circ, colors[i%3])
            circles.append(circ)
            new_gaps.append((circ, gap[0], gap[1]))
            new_gaps.append((circ, gap[1], gap[2]))
            new_gaps.append((circ, gap[0], gap[2]))
        gaps = new_gaps
        new_gaps = []

    if plot:
        plot_circle((0,0,1))
        pl.axis('equal')
        pl.show()

    # return 1 - Sum of areas / Total area
    return 1 - sum(c[2]*c[2] for c in circles)
    

if __name__ == '__main__':
    print Euler199(3)
    print Euler199(10)
