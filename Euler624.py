# Euler 624
# Let F be the fibonacci matrix F = [[1,1],[1,0]
# We can show that the matrix P(n) = [[~, ~],[~,P(n)]] given by
#
#   P(n) = (I - F^n / 2^n)^(-1) - I
#
# is the solution.
#
# Ans: 984524441
#    Had some trouble with overflow.  Damn 64 bit integers....

from Primes import matModMult, matModPow
import scipy as sp

def inverse2x2(A,p):
    a,b,c,d = int(A[0,0]),int(A[0,1]),int(A[1,0]),int(A[1,1])
    X = sp.zeros((2,2),dtype=int)
    #print a,b,c,d
    det = int((a*d - b*c)%p)
    #print det
    detInv = pow(det, p-2,p)
    #print detInv
    X[0,0] = (d * detInv) % p
    X[0,1] = (-b * detInv) % p
    X[1,0] = (-c * detInv) % p
    X[1,1] = (a * detInv) % p
    #print a, detInv, p
    return X
    
def P(n,p):
    #print p
    I = sp.eye(2, dtype=int)
    F = sp.array([[1,1],[1,0]],dtype=int)
    inv2 = pow(2,p-2,p)
    F = inv2 * F
    #print F
    Pmat = inverse2x2(I-matModPow(F, n, p), p) - I
    return Pmat[1,1] % p
    
if __name__ == '__main__':
    print 'Q(P(2),109)={0}'.format(P(2,109))
    print 'Q(P(3),109)={0}'.format(P(3,109))
    print 'Q(P(10^18),1 000 000 009)={0}'.format(P(10**18, 10**9+9))