from scipy.integrate import dblquad
from scipy import arccos
from math import sqrt, pi

def subtend(y,x):
    num = x*(x-3) + y*(y-4)
    den = sqrt((x-3)**2 + y**2) * sqrt(x**2 + (y-4)**2)
    return arccos(num / den)
    
if __name__ == '__main__':
    I = dblquad(subtend, 0, 3, lambda x: 0, lambda x: 4-(4*x/3), epsrel=1e-18)
    print I
    print I[0] / (12*pi)