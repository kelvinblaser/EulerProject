import pylab as pl
import numpy as np
from math import atan2, sin, cos, pi, sqrt

rel_r_pos = [(cos(2*pi*n/5.0), sin(2*pi*n/5.0)) for n in range(5)]
rel_l_pos = [(-x,y) for x,y in rel_r_pos]
d = sqrt(2*(1-cos(2*pi/5.0)))

def r(circ_center, pos, num_arcs, memo):
    key = (str(round(circ_center[0],6)), str(round(circ_center[1],6)), pos, num_arcs, 'r')
    try:
        return memo[key]
    except KeyError:
        pass
    if num_arcs == 0:
        if round(circ_center[0],6) == 0.0 and round(circ_center[1],6) == 0.0 and pos == 0:
            return 1
        else:
            return 0
    position = [circ_center[i] + rel_r_pos[pos][i] for i in range(2)]
    if d*(num_arcs+1) < sqrt((position[0]-1)**2 + position[1]**2):
        return 0
    
    new_pos = (pos+1)%5
    new_circ_center = [circ_center[i] + 2*rel_r_pos[new_pos][i] for i in range(2)]
    memo[key] = r(circ_center, new_pos, num_arcs-1, memo) + l(new_circ_center, (5-new_pos)%5, num_arcs-1, memo)
    return memo[key]

def l(circ_center, pos, num_arcs, memo):
    key = (str(round(circ_center[0],6)), str(round(circ_center[1],6)), pos, num_arcs, 'l')
    try:
        return memo[key]
    except KeyError:
        pass
    if num_arcs == 0:
        return 0
    position = [circ_center[i] + rel_l_pos[pos][i] for i in range(2)]
    if d*(num_arcs+1) < sqrt((position[0]-1)**2 + position[1]**2):
        return 0
    
    new_pos = (pos+1)%5
    new_circ_center = [circ_center[i] + 2*rel_l_pos[new_pos][i] for i in range(2)]
    memo[key] = l(circ_center, new_pos, num_arcs-1, memo) + r(new_circ_center, (5-new_pos)%5, num_arcs-1, memo)
    return memo[key]

if __name__ == '__main__':
    memo = {}
    print 2*r([0.0,0.0],0,5,memo), 'paths in 5 arcs'
    print 2*r([0.0,0.0],0,25,memo), 'paths in 25 arcs'
    print 2*r([0.0,0.0],0,70,memo), 'paths in 70 arcs'
    print 2**25, 2**70

