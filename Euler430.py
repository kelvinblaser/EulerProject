#Euler 430 - Disk Flipping
# Kelvin Blaser

import scipy as sp

def E(N,M, tol=0.001):
    n = 1
    ans = 0
    n_max = int(N/2)
    while n <= n_max:
        diff = P(n,N,M)
        if abs(diff) < tol:
            break
        ans += diff
        #if n%10000 == 0:
         #   print n, ans
        n += 1
    if int(N)%2 == 1:
        ans += P(int(N)/2+1, N, M) / 2.
    ans += float(N)/2
    return ans

def P(n,N,M):
    b = (2*n*(N-n+1) - 1) / float(N*N)
    a = 1. - b
    #A = sp.array([[a,b],[b,a]])
    #AM = mat_pow(A,M)
    #return AM[0,0]
    return (a-b)**M

def mat_pow(A,M):
    if M==1:
        return A

    X = mat_pow(A, M/2)
    X = sp.dot(X,X)
    if M%2 == 0:
        return X
    return sp.dot(X,A)


    
