
from collections import defaultdict
from scipy import ones, zeros, array, where, concatenate
from pylab import plot, figure
from Primes import MakePrimeList

def C(n, color='r', plo=False):
    ps = MakePrimeList(n)
    print 'Primes Calculated'
    mu = list(ones(n+1))
    for p in ps:
        for x in range(p,n+1,p):
            mu[x] *= -1
        for x in range(p*p,n+1,p*p):
            mu[x] = 0
    print 'Mobius Function Calculated'
    P = zeros(n+1, dtype=int)
    N = 0*P
    for i in range(1,n+1):
        P[i] = P[i-1] + (mu[i]==1)
        N[i] = N[i-1] + (mu[i]==-1)
    PmN = 100*P - 99*N
    NmP = 100*N - 99*P
    if plo:
        figure(2)
        plot(PmN,'b')
        plot(NmP,'g')
        plot((PmN+NmP)/2., 'r')
        ans = 0
        alistb = []
        blistb = []
        alistg = []
        blistg = []
        alistr = []
        blistr = []
        for a in range(1,n+1):
            for b in range(a,n+1): 
                #NN = N[b] - N[a-1]
                #PP = P[b] - P[a-1]
                #if 99*NN <= 100*PP and 99*PP <= 100*NN:
                if PmN[b] >= PmN[a-1]:
                    alistb.append(a)
                    blistb.append(b+0.3)
                if NmP[b] >= NmP[a-1]:
                    #pass
                    alistg.append(a+0.3)
                    blistg.append(b)
                if PmN[b] >= PmN[a-1] and NmP[b] >= NmP[a-1]:
                    alistr.append(a)
                    blistr.append(b)
                    ans += 1
    if plo:
        figure(1)
        plot(alistb, blistb, 'ob')
        plot(alistg, blistg, 'og')
        plot(alistr, blistr, 'or')
    blue = countCriterion(PmN)
    print 'Blue Calculated'
    green = countCriterion(NmP)
    print 'Green Calculated'
    return blue + green - n*(n+1)/2

def countCriterion(z):
    counts = defaultdict(int)
    ans = 0
    counts[0] = 1
    for i in range(1,len(z)):
        if i%100000 == 0:
            print i, ans
        ans += sum(counts[x] for x in counts if x <= z[i])
        counts[z[i]] += 1  
    print 'Values in dictionary: %d'%(len(counts))
##    q = array(z)
##    ans = 0
##    while len(q) > 0:
##        ixs = where(q == max(q))
##        ix = max(ixs[0])
##        ans += ix
##        q = concatenate((q[:ix],q[ix+1:]))
    return ans
