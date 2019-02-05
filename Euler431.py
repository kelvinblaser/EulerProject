###############################################################################
# Euler 431 - Square Space Silo
# Kelvin Blaser         2015.4.2
#
#------------------------------------------------------------------------------
# Set a 2d coordinate system up in the horizontal plane with the origin at the
# center axis of the silo.  The height of the empty space above the point (x,y)
# is z = tan(alpha) * sqrt((x-X)^2 + y^2) where X is the horizontal distance to
# the point of the cone from the center of silo and alpha is the angle of repose
# of the grain.  The volume V is just the integral of this function z(x,y) over
# the cross-section of the silo.
#
# To simplify calculations, make a change of variables x = Rx', y = Ry', z = Rz'
# X = RX'and factor out the tan(alpha) so that
#
# V(X) = tan(alpha) * R^3 v(X/R)   where
#   v(f) = iint sqrt((x-f)^2 + y^2) dxdy
#
#------------------------------------------------------------------------------
# Since v(f) is monotonic, we can simply find V(0) and V(R) to know which
# square numbers to search for.  For each possible square n^2, use a binomial
# search to find the X = Rf for which V(X) = n^2
#
###############################################################################

from scipy.integrate import dblquad
from scipy import pi, tan, sqrt

def llim(x):
    return -sqrt(1-x*x)

def ulim(x):
    return sqrt(1-x*x)

def reducedVolume(f):
    def integrand(x,y):
        return sqrt((x-f)*(x-f) + y*y)
    return dblquad(integrand,-1.0,1.0,llim,ulim)
    
def Volume(X,R,alpha):
    v,err = reducedVolume(float(X)/R)
    err *= R * R * R * tan(alpha)
    return v * R * R * R * tan(alpha)

def findOffset(n,R,alpha):
    xtop = R
    xbot = 0.0
    vtop = Volume(xtop,R,alpha)
    vbot = Volume(xbot,R,alpha)
    while xtop - xbot > 1e-10:
        xmid = (xtop + xbot)/2.
        vmid = Volume(xmid,R,alpha)
        print '%2.10f  %2.10f'%(xmid, vmid)
        if vmid > n:
            xtop = xmid
            vtop = vmid
        else:
            xbot = xmid
            vbot = vmid
    return (xtop+xbot)/2.

def Euler431(R,alpha):
    Vmax = Volume(R,R,alpha)
    Vmin = Volume(0.0,R,alpha)
    ret = 0.0
    nn = [n for n in range(int(sqrt(Vmin)),int(sqrt(Vmax))+2) if
          n*n >= Vmin and n*n <= Vmax]
    for n in nn:
        ret += findOffset(n*n,R,alpha)
    return ret

