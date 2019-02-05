# Euler 260

def intKey(x,y,z,N):
    l = [x,y,z]
    l.sort()
    x,y,z = l
    return z + N*(y + N*x)

def stoneSum(N):
    s = 0
    pStates = {}
    pCount = 0
    for z in range(N+1):
        for y in range(z+1):
            for x in range(y+1):
                try:
                    p = pStates[intKey(x,y,z,N)]
                except KeyError:
                    # We have a p state
                    s += x + y + z
                    pCount += 1
                    for k in range(1, N-z+1):
                        pStates[intKey(x,y,z+k,N)] = None
                        pStates[intKey(x,y+k,z+k,N)] = None
                        pStates[intKey(x+k,y+k,z+k,N)] = None
                        pStates[intKey(x+k,y,z+k,N)] = None
                    for k in range(1,N-y+1):
                        pStates[intKey(x,y+k,z,N)] = None
                        pStates[intKey(x+k,y+k,z,N)] = None
                    for k in range(1,N-x+1):
                        pStates[intKey(x+k,y,z,N)] = None
        if z%20 == 0:
            print z, len(pStates), pCount, s
    print len(pStates)