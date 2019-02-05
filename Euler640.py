# Euler 640
# Kelvin Blaser		2019.01.28
#
# Pretty simple dynamic programing / iterative relaxation
# 

def expectedTurns(numCards, diceSides, eps=1e-9):
    states = 2**numCards
    diceProb = 1.0 / (diceSides * diceSides)
    expected = [0.0]*states
    numTraversals = 0
    changed = True
    while changed:
        for n in range(1, states):
            prevExpected = expected[n]
            newExpected = 1.0
            for x in range(1, diceSides+1):
                for y in range(1, diceSides+1):
                    newExpected += diceProb * min(expected[n^(1 << (x-1))], expected[n^(1 << (y-1))], expected[n^(1 << (x+y-1))])
            expected[n] = newExpected
            changed = abs(newExpected - prevExpected) > eps
        if numTraversals % 10 == 0:
            print diceSides, numTraversals, expected[-1], abs(newExpected - prevExpected)
        numTraversals += 1
        
    return expected, numTraversals
    
if __name__ == '__main__':
    expected = {}
    n = {}
    for x in range(2, 8):
        e, nn = expectedTurns(2*x, x)
        expected[x] = e
        n[x] = nn
    print ''
    print '------------------------------------------------------------------------------------'
    print ' 4 cards and 2 sided coins : Expect {0:9.6f} turns calculated over {1:3d} iterations'.format(round(expected[2][-1], 6), n[2])
    for x in range(3, 8):
        print '{2:2d} cards and {3} sided dice  : Expect {0:9.6f} turns calculated over {1:3d} iterations'.format(round(expected[x][-1], 6), n[x], 2*x, x)
    print '------------------------------------------------------------------------------------'