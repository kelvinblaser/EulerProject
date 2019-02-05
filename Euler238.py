# Euler 238

from bisect import bisect_left

def bbs():
    # Testing reveals that blum blum shub is cyclical and s0 is part of the 
    # cycle.
    s0 = 14025256
    m = 20300713
    yield s0
    s = (s0*s0)%m
    while s != s0:
        yield s
        s = (s*s)%m

def toDigits(num):
    digs = []
    while num > 0:
        digs.append(num%10)
        num //= 10
    return digs[::-1]
    
def createAnswerArray():
    nums = list(bbs())
    digits = []
    for num in nums:
        digits.extend(toDigits(num))
    digits.extend(digits)
    
    # Make array of cumulative sums   
    runningSum = [0]*len(digits)
    runningSum[0] = digits[0]
    for i in range(1, len(digits)):
        runningSum[i] = runningSum[i-1] + digits[i]
        
    # Make answer array of size sum(digits) initialized to zero
    s = sum(digits) // 2
    p = [0]*s
    p[0] = 1
    
    # For each number up to sum(digits)
        # Left endpoint is index 0
        # Bisect cumulative sum to find right endpoint index closest to number
        # Use two pointer technique to find substring sum match
        # If found, set answer array value to left endpoint index
        # If not found, leave answer array value 0
    
    for x in range(1, s):
        l = 0
        r = bisect_left(runningSum, x)
        rs = runningSum[r]
        if x%10000000 == 0: print '{0}/{1}'.format(x, s)
        while r < len(digits):
            if rs == x:
                p[x] = l+1
                break
            if rs < x:
                r += 1
                if r < len(digits):
                    rs += digits[r]
            else:
                rs -= digits[l]
                l += 1
                
    return s,p

def solve(N):
    s,p = createAnswerArray()
                
    # Use answer array to calculate the total sum
    return (N // s)*sum(p) + sum(p[1:(N%s)+1])
    
    
if __name__ == '__main__':
    #print solve(1000)
    print solve(2*10**15)
    