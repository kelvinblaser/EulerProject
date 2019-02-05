# Euler 331
# Kelvin Blaser  	2019.01.15
#
#  The math of the solution
#
# Let a single move consist of choosing a square on the board and flipping
# each disk in the row and column as that square.
#
# 1. All moves are commutative.  
# 2. Each move is its own inverse.
#
# Together, these mean we can work with sets of moves, rather than sequences of 
# moves.  The set of sets of moves has size 2^(N^2) for an NxN board.  The 
# action of those sets of moves on the board constitues a function from sets of
# moves to final board configuration.  There can be at most 2^(N^2) such final
# configurations, so if we can show that if every configuration is reachable,
# the function is bijective and the solution set of moves is unique.
#
# Odd N
#   Consider the number of black disks in each row and their repsective parities.
#   A move will change one disk in each of (N-1) rows and N discs in the 
#   remaining row.  But N is odd, so any move changes the parity of the row
#   counts in every row.  Any configuration that is reachable must have all row
#   counts odd or all row counts even.  Even then, I'm not sure if every 
#   configuation with uniform row parities is reachable, and if it is, how to 
#   find its minimal solution.  Luckily, for every odd N under consideration
#   except for N=5, there is at least one row with two black disks and one row
#   with one black disk.  Thus the boards are unreachable.  
#
#   We remove the odd
#   N from consideration and remember to add 3 to the total for T(5) (Solution
#   given in the problem statement)
#
# Even N
#   Consider the set of moves which consists of every cell in a row and every 
#   cell in a column. Disks outside of that row and outside that column will be
#   flipped twice, for no change.  Disks in the row but not in the column and
#   vice-versa will be fliped N=2k times, for no change.  The cell in the row
#   and in the column will be flipped 2N-1 times, and changes.  Thus this set of
#   moves has the net effect of flipping a single disk and leaving the rest
#   unchanged.
#
#   This means that every configuration is reachable, and the solution set is 
#   unique.  Furthermore, we have a very expensive algorithm for finding it.
#   Can we speed up the algorithm?
#
#   The number of times we use the move for a particular cell is just the sum
#   of the number of black disks in its row and the number of black disks in its
#   column.  Then subtract 1 if the cell itself is a black disc, since it got 
#   added in twice.  We only need to know the parity though, so we keep track
#   of which rows have an even number of black discs and which have an odd.  
#   Because of the symmetry, the columns are the same as the rows. 
#
#   Suppose there are 'e' even rows and 'o' odd rows.  Every even row intersects
#   'o' columns and every odd row intersects 'e' even columns.  So there are a 
#   total of 2*e*o discs whose rowSum and columnSum add to an odd number.  Most 
#   of these are white discs, so we start there.  Then we correct for each black
#   disk by adding 1 if its rowSum + columnSum is even, and subtract 1 if its
#   rowSum + columnSum is odd.
#
#   The tricky part is doing this without keeping a vector of 1 billion ints or 
#   bools when calculating T(2^30-30)


import sys
import time
import datetime

def makeBoardMedium(N):
    board = [[' ' for x in range(N)] for y in range(N)]
    for x,y in blackDiskGen(N):
        board[x][y] = 'O'
    return [''.join(row) for row in board]

def makeBoard(N):
    board = [[' ' for x in range(N)] for y in range(N)]
    for x in range(N):
        for y in range(N):
            if (N-1)**2 <= x*x + y*y < N**2:
                board[x][y] = 'O'
    return [''.join(row) for row in board]
    
def solveSlow(N):
    board = makeBoard(N)
    rowCounts = [sum(1 for c in row if c == 'O') for row in board]
    evens = sum(1 for count in rowCounts if count%2 == 0)
    odds = N - evens
    ans = 2 * odds * evens
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'O':
                if (rowCounts[i] + rowCounts[j]) % 2 == 0:
                    ans += 1
                else:
                    ans -= 1
    return ans
    
def blackDiskGen(N):
    N12 = (N-1)**2
    N2 = N**2
    point = [0,N-1]
    while point[0] < N:
        x,y = point
        yield x,y
        if x < N and N12 <= (x+1)**2 + y**2 < N2:
            point[0] += 1
        elif y > 0 and N12 <= x**2 + (y-1)**2 < N2:
            point[1] -= 1
        elif y > 0 and x < N and N12 <= (x+1)**2 + (y-1)**2 < N2:
            point[0] += 1
            point[1] -= 1
        else:
            point[0] = N
    
def solveMedium(N):
    rowCounts = [0 for _ in range(N)]
    for x,y in blackDiskGen(N):
        rowCounts[x] += 1
    evens = sum(1 for count in rowCounts if count%2 == 0)
    odds = N - evens
    ans = 2 * odds * evens
    print odds, evens
    for x,y in blackDiskGen(N):
        if (rowCounts[x] + rowCounts[y]) % 2 == 0:
            ans += 1
        else:
            ans -= 1
    return ans
    
def intRoot(x):
    r = int(x**0.5)
    while r*r > x:
        r -= 1
    while (r+1)*(r+1) <= x:
        r += 1
    return r
    
def diskRowGen(N):
    y = N-1
    xStart, xEnd = 0, 0
    while y > xEnd:
        xStart = xEnd
        if xStart*xStart + y*y < (N-1)**2: xStart += 1
        xEnd = intRoot(N*N - y*y) 
        if xEnd*xEnd == N*N - y*y: xEnd -= 1
        yield (xStart, xEnd, y)
        y -= 1
        
def solveFast(N):
    evens = 0
    last = -1
    lastCount = 0
    ans = 1     # We ge an extra -1 by pretending there is a black disk at (-1,N).  
                # Correct for it by starting at 1 instead of 0
    for xs, xe, y in diskRowGen(N):
        # Process row and all points except the one at xe and at xs
        rowSize = xe-xs+1
        if rowSize%2 == 0: 
            evens += 1
            ans -= rowSize-2
        else:
            ans += rowSize-2
        
        # Process the last column of the last row
        # Process the last point of the last row
        # Process first point of this row
        lastPointVal = pow(-1, lastCount)
        firstPointVal = pow(-1, rowSize)
        if xs == last: 
            evens += 1
            ans += lastPointVal + firstPointVal
        else:
            ans -= lastPointVal + firstPointVal
            
        # Update last values
        last = xe
        lastCount = rowSize
    # Process the last column and last point of the last row
    # as well as first column of the next row if applicable
    if xe == y:
        # Case:
        #  'OO'  or  ' O'
        #  ' O'      '  '
        ans *= 2
        ans += 1
    else:
        if (N-1)**2 <= xe*xe + (y-1)**2 < N*N:
            # Case:
            #  'O '
            #  'OO'
            evens += 1
            if lastCount % 2 == 0:
                ans += 1
            else:
                ans -= 1
            ans *= 2
            ans += 1
        else:
            # Case:
            #  'O '
            #  ' O'
            if lastCount % 2 == 0:
                ans -= 1
            else:
                ans += 1
            ans *= 2
            
    ans += 2*evens*(N-evens)
    return ans

if __name__ == '__main__':
    print 'T(10) =', solveFast(10)
    print 'T(1000) =', solveFast(1000)
    print ''
    print 'Started at -', datetime.datetime.now()
    s = 3
    valsStr = ' '*11 + 'Values'
    sumStr = '   Sum'
    timeStr = ' Time Taken'
    print '{0:35} | {1:20} | {2}'.format(valsStr, sumStr, timeStr)
    print '-'*80
    start = time.clock()
    for i in range(4,31,2):
        n = pow(2,i) - i
        t = solveFast(n)
        s += t
        Tstr = 'T(2^{0} - {0}) = {1}'.format(i,t)
        print '{0:35} | {1:20} | {2} s'.format(Tstr, str(s), time.clock()-start)
        sys.stdout.flush()
    end = time.clock()
    print '-'*80
    print ''
    print 'Sum =', s
    print 'Finished at -', datetime.datetime.now()
    print 'Took', end - start, 'seconds'
        