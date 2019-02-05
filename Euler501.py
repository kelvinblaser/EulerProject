import Primes
#reload(Primes)

def eightDivisorCount(n):
    ps = Primes.MakePrimeList(int(n**0.5)+2)
    primePi = Primes.Prime_Pi()
    f = 0
    for p in ps:
        if p**7 > n:
            break
        #print p
        f += 1
    for p in ps:
        if 2*p**3 > n:
            break
        f += primePi(n//(p**3), ps)
        print p,f,len(primePi.restricted_memo)
        if (n//(p**3)) >= p:
            f -= 1
        #print p, primePi(n//(p**3), ps)
    for n1,p1 in enumerate(ps):
        if p1**3 >= n:
            break
        for p2 in ps[n1+1:]:
            if p1*p2*p2 >= n:
                break
            f += primePi(n//(p1*p2),ps) - primePi(p2,ps)
            #print p1,p2,primePi(n//(p1*p2),ps),primePi(p2,ps)
            if p2 < 10000:
                print p1,p2,f,len(primePi.restricted_memo)
        print p1,f,len(primePi.restricted_memo)

    return f
        
