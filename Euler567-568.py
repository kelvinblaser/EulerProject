# Euler 567 & 568
#
# First, by probability and combinatorial arguments, we find
#
#   JA(n) = 1/2^n sum( nCk / k, k = 1 .. n )
#   JB(n) = sum( 1 / (k * nCk), k = 1 .. n )
#
# From https://arxiv.org/pdf/math/0104026v1.pdf
# and Equation 12 and 13 from https://cs.uwaterloo.ca/journals/JIS/VOL7/Sury/sury99.pdf
# we can derive alternate forms for JA and JB
#
#   JA(n) = 1/2^n sum( (2^k-1)/k, k = 1 .. n )
#   JB(n) = 1/2^n sum( 2^k / k, k = 1 .. n )
#
# For problem 567
#   Define X(n) = sum( 2^(k+1) - 1 / k, k = 1 .. n )
#
#   S(m) = sum ( X(n) / 2^n, n = 1 .. m )
#
#   Rearrange the sums in S(m) to get
#
#   S(m) = (4 + 1/2^m)Hm - 2sum(1/(k 2^k), k = 1 .. m) - 2*sum(1/(2^k(m-k)) k = 0 .. m-1)
#   where Hm is the mth Harmonic number sum(1/k, k = 1 .. m)
#
#   In the limit of large m, Hm -> ln(m) + gamma + 1/2m where gamma is 
#    Euler-Mascheroni constant
#
#   The first sum looks like the expansion of ln(1+x) for x = -1/2. For large m,
#   this term looks like -2 sum(1/k 2^k) -> 2ln(1-1/2) = -2ln(2) = - ln(4)
#
#   In the second sum, for large m only the first few terms contribute much, 
#   where 2^k is small and m-k is approximately m
#
#   sum(1/(2^k(m-k) k = 0 .. m-1) -> sum(1/(m 2^k), k = 0 .. inf) = 2/m
#
#   Putting these together, we get
#
#   S(m) = 4(ln(m) + gamma + 1/2m) - ln(4) - 4/m
#
# For problem 568
#   D(n) = JB(n) - JA(n) = 1/2^n sum( 1/k, k = 1 .. n ) -> 1/2^n (ln(n) + gamma)
#   
#   Again with gamma the Euler-Mascheroni constant
#
# Use logarithms to keep the extreme numbers more manageable

from math import exp, log

EulerMascheroni = 0.577215664901533

def S(m):
    return 4*(log(m) + EulerMascheroni + 1/(2.0*m)) - log(4) - 4.0/m
    
def D(n):
    logAns = log(log(n) + EulerMascheroni) - n*log(2)
    log10 = log(10)
    exponent = int(logAns / log10)
    mantissa = exp( logAns - exponent*log10 )
    return mantissa, exponent
    
if __name__ == '__main__':
    print 'S(123456789) = {0}'.format(S(123456789))
    m,e = D(123456789)
    print 'D(123456789) = {0} x 10^{1}'.format(m*10, e-1)
    print 'Seven sig digits = {0}'.format(int(m*10**7))
        
# What follows is me trying to divine the pattern =D

#def JAgen(n):
#    #n2 = 1.0 # pow(0.5, n)
#    nCk = 1.0
#    lnCk = log(nCk)
#    l2n = n*log(2.0)
#    comp = 0.0
#    for k in range(1, n+1):
#        delta = log(n-k+1) - log(k) - comp
#        t = lnCk + delta
#        comp = (t-lnCk)-delta
#        lnCk = t
#        yield exp(lnCk - log(k) - l2n)
#    return
#    
#def JBgen(n):
#    nCk = 1.0
#    lnCk = log(nCk)
#    comp = 0.0
#    for k in range(1, n+1):
#        delta = log(n-k+1) - log(k) - comp
#        t = lnCk + delta
#        comp = (t-lnCk)-delta
#        lnCk = t
#        yield exp(-lnCk - log(k))
#    return
#    
#def JB(n):
#    if n <= 50:
#        return sum(JBgen(n))
#    return sum(pow(2.0, 50 - j) / (n-j) for j in range(51)) / pow(2.0, 50)
#    
#def JA(n):
#    if n <= 50:
#        return sum(JAgen(n))
#    return JB(n)
#    
#    
#    
#def S(m):
#    return sum(JA(n) + JB(n) for n in range(1, m+1))
#    
#def Dgen(n):
#    A = list(JAgen(n))
#    B = list(JBgen(n))
#    A.sort(reverse=True)
#    B.sort(reverse=True)
#    for x,y in zip(B, A):
#        yield x - y
#    return
#    
#def D(n):
#    return kahanSum(Dgen(n))
#    
#def kahanSum(vec):
#    s, c = 0.0, 0.0
#    for x in vec:
#        y = x - c
#        t = s + y
#        c = (t-s)-y
#        s = t
#    return s