# Euler 389 - Platonic Dice
# https://projecteuler.net/problem=389
#
# Kelvin Blaser  2014.11.7

import scipy as sp
import pylab as pl

def calc_Nknm(k,n_max,m_max, tol=1e-360):
    # Nk(n,m) = Number of ways to get n from m k-sided dice
    print 'Calculating Nk(n,m) for k = %d, n = %d, m = %d'%(k,n_max,m_max)
    N = sp.zeros((n_max+1, m_max+1))
    N[1:k+1,1] = 1.0 / k
    for m in range(2,m_max+1):
        if m % 100 == 0:
            print 'm = %d'%(m,)
        for n in range(m,min(m*k,n_max)+1):
            N[n,m] = sum(N[max(0,n-k):n,m-1]) / k
            if N[n,m] < tol:
                break
            
    print ''
    return N

def plot_prob(pX):
    pl.plot(pX)

def Euler389(tol=1e-20):
    # Solve for P(T)
    pT = sp.zeros(5)
    pT[1:] = 0.25

    # Solve for P(C)
    # Nk(n,m) = Number of ways to get n from m k-sided dice
    # P(C) = sum( P(T) * N6(C,T) * 1/6**T )
    N6 = calc_Nknm(6,4*6,4)
    pC = sp.zeros(4*6+1)
    p6 = 1.0 / 6.0
    for C in range(1, 4*6+1):
        pC[C] = sum( pT[T] * N6[C,T] for T in range(4+1) )
        if pC[C] < tol:
            break
    pl.figure(1)
    plot_prob(pC)
    #pl.figure(2)
    #for T in range(1,5):
    #    plot_prob(pT[T] * N6[:,T] * p6**T)

    # Solve for P(O)
    # P(O) = sum( P(C) * N8(O,C) * 1/8**C )
    N8 = calc_Nknm(8,4*6*8,4*6)
    pO = sp.zeros(4*6*8+1)
    p8 = 1.0 / 8.0
    for O in range(1, 4*6*8+1):
        pO[O] = sum( pC[C] * N8[O,C] for C in range(4*6+1) )
        if pO[O] < tol:
            break
    pl.figure(2)
    plot_prob(pO)

    # Solve for P(D)
    # P(D) = sum( P(O) * N12(D,O) * 1/12**O )
    N12 = calc_Nknm(12,4*6*8*12,4*6*8)
    pD = sp.zeros(4*6*8*12+1)
    p12 = 1.0 / 12.0
    for D in range(1, 4*6*8*12+1):
        pD[D] = sum( pO[O] * N12[D,O] for O in range(4*6*8+1) )
        if pD[D] < tol:
            break
    pl.figure(3)
    plot_prob(pD)

    # Solve for P(I)
    # P(I) = sum( P(D) * N20(I,D) * 1/20**D )
    #N20 = sp.zeros((4*6*8*12*20+1,4*6*8*12+1))
    N20 = calc_Nknm(20,4*6*8*12*20,4*6*8*12)
    pI = sp.zeros(4*6*8*12*20+1)
    p20 = 1.0 / 20.0
    for I in range(1, 4*6*8*12*20+1):
        pI[I] = sum( pD[D] * N20[I,D] for D in range(4*6*8*12+1) )
        if pI[I] < tol:
            break
    pl.figure(4)
    plot_prob(pI)
    
    pl.show()

    # Calculate mean and variance of I
    I_mean = sum( I * pI[I] for I in range(len(pI)) )
    I_var = sum( (I-I_mean)**2 * pI[I] for I in range(len(pI)) )
    I_sig = sp.sqrt(I_var)
    pl.plot([I_mean, I_mean],[0,pI[int(I_mean)]])
    pl.plot([I_mean-I_sig, I_mean-I_sig,I_mean+I_sig, I_mean+I_sig],
            [pI[max(0,int(I_mean-I_sig))],0,0,pI[int(I_mean+I_sig)]])
    print I_mean, I_var, sum(pI), sum(pD)
    return I_var

if __name__ == '__main__':
    print Euler389()
