import scipy

def totientList(n):
    """
    Calculates a list of Euler Totients of the integers from 0 to n
    """
    totient = range(0,n+1)
    totient[0] = 0L
    totient[1] = 0L
    for x in range(2,n+1):
        if x == totient[x]:
            j = x
            while j <= n:
                totient[j] *= (x-1)
                totient[j] /= x
                j += x

    return totient
