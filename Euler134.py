# Euler 134 - Prime Pair Connection
# Kelvin Blaser
from Primes import MakePrimeList

ps = MakePrimeList(1000000)[2:]
ans = 0
for i in range(len(ps)-1):
    p1,p2 = ps[i],ps[i+1]
    n = p1
    d = 0
    while n > 0:
        d += 1
        n /= 10
    x = (-p1 * pow(10*d,p2-2,p2))%p2
    ans += p1 + x*10**d
print ans
