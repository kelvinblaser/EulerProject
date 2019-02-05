# Euler 297 - Zeckendorf Representation
# https://projecteuler.net/problem=297
# Kelvin Blaser 2014.10.15

def Euler297(N):
    # Generate Fibonacci numbers
    fibs = [1,2]
    while fibs[-1] < N:
        fibs.append(fibs[-1]+fibs[-2])
    memo = {1 : 0, 2 : 1}

    def find_fib(N):
        bot = 0
        top = len(fibs)-1
        mid = (top+bot)/2
        while(mid != bot):
            if fibs[mid] < N:
                bot = mid
            else:
                top = mid
            mid = (top+bot)/2
        return fibs[bot]            
    
    def sig(N):
        try:
            return memo[N]
        except KeyError:
            pass
        ff = find_fib(N)
        memo[N] = sig(ff) + sig(N-ff) + (N-ff)
        return memo[N]

    return sig(N)

if __name__ == '__main__':
    print Euler297(10**6)
    print Euler297(10**17)
        
        
        
    
