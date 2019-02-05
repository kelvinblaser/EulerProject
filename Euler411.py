################################################################################
# Euler 411 - Uphill Paths
# Kelvin Blaser      2015.03.27
#
################################################################################
from collections import defaultdict

def S(n):
    stations = list(set([(pow(2,i,n),pow(3,i,n)) for i in range(0,2*n+1)]))
    print len(stations)
    stations.append((n,n))
    stations.sort()
    max_path = defaultdict(int)
    bot_stack = [(0,0,0)]

    max_len = 1

    while bot_stack:
        x,y,c = bot_stack.pop()
        #print x,y
        if c < max_path[(x,y)]:
            continue
        max_path[(x,y)] = c
        new_bots = ([(xn,yn,c+1) for xn,yn in stations
                     if xn >= x and yn >= y and not (xn==x and yn==y)])
        bot_stack.extend(new_bots[::-1])
        if len(bot_stack) > max_len:
            max_len = len(bot_stack)
            print max_len, max_path[(n,n)]-1

    return max_path[(n,n)]-1
                
    
