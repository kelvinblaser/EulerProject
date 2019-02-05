################################################################################
# Euler 425 - Prime Connection
# Kelvin Blaser      2015.03.05
#
# 
################################################################################
from Primes import MakePrimeList, Miller_Rabin
from collections import defaultdict

def getConnections(p):
    digs = '0123456789'
    pstr = str(p)
    conns = []
    for ix in range(len(pstr)):
        for d in digs:
            if p > 10 and ix == 0 and d == '0' and pstr[1] == '0':
                #print p
                continue
            conns.append(int(pstr[:ix]+d+pstr[ix+1:]))
    for d in digs:
        conns.append(int(d+pstr))
    return set(conns)

def getPrimeConnections(p):
    conns = getConnections(p)
    conns = [q for q in conns if Miller_Rabin(q)]
    return conns

def not2sRelatives(N):
    primes = MakePrimeList(N)
    relatives2 = defaultdict(bool)
    relatives2[2] = True
    count = 0
    for p in primes:
        count += 1
        if count % 100 == 0:
            print '%d/%d\t%d'%(count,len(primes),p)
        if p > 100 and str(p)[:2] == '10':
            continue
        visited = defaultdict(bool)
        shell = [p]
        while shell:
            new_shell = []
            for q in shell:
                visited[q] = True
                if relatives2[q]:  # q is 2's rel ==> p is 2's rel
                    relatives2[p] = True
                    new_shell = []
                    break
                conns = [x for x in getConnections(q) if x < p]
                conns = [x for x in conns if Miller_Rabin(x)]
                conns = [x for x in conns if not visited[x]]
                new_shell.extend(conns)
            shell = new_shell
            #print shell, visited[101]
    return [p for p in primes if not relatives2[p]]

if __name__ == '__main__':
    print 'F(10^3) = %d'%(sum(not2sRelatives(1000)))
    print 'F(10^4) = %d'%(sum(not2sRelatives(10**4)))
    #print 'F(10^7) =',sum(not2sRelatives(10**7))
    


