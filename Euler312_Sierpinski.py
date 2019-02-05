# Euler 312 - Cyclic paths on Sierpinski graphs
# Kelvin Blaser   2014.04.27

import scipy as sp

def mat_mod_exp(M, e, m):
    if e == 1:
        return sp.array(M)%m
    X = mat_mod_exp(M, e/2, m)
    X %= m
    if e%2 == 1:
        return sp.dot(X, sp.dot(X,M))%m
    return sp.dot(X,X)%m

def mod_exp(x,e,m):
    if e == 1:
        return x%m
    b = mod_exp(x,e/2,m)
    if e%2 == 1:
        return (b*b*x)%m
    return (b*b)%m


if __name__ == '__main__':
    x3 = sp.array([3,2,1,2,1,0,0,1])
    M = sp.array([[3,1,0,0,-2,-1,0,0],
                  [1,3,0,0,-1,-2,0,0],
                  [0,0,3,1,0,0,-2,-1],
                  [0,0,1,3,0,0,-1,-2],
                  [1,0,0,0,0,0,0,0],
                  [0,1,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0]], dtype=sp.int64)

    # Calculate C(10000)
    Z = mat_mod_exp(M,9996,2*2*3*13**7)
    X = Z.dot(x3)% (2*2*3*13**7)
    #print X
    print ((mod_exp(2,X[0],13**8)*mod_exp(3,X[2],13**8))%13**8)**3%13**8

    # Calculate C(C(C(10000))) mod 13^8
    m1a = 2**10*3*13**3   # phi(phi(phi(phi(phi(13**8)))))
    Z1 = mat_mod_exp(M,9996,m1a)
    X1 = Z1.dot(x3) % m1a
    m1b = 2**8*3*13**4    # phi(phi(phi(phi(13**8))))
    C1 = ((mod_exp(2,X1[0],m1b)*mod_exp(3,X1[2],m1b))%m1b)**3%m1b

    m2a = 2**6*3*13**5    # phi(phi(phi(13**8)))
    Z2 = mat_mod_exp(M,C1-4,m2a)
    X2 = Z2.dot(x3) % m2a
    m2b = 2**4*3*13**6    # phi(phi(13**8))
    C2 = ((mod_exp(2,X2[0],m2b)*mod_exp(3,X2[2],m2b))%m2b)**3%m2b

    m3a = 2**2*3*13**7    # phi(13**8)
    Z3 = mat_mod_exp(M,C2-4,m3a)
    X3 = Z3.dot(x3) % m3a
    m3b = 13**8
    C3 = ((mod_exp(2,X3[0],m3b)*mod_exp(3,X3[2],m3b))%m3b)**3%m3b

    print C3
    
