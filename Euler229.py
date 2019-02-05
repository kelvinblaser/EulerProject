def Euler229(m):
    from math import sqrt
    memo = {}
    coeff = [1,2,3,7]
    for x in range(1, int(sqrt(m))+1):
        for a in range(1, int(sqrt(m))+1):
            for i,c in enumerate(coeff):
                n = a*a + c*x*x
                if n <= m:
                    try:
                        memo[n] |= 2**i
                    except KeyError:
                        memo[n] = 2**i
                n = x*x + c*a*a
                if n <= m:
                    try:
                        memo[n] |= 2**i
                    except KeyError:
                        memo[n] = 2**i
            
        if x%100 == 0:
            print x, len(memo)
            for n in memo.keys():
                if n < x*x:
                    if memo[n] != 15:
                        del memo[n]

    count = 0
    for n in memo:
        if memo[n] == 15:
            count += 1

    return count
