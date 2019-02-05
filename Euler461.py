################################################################################
# Euler 461 - Almost Pi
# Kelvin Blaser      2015.03.14  (Or 3.14.15  The Pi day of the century)
#
################################################################################
import scipy as sp

def bisect(ab_dat, val):
    bot, top = 0,len(ab_dat)-1
    while top-bot > 1:
        mid = (top+bot)//2
        if ab_dat[mid]['val'] > val:
            top = mid
        else:
            bot = mid
    return top

def f(n,k):
    return sp.exp(float(k)/float(n)) - 1.0

def g(N):
    ab_type = sp.dtype([('val',sp.float64),('a',sp.int16),('b',sp.int16)])
    k_max = int(N*sp.log(sp.pi+1)) + 1

    ff = [f(N,k) for k in range(0,k_max+1)]

    ab_dat = sp.zeros((k_max*(k_max+1))/2, dtype = ab_type)
    ix = 0
    for a in xrange(1,k_max+1):
        for b in xrange(1,a+1):
            ab_dat[ix]['val'] = ff[a] + ff[b]
            ab_dat[ix]['a'] = a
            ab_dat[ix]['b'] = b
            ix += 1
            if ix%1000000 == 0:
                print 'Building %d/%d'%(ix,len(ab_dat))
    ab_dat.sort()

    gmin = sp.pi
    amin,bmin,cmin,dmin = 0,0,0,0

    for ix in xrange(len(ab_dat)):
        if ix%1000000 == 0:
            print 'Searching %d/%d'%(ix,len(ab_dat))
        jx = bisect(ab_dat, sp.pi-ab_dat[ix]['val'])
        if jx > 0:
            v = ab_dat[ix]['val'] + ab_dat[jx-1]['val']
            if abs(v-sp.pi) < gmin:
                gmin = abs(v - sp.pi)
                listmin = [ab_dat[ix]['a'],ab_dat[ix]['b'],
                           ab_dat[jx-1]['a'],ab_dat[jx-1]['b']]
                listmin.sort()
                amin,bmin,cmin,dmin = tuple(listmin)
                print v,amin,bmin,cmin,dmin,amin**2+bmin**2+cmin**2+dmin**2
        if jx < len(ab_dat):
            v = ab_dat[ix]['val'] + ab_dat[jx]['val']
            if abs(v-sp.pi) < gmin:
                gmin = abs(v - sp.pi)
                listmin = [ab_dat[ix]['a'],ab_dat[ix]['b'],
                           ab_dat[jx]['a'],ab_dat[jx]['b']]
                listmin.sort()
                amin,bmin,cmin,dmin = tuple(listmin)
                print v,amin,bmin,cmin,dmin,amin**2+bmin**2+cmin**2+dmin**2

    return amin,bmin,cmin,dmin,ff[amin]+ff[bmin]+ff[cmin]+ff[dmin],gmin
        
    
    
