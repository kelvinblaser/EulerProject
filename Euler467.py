def smallest_super(a, b, debug=False):
    if len(a) < len(b):
        a,b = b,a # a is now longest
        if len(b) == 0:
            return a
        val = a[len(a)/2]
        ix = 0
        left = a[:len(a)/2]
        right = a[len(a)/2+1:]
        
        sma_sup = a+b
        while ix <= len(b):  # For each slot
            temp = smallest_super(left,b[:ix])+[val,]
            if ix < len(b) and val == b[ix]:
                temp += smallest_super(right, b[ix+1:])
                ix += 2
            else:
                temp += smallest_super(right, b[ix:])
                ix += 1
            # Compare temp to sma_sup
            if compare_digit_list(temp, sma_sup):
                sma_sup = temp
    return sma_sup

def compare_digit_list(a,b):
    if len(a) < len(b):
        return True
    if len(a) > len(b):
        return False
    for ix in range(len(a)):
        if a[ix] < b[ix]:
            return True
        if a[ix] > b[ix]:
            return False
    return False
