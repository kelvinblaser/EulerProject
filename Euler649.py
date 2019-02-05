# Euler 649

MOD = 10**9

def M(n,c):
    oneCoinGrundyDist = grundyDistribution(n)
    #print oneCoinGrundyDist
    grundyDist = xorScores(oneCoinGrundyDist, c)
    #print grundyDist
    return (pow(n*n,c,MOD) - grundyDist[0]) % MOD
    
def grundyDistribution(n):
    # Calculate one period of the grid
    grid = [[0 for x in range(9)] for y in range(9)]
    for x in range(9):
        for y in range(9):
            possible = set()
            if x >= 2: possible.add(grid[x-2][y])
            if x >= 3: possible.add(grid[x-3][y])
            if x >= 5: possible.add(grid[x-5][y])
            if x >= 7: possible.add(grid[x-7][y])
            if y >= 2: possible.add(grid[x][y-2])
            if y >= 3: possible.add(grid[x][y-3])
            if y >= 5: possible.add(grid[x][y-5])
            if y >= 7: possible.add(grid[x][y-7])
            grid[x][y] = mex(possible)
    # Calculate distributions for the period, and each row of the period
    rowDists = [[0 for x in range(8)] for row in range(9)]
    gridDist = [0 for x in range(8)]
    for row in range(9):
        for g in grid[row]:
            rowDists[row][g] += 1
            gridDist[g] += 1
    # Calculate the distribution for the entire grid
    periods = n//9
    dist = [periods**2 * gridDist[g] for g in range(8)] # The full periods
    for row in range(n%9): # Most of the leftover rows and columns
        for g in range(8):
            dist[g] += 2*periods*rowDists[row][g]
    for row in range(n%9): # The last small corner
        for col in range(n%9):
            dist[grid[row][col]] += 1
    return dist
    
def mex(scoreSet):
    l = list(scoreSet)
    l.sort()
    for x in range(len(l)):
        if x != l[x]:
            return x
    return len(l)
    
def xorScores(scoreDist, c):
    dist = [0 for x in range(len(scoreDist))]
    dist[0] = 1
    # Invariant - dist holds the distribution for _ coins
    for _ in range(c):
        newDist = [0 for s in range(8)]
        for x in range(len(scoreDist)):
            for y in range(len(dist)):
                newDist[x^y] += scoreDist[x] * dist[y]
                newDist[x^y] %= MOD
        dist = newDist
    return dist
    
if __name__ == '__main__':
    print 'M(3,1) =', M(3,1)
    print 'M(3,2) =', M(3,2)
    print 'M(9,3) =', M(9,3)
    print 'M(10 000 019, 100) =', M(1000019,100), 'MOD 10^9'