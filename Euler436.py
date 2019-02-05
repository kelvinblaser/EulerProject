import numpy.polynomial as pn
import numpy.random as rd
import pylab as pl
import numpy as np

class Sum_Dist:
    ''' Creates functions which represents the probablility distribution of a
    sum of n numbers drawn from a uniform random sample [0,1).'''
    
    def __init__(self, n):
        # Create the segmented polynomials
        if n <= 1:
            n = 2
        self.n = n
        polys = [[pn.Polynomial([0])]*(n+1) for i in range(n+1)]
        polys[1][1] = pn.Polynomial([1])
        for i in range(2,n+1):
            #for x in polys:
            #    for y in x:
            #        print y
            #    print ' '
            for j in range(n,0,-1):
                polys[i][j] = polys[i-1][j].integ()
                polys[i][j] = polys[i][j] - polys[i][j](j-1)
                new_poly = polys[i-1][j-1].integ()
                new_poly = new_poly(j-1) - new_poly(pn.Polynomial([-1, 1]))
                polys[i][j] += new_poly

        self.polys = polys

    # Create the sum distribution from the polynomials
    def __call__(self, n, x):
        ''' Returns the probabitlity distribution of a sum of n numbers drawn 
        from a uniform random sample [0,1).'''
        if x <= 0:
            return 0
        if x >= n:
            return 0
        return self.polys[n][int(x)+1](x)

def special_integral(m,n,sum_dist):
    poly_m = sum_dist.polys[m][2]
    poly_n = sum_dist.polys[n][1]

    # v integration
    poly_y = poly_m.integ()
    poly_y = poly_y(2) - poly_y(pn.Polynomial([2,-1]))

    # u integration
    poly_x = poly_n.integ()
    poly_x = poly_x(1) - poly_x(pn.Polynomial([1,-1]))

    # y integration
    poly_z = poly_y.integ()
    poly_z = poly_z(1) - poly_z(pn.Polynomial([0,1]))
    
    # x integration
    poly_x = poly_x * poly_z
    poly_x = poly_x.integ()
    return poly_x(1) - poly_x(0)

def Euler436(N=20):
    P = [[pn.Polynomial([0]) for i in range(3)] for j in range(N+1)]
    P[1][1] += 1
    I1 = [[pn.Polynomial([0]) for i in range(3)] for j in range(N+1)]
    I2 = [[pn.Polynomial([0]) for i in range(3)] for j in range(N+1)]
    I3 = [[pn.Polynomial([0]) for i in range(3)] for j in range(N+1)]
    IZ = [[pn.Polynomial([0]) for i in range(3)] for j in range(N+1)]
    for i in range(2,N+1):
        for j in range(2,0,-1):
            P[i][j] = P[i-1][j].integ()
            P[i][j] -= P[i][j](j-1)
            new_poly = P[i-1][j-1].integ()
            new_poly = new_poly(j-1) - new_poly(pn.Polynomial([-1,1]))
            P[i][j] += new_poly
    for i in range(N+1):
        for j in range(1,3):
            I1[i][j] = P[i][j].integ()
            I1[i][j] -= I1[i][j](j-1)
            I1[i][j] += I1[i][j-1](j-1)
            I2[i][j] = I1[i][j].integ()
            I2[i][j] -= I2[i][j](j-1)
            I2[i][j] += I2[i][j-1](j-1)
            I3[i][j] = I2[i][j].integ()
            I3[i][j] -= I3[i][j](j-1)
            I3[i][j] += I3[i][j-1](j-1)
            IZ[i][j] = I1[i][j] * pn.Polynomial([0,1])
            IZ[i][j] = IZ[i][j].integ()
            IZ[i][j] -= IZ[i][j](j-1)
            IZ[i][j] += IZ[i][j-1](j-1)


#    pl.figure('P')
    x = np.linspace(0,1.99,200)
#    for i in range(1,N+1):
#        y = np.array([P[i][int(a)+1](a) for a in x])
#        pl.plot(x,y)
#    pl.figure('I1')
#    for i in range(1,N+1):
#        y = np.array([I1[i][int(a)+1](a) for a in x])
#        pl.plot(x,y)
#    pl.figure('I2')
#    for i in range(1,N+1):
#        y = np.array([I2[i][int(a)+1](a) for a in x])
#        pl.plot(x,y)
#    pl.figure('IZ')
#    for i in range(1,N+1):
#        y = np.array([IZ[i][int(a)+1](a) for a in x])
#        pl.plot(x,y)

    prob = 0
    eta = pn.Polynomial([0,1])
    for n in range(1, N+1):
        eta_int1 = [z(1) - z for z in IZ[n-1]]
        z_int1 = [p for p in P[n-1]]
        for i in range(3):
            eta_int1[i] += eta*I1[n-1][i] - eta*(I1[n-1][i](1))
        pl.figure('eta_int1')
        y = np.array([eta_int1[int(a)+1](a) for a in x])
        pl.plot(x,y)
        for m in range(1, N+1):
            eta_int = [I for I in I1[m-1]]
            eta_int[1] = eta_int[1](1-eta)
            eta_int[0] = eta_int[2](1-eta)
            eta_int[2] = eta_int[0](1-eta)
            z_int = [z_int1[i] * I3[m-1][i] for i in range(3)]
            for j in range(3):
                eta_int[j] *= eta_int1[j]
            for j in range(1,3):
                eta_int[j] = eta_int[j].integ()
                eta_int[j] -= eta_int[j](j-1)
                eta_int[j] += eta_int[j-1](j-1)
                z_int[j] = z_int[j].integ()
                z_int[j] -= z_int[j](j-1)
                z_int[j] += z_int[j-1](j-1)
            pl.figure('eta_int')
            y = np.array([eta_int[int(a)+1](a) for a in x])
            pl.plot(x,y)
            pl.figure('z_int')
            y = np.array([z_int[int(a)+1](a) for a in x])
            pl.plot(x,y)
            prob += eta_int[1](1) - eta_int[1](0)
            prob -= 0.5 * (z_int[1](1) - z_int[1](0))
                
    return prob
##N = 20
##sum_dist = Sum_Dist(N)
##prob = 0.0
##for n in range(1,N):
##    for m in range(n+1, N+1):
##        prob += special_integral(m,n,sum_dist)
##        print '\t', prob
##    print prob
##
##print ' '
##print prob
        
