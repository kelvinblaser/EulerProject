import scipy as sp
from scipy.integrate import trapz
## Trapezoidal rule converges very fast for smooth periodic functions.
## 64 samples is enough to get the required precision.

def ellipse_center_path(a,b,N=128):
    alpha = sp.linspace(0,sp.pi/2,N)
    s = sp.sin(alpha)
    c = sp.cos(alpha)
    z = sp.sqrt(a*a*c*c + b*b*s*s)
    dx = z+(b*b-a*a)*(a*a*c*c*c*c - b*b*s*s*s*s)/(z*z*z)
    dy = -a*b*(b*b-a*a)*c*s/(z*z*z)
    integrand = sp.sqrt(dx*dx + dy*dy)
    return 4*trapz(integrand,alpha)

if __name__ == '__main__':
    print ellipse_center_path(1,4,64)
    print ellipse_center_path(2,4,64)
    print ellipse_center_path(3,4,64)
    print ellipse_center_path(4,4,64), 2*sp.pi*4
    print ellipse_center_path(1,4,64) + ellipse_center_path(3,4,64)
