# Euler 161 - Triominoes
import scipy as sp

def make_filling_list(r, c):
    tiles = []
    # L shaped tiles
    for i in range(r-1):
        for j in range(c-1):
            t1 = sp.zeros(r*c, dtype=int)
            t2 = sp.zeros(r*c, dtype=int)
            t3 = sp.zeros(r*c, dtype=int)
            t4 = sp.zeros(r*c, dtype=int)
            t1[i*c + j + 1]     = 1
            t1[(i+1)*c + j]     = 1
            t1[(i+1)*c + j + 1] = 1
            t2[i*c + j]         = 1
            t2[(i+1)*c + j]     = 1
            t2[(i+1)*c + j + 1] = 1
            t3[i*c + j]         = 1
            t3[i*c + j + 1]     = 1
            t3[(i+1)*c + j]     = 1
            t4[i*c + j]         = 1
            t4[i*c + j + 1]     = 1
            t4[(i+1)*c + j + 1] = 1
            tiles.append(tuple(t1))
            tiles.append(tuple(t2))
            tiles.append(tuple(t3))
            tiles.append(tuple(t4))

    # Vertical bars
    for i in range(r-2):
        for j in range(c):
            t = sp.zeros(r*c, dtype=int)
            t[i*c+j]     = 1
            t[(i+1)*c+j] = 1
            t[(i+2)*c+j] = 1
            tiles.append(tuple(t))

    # Horizontal Bars
    for i in range(r):
        for j in range(c-2):
            t = sp.zeros(r*c, dtype=int)
            t[i*c+j]   = 1
            t[i*c+j+1] = 1
            t[i*c+j+2] = 1
            tiles.append(tuple(t))

    tiles.sort()
    tiles.reverse()
    return sp.array(tiles)
            
def tiling_ways(tiles, memo, level = 0):
    #print ' '*level, tiles.shape
    key = []
    for t in tiles:
        key.append(tuple(t))
    key = tuple(key)
    if key in memo:
        return memo[key]
    
    s = 0
    while len(tiles) > 0:
        col_sum = sum(tiles, 0)
        if any(col_sum == 0):
            memo[key] = s
            return s
        if all(col_sum == 1):
            memo[key] = s+1
            return s+1

        new_tiles = []
        for t in tiles:
            if any(sp.logical_and(tiles[0], t)):
                continue
            new_tiles.append(t)
        if not new_tiles:
            tiles = tiles[1:,:]
            continue
        new_tiles = sp.array(new_tiles)
        next_tiles = []
        for b in range(len(tiles[0])):
            if tiles[0,b]:
                continue
            next_tiles.append(new_tiles[:,b])
        next_tiles = sp.array(next_tiles).transpose()
        new_tiles = []
        for t in next_tiles:
            new_tiles.append(tuple(t))
        new_tiles.sort()
        new_tiles.reverse()

        s += tiling_ways(sp.array(new_tiles), memo, level+1)

        tiles = tiles[1:,:]
        
    memo[key] = s
    return s
        
def Euler161(r,c):
    if r*c%3 != 0:
        return 0
    tiles = make_filling_list(r,c)
    memo = {}
    return tiling_ways(tiles, memo)
