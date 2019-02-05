#-------------------------------------------------------------------
# Euler 512
#
#  We're just adding up the totients of odd numbers up to n here
#-------------------------------------------------------------------

def Euler512(n):
    f = list(xrange(1,n+1,2))
    g = 1
    print 'Just startin\' bro'
    for ix in range(1,len(f)):
        if isPow10TimesSingleDigit(ix):
            print ix, g
        p = 2*ix+1
        if not f[ix] == p:
            g += f[ix]
            continue
        for jx in range(ix,len(f),p):
            f[jx] /= p
            f[jx] *= p-1
        g += f[ix]
    return g
    
def isPow10TimesSingleDigit(n):
    while n >= 10:
        if not n%10 == 0:
            return False
        n /= 10
    return True
    
    
if __name__ == '__main__':
    print 'g(100) = {0}'.format(Euler512(100))
    print 'g(5x10^8) = {0}'.format(Euler512(5*10**8))    