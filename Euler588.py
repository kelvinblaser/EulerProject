#------------------------------------------------------
# Euler 588
# 
# For theory see:
# https://pdfs.semanticscholar.org/68cd/9b758a764a27a45175cf74a36c4b299d0fd5.pdf
# 'Odd Entries in Pascal's Trinomial Triangle' - Steven Finch, Pascal Sebah, Zai-Qiao Bai
#-----------------------------------------------------

def Q(x, cache):
    if x == 0:
        return 1
    try:
        return cache[x]
    except KeyError:
        pass
        
    if x%2 == 0:
        n = x
        while n%2 == 0:
            n //= 2
        ans = Q(n, cache)
    elif x%8 == 1:
        ans = 5*Q((x-1)//8, cache)
    elif x%8 == 3:
        n = (x-3)//8
        ans = 2*Q(4*n+1, cache) - 3*Q(n, cache)
    elif x%8 == 5:
        n = (x-5)//8
        ans = 3*Q(2*n+1, cache) + 2*Q(n, cache)
    elif x%8 == 7:
        n = (x-7)//8
        ans = 3*Q(2*n+1, cache) + 2*Q(4*n+1, cache) - 6*Q(n, cache)
    cache[x] = ans
    return ans

if __name__ == '__main__':
    s = 0
    cache = {}
    for k in range(1, 19):
        q = Q(10**k, cache)
        s += q
        print 'Q(10^{0}) = {1}'.format(k, q)
    print 'Sum : {0}'.format(s)
    print 'Cached Values : {0}'.format(len(cache))