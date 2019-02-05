def calculateBinaryDigits(n):
    digits = []
    while n > 0:
        digits.append(n%2)
        n /= 2
    return digits

def allDigitsZero(digits):
    for d in digits:
        if d:
            return False
    return True

def G(n):
    digits = calculateBinaryDigits(n)
    base = 2
    summ = digits[0]
    base += digits[0]

    while not allDigitsZero(digits):
        index = 0
        while digits[index]==0:
            digits[index] = base
            index += 1
        digits[index] -= 1
        base += 1
        summ += 1
        summ += digits[0]
        base += digits[0]
        digits[0] = 0
    return summ
