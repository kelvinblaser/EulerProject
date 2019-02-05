# Euler 250 - https://projecteuler.net/problem=250
# 250250
# Kelvin Blaser   2014.10.14
import scipy as sp

MOD = 10**16

# Calculate the members of the set mod 250
set250 = [pow(x,x,250) for x in range(1,250251)]

# Calculate the counts of each number
c = [set250.count(x) for x in range(250)]

# ways[i,j] = ways to sum a set of i's to get j mod 250
ways = sp.zeros((250,250), dtype=sp.int64)
for i in range(250):
    choo = 1
    ways[i,0] = 1
    for x in range(1, c[i]+1):
        choo *= c[i]+1-x
        choo /= x
        ways[i,(i*x)%250] += choo % MOD
        ways[i,(i*x)%250] %= MOD

# upp[i,j] = ways to sum a set of i+'s to get j mod 250
upp = sp.zeros((250,250), dtype=sp.int64)
upp[249,:] = ways[249,:]
for i in range(248,-1,-1):
    print i
    for x in range(250):
        z1 = int(ways[i,x])
        for y in range(250):
            z2 = int(upp[i+1,y])
            upp[i,(x+y)%250] += (z1*z2)%MOD
            upp[i,(x+y)%250] %= MOD

print upp[0,0]


