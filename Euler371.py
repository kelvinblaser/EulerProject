# Euler 371
#
# Naieve solution assuming 26**3 is close enough to infinity that we are 
# accurate to 8 places

import numpy as np

E = np.zeros((2,500), dtype=np.float64)

E[0, 499] = 2.004
E[1, 499] = 2.0

for n in range(498, -1, -1):
    E[1,n] = 1000.0/(999-n) * (1.0 + (499-n)/500.0 * E[1,n+1])
    E[0,n] = 1000.0/(999-n) * (1.0 + (499-n)/500.0 * E[0,n+1] + E[1,n]/1000.0)
    
print E[0,0]