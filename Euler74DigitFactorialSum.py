#Euler 74
from scipy import misc

def factorialSum(n):
    digitSum = 0
    while n > 0:
        digitSum += misc.factorial(n%10,1)
        n /= 10
    return int(digitSum)

def chainSize(n, memo):
    if memo.has_key(n):
        return memo[n]
    try:
        memo[n] = 1 + chainSize(factorialSum(n),memo)
    except:
        print n

    return memo[n]

def initializeLoops():
    memo = {}
    memo[0] = 1
    memo[1] = 1
    memo[2] = 1
    memo[145] = 1
    memo[169] = 3
    memo[1454] = 3
    memo[363601] = 3
    memo[871] = 2
    memo[872] = 2
    memo[45361] = 2
    memo[45362] = 2
    memo[40585] = 1
    return memo


def count60(N=1000):
    memo = initializeLoops()
        
    count = 0
    for n in range(N):
        if chainSize(n,memo) == 60:
            count += 1
    return count
