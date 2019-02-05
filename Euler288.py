################################################################################
# Euler 288 - An Enormous Factorial
# Kelvin Blaser      2015.03.07
#
# Since Tn < p by definition, the number N(p,q) can be written in base p as
# [Tn Tn-1 Tn-2 ... T2 T1 T0].  That is, Tn is the (n+1)th digit of N(p,q) in
# base p.
#
# This is nice, because then dividing by p^e, floor(N(p,q)/p^e) can be done by
# truncating the last e terms in the sum (digits base p) and subtracting e from
# the exponent of p^n in the rest of the terms.
#
#  NF(p,q) = sum( floor( N(p,q) / p^e ) for e in range(1,infinity) )
#          = sum( sum( Tn p^(n-e) for n in range(1,q+1) ) for e in range(1,n+1)
#
# Taking this sum modulo p^x term by term shows that we only need the terms for
# which (n-e) < x.  Changing the order of summation and applying this
# restriction gives
#
#  NF(p,q) = sum( Tn * sum( p^j for j in range(0,min(n,x)) ) for n in
#                                                           range(1,q+1) )
#          = sum( Tn * (p^y - 1)/(p-1) for n in range(0,q+1) )
#                   where y = min(n,x)
################################################################################

def rngGen(p,q):
    s = 290797
    for x in xrange(q+1):
        yield s % p
        s *= s
        s %= 50515093

def NF(p,q,x):
    ''' Gives NF(p,q) mod p^x '''
    ret = 0
    py = [p**y for y in range(x+1)]
    px = p**x
    for n,Tn in enumerate(rngGen(p,q)):
        ret += Tn * (py[min(x,n)] - 1)/(p-1)
        ret %= px
    return ret

if __name__ == '__main__':
    print 'NF(%d,10^%d) mod %d^%d = %d'%(3,4,3,20,NF(3,10**4,20))
    print 'NF(%d,10^%d) mod %d^%d = %d'%(61,7,61,10,NF(61,10**7,10))
        
