import Primes

def Euler122():
    primes = Primes.MakePrimeList(200)
    m = {}
    m[1] = 0
    for x in range(2, 201):
        if x in primes:
            m[x] = m[x-1] + 1
        else:
            m[x] = 0
            y = x
            for p in primes:
                while y%p == 0 and y > 0:
                    m[x] += m[p]
    ans = 0
    for x in range(1, 201):
        ans += m[x]

    print 'Sum: ', ans
    return ans
