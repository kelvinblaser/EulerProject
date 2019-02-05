#------------------------------------------------------------------------------
# Euler 607 - Marsh Crossing
#   Kelvin Blaser Sept. 9, 2017
#
# 1. Rotate the reference frame by 45 degrees
# 2. Have to travel 100/sqrt(2) leagues horizontal and the same vertical
# 3. Calculate x and y coords for the straight path through the marsh 'strips'
# 4. Let y coords vary, but initial and final y coords are fixed
# 5. Time spent is sum of d(r_i, r_i+1) / v_i for each interval
# 6. Minimize using scipy
# 7. ???
# 8. Profit
#------------------------------------------------------------------------------

from scipy.optimize import minimize
from matplotlib.pyplot import plot, show

def calcXvalues():
    x = [0.0]*8
    x[7] = 100.0 / (2**0.5)
    x[1] = (x[7] - 50.0)/2.0
    for i in range(2, 7):
        x[i] = x[i-1] + 10.0
    return x
    
def timeToCross(yOpt, x, v):
    y = [0.0]
    y.extend(yOpt)
    y.append(x[-1])
    T = 0.0
    for i in range(7):
        T += (((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)**0.5)/v[i]
    return T

def solveMarshCrossing():
    x = calcXvalues()
    y = x[:]
    v = [10, 9, 8, 7, 6, 5, 10]
    res = minimize(timeToCross, y[1:7], args=(x,v), tol=10e-15)
    return res

if __name__ == '__main__':
    res = solveMarshCrossing()
    print res
    x = calcXvalues()
    y = [0.0]
    y.extend(res.x)
    y.append(x[-1])
    plot(x,y)
    show()