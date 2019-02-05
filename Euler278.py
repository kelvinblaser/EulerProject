#----------------------------------------------------
# The key word for Google here is 'Frobenius Number'
# or 'Coin Problem
#
# f(a,b) = a*b - a - b
# f(a,b,c) = no general formula but.....
# if c | lcm(a,b) 
#  then f(a,b,c) = lcm(c,a) + lcm(c,b) - a - b - c
#
# Luckily for us
# lcm(pq,pr) = p^2qr / gcd(pq,qr) = pqr
# qr | pqr
# ...
# f(pq,pr,qr) = lcm(qr,pq) + lcm(qr,pr) - pq - pr - qr
#             = 2pqr - pq - pr - qr
#----------------------------------------------------

from Primes import MakePrimeList

if __name__ == '__main__':
    primes = MakePrimeList(5000)
    sp = [p for p in primes]
    for ix in range(1,len(sp)):
        sp[ix] += sp[ix-1]
    
    s = 0
    for nr,r in enumerate(primes):
        for nq,q in enumerate(primes[:nr]):
            if nq == 0 : continue
            s += (2*q*r - q - r)*sp[nq-1] - nq*q*r
    print s