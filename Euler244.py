# Euler 244 - Sliders
#
# Create a SliderBoard class that can hash.  Hash is 20 bits.  First 16 bits
# tell us where the blue squares are.  There should be eight 1's and eight 0's
# Last 4 bits tell us where the empty square is.  It should correspond to one of
# the zeros in the first 16 bits.  Hash takes 2^20 = 1048576 values, but only 
# 16! / (8! 7! 1!) = 102960 of them are valid boards
#
# SliderBoard should also be able to calculate all the possible moves to new 
# slider boards.  Method should return the hash value of the next slider board
# along with the corresponding move 'L','U','R','D'.

# Dynamic programming on moves.  Keep track of number of paths, along with
# sum of check sums of the paths to the board.  Initialize sum of check sums to 
# -1. Once the sum of check sums of the end state board is no longer -1, return
# the sum of check sums

from collections import defaultdict

class SliderBoardCalculator:
    def hashToBoard(self, boardHash):
        bluesPart = boardHash // 16
        emptyPart = boardHash % 16
        
        board = [['r' for x in range(4)] for y in range(4)]
        
        sq = 15
        numBlue = 0
        while bluesPart > 0:
            if bluesPart % 2 == 1:
                numBlue += 1
                if sq == emptyPart: return None
                board[sq // 4][sq%4] = 'b'
            bluesPart //= 2
            sq -= 1
        if numBlue != 8: return None
            
        board[emptyPart // 4][emptyPart % 4] = 'e'
        
        return board
        
        
    def boardToHash(self, board):
        bluesPart = 0
        emptyPart = 0
        
        for x in range(4):
            for y in range(4):
                bluesPart *= 2
                if board[x][y] == 'b':
                    bluesPart += 1
                if board[x][y] == 'e':
                    emptyPart = x*4+y
        return bluesPart*16 + emptyPart
        
    def getMoves(self, boardHash):
        board = self.hashToBoard(boardHash)
        emptyPart = boardHash % 16
        x,y = emptyPart // 4, emptyPart % 4
        moves = set()
        if x > 0: 
            nb = [[c for c in row] for row in board]
            nb[x][y], nb[x-1][y] = nb[x-1][y], nb[x][y]
            moves.add(('D', self.boardToHash(nb)))
        if x < 3: 
            nb = [[c for c in row] for row in board]
            nb[x][y], nb[x+1][y] = nb[x+1][y], nb[x][y]
            moves.add(('U', self.boardToHash(nb)))
        if y > 0: 
            nb = [[c for c in row] for row in board]
            nb[x][y], nb[x][y-1] = nb[x][y-1], nb[x][y]
            moves.add(('R', self.boardToHash(nb)))
        if y < 3:
            nb = [[c for c in row] for row in board]
            nb[x][y], nb[x][y+1] = nb[x][y+1], nb[x][y]
            moves.add(('L', self.boardToHash(nb)))
        return moves
    
    def isValidHash(self, boardHash):
        if self.hashToBoard(boardHash) is None:
            return False
        return True
        
def Euler244():
    startBoard = [['e','r','b','b'],['r','r','b','b'],['r','r','b','b'],['r','r','b','b']]
    endBoard = [['e','b','r','b'],['b','r','b','r'],['r','b','r','b'],['b','r','b','r']]
    
    sbc = SliderBoardCalculator()
    startHash = sbc.boardToHash(startBoard)
    endHash = sbc.boardToHash(endBoard)
    
    validHashes = [x for x in range(2**20) if sbc.isValidHash(x)]
    print len(validHashes)
    
    pathLen = 0
    numPaths = defaultdict(int)
    numPaths[startHash] = 1
    sumCheckSum = defaultdict(int)
    while numPaths[endHash] == 0:
        newNumPaths = defaultdict(int)
        newSumCheckSum = defaultdict(int)
        for k in validHashes:
            if numPaths[k] != 0:
                for c, h in sbc.getMoves(k):
                    newNumPaths[h] += numPaths[k]
                    newSumCheckSum[h] += 243*sumCheckSum[k] + numPaths[k]*ord(c)
                    newSumCheckSum[h] %= 100000007
        numPaths = newNumPaths
        sumCheckSum = newSumCheckSum
        pathLen += 1
        print pathLen, len(numPaths)
        
    print numPaths[endHash], sumCheckSum[endHash]
        
    return sumCheckSum[endHash]
    
if __name__ == '__main__':
    Euler244()
    
    