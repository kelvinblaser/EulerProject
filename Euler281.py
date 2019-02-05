#---------------------------------------------------
# Euler 281
#
# http://math.stackexchange.com/questions/600/circular-permutations-with-indistinguishable-objects
#
# Hmmmm - Wrong answer  =(
#---------------------------------------------------

FMAX = 10**15

# Find the maximum n we need to consider
nMax = 1
while 2**nMax <= 2*nMax*FMAX:
    nMax += 1

phi = list(range(nMax+1))
divisors = [[] for x in phi]

# Calculate totient and divisors
divisors[1].append(1)
for x in range(2, nMax+1):
    divisors[x].append(1)
    if phi[x] == x: # Found a prime
        for y in range(x,nMax+1,x):
            phi[y] /= x
            phi[y] *= x-1
    for y in range(x,nMax+1,x):
        divisors[y].append(x)
        
# For each n, calculate f(m,n) starting with m = 2.
# f is strictly increasing with m, so once f(m,n) > FMAX,
# stop adding it to the sum
s = 0
for n in range(1, nMax+1):
    f = 0
    m = 2
    while f <= FMAX:
        s += f
        f = 0
        for k in divisors[n]:
            kProd = 1
            for x in range(m):
                num = 1
                den = 1
                for y in range(1,k+1):
                    num *= x*k + y
                    den *= y
                kProd *= num
                kProd //= den
            f += kProd * phi[n//k]
            #if m == 2 and n == 2: print k, kProd, phi[n//k]
            #print f
        f //= m*n
        m += 1
        #if f <= FMAX: print n, m-1, f
print s