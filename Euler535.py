
def R(n,cache):
    #R(n) = sum( floor( sqrt( S(m)))) for m = 1..n
    try: return cache[n]
    except KeyError: pass
    
    j = find_j(n,cache)
    cache[n] = R(j,cache) + sum_sqrt(n-j)
    return cache[n]

def find_j(n, cache):
    top, bot = n,1
    while top - bot > 1:
        mid = (top+bot)/2
        if mid + R(mid, cache) > n:
            top = mid
        else:
            bot = mid
    return bot

def sum_sqrt(n):
    bot, top = 1,n
    while top-bot > 1:
        r = (top+bot)/2
        if r*r > n:
            top = r
        else:
            bot = r
    r = bot
    s = (r-1)*(2*r-1)*r/3 + (r-1)*r/2
    return s + r*(n-r*r+1)

def S(n, r_cache, s_cache):
    try: return s_cache[n]
    except KeyError: pass
    
    j = find_j(n,r_cache)
    if j + R(j, r_cache) < n:
        s_cache[n] = n-j
    else:
        s_cache[n] = S(j, r_cache, s_cache)
    return s_cache[n]

def T(n, r_cache, s_cache):
    if n <= 1:
        return n
    sn = S(n, r_cache, s_cache)
    if sn > n//2:
        return T(n-sn, r_cache, s_cache) + sn*(sn+1)/2
    else:
        return T(n-1, r_cache, s_cache) + sn

if __name__ == '__main__':
    r_cache = {1:1}
    s_cache = {1:1}
    for x in [1,20,1000, 10**9, 10**18]:
        print 'T(%d) = %d'%(x, T(x, r_cache, s_cache))


    

    
