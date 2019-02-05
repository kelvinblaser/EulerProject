# Euler 645

from collections import defaultdict

def cacheKeyFromSegments(segments):
    key = [(k, segments[k]) for k in segments if segments[k] > 0]
    key.sort()
    return tuple(key)
    
def E(n):
    if n < 3: return {}, 1.0
    cache = {}
    segments = {n-1 : 1}
    ans = 1.0 + _E(segments, n, cache)
    print ans, len(cache)
    return cache, ans
    
def copySegments(segments):
    newSegments = defaultdict(int)
    for m in segments:
        if segments[m] > 0:
            newSegments[m] = segments[m]
    return newSegments
    
def _E(segments, n, cache):
    key = cacheKeyFromSegments(segments)
    if len(key) == 1 and key[0][0] == 2:
        return EOnlyTwos(key[0][1], n)
        
    if key in cache:
        return cache[key]
        
    ans = float(n)
    for m in segments:
        if segments[m] == 0: continue
        if m > 3:
            for k in range(3,m-1):
                newSegments = copySegments(segments)
                newSegments[m] -= 1
                newSegments[k-1] += 1
                newSegments[m-k] += 1
                ans += segments[m] * _E(newSegments, n, cache)
            newSegments = copySegments(segments)
            newSegments[m] -= 1
            newSegments[m-2] += 1
            ans += 2.0 * segments[m] * _E(newSegments, n, cache)
        if m > 2:
            newSegments = copySegments(segments)
            newSegments[m] -= 1
            newSegments[m-1] += 1
            ans += 2.0 * segments[m] * _E(newSegments, n, cache)
        if m == 2:
            newSegments = copySegments(segments)
            newSegments[m] -= 1
            ans += 2.0 * segments[m] * _E(newSegments, n, cache)
    ans /= sum(m*segments[m] for m in segments)
    
    cache[key] = ans
    return ans
    
def EOnlyTwos(numTwos, n):
    ans = 0.0
    for k in range(1, numTwos+1):
        ans += 1.0 / (2.0*k)
    return n * ans