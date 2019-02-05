# Euler 104 - Fibonacci Stuffs
import scipy as sp

def ExpSignificand(num, exp):
    if exp == 0:
        return 1.
    if exp == 1:
        return num
    num1 = ExpSignificand(num, int(exp/2))
    num1 *= num1
    if exp % 2 == 1:
        num1 *= num
    num1 /= 10.0**(int(sp.log10(num1)))
    return num1

def FibFirst9(n):
    phi = (1 + sp.sqrt(5))/2.
    fn = ExpSignificand(phi, n)
    fn /= sp.sqrt(5)
    if fn < 1:
        fn *= 10
    digits = []
    for x in range(9):
        digits.append(int(fn))
        fn -= int(fn)
        fn *= 10
    
    return digits

def getDigits(num):
    digits = []
    while num > 0:
        digits.append(num%10)
        num /= 10
    return digits
    

def isPanDigital(digitList):
    if len(digitList) != 9:
        return False

    digitList.sort()
    for n in range(9):
        if not digitList[n] == n+1:
            return False
    return True

def Euler104():
    n = 2
    fn1 = 1
    fn2 = 0
    while n < 1000000:
        fn = (fn1 + fn2) % 1000000000
        lastDigits = getDigits(fn)
        if isPanDigital(lastDigits):
            firstDigits = FibFirst9(n)
            if isPanDigital(firstDigits):
                return n
        fn2 = fn1
        fn1 = fn
        n += 1
    return 0

n = Euler104()
print n
