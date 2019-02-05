# Euler 328 - Lowest-cost Search
# Kelvin Blaser		2019.01.28
#
#  I have a good brute-ish force algo.  Searching any interval from lo to hi
#  has an optimal choice.  So I calculate and store the optimal cost for each
#  interval.  There are ~ hi - lo = O(N) choices for each interval, with N*(N-1)
#  intervals.  This results in O(N^3) time and O(N^2) space complexity
#  N = 200000 is much too high for this algorithm, but N = 500 or 600 is doable
#
#  How to speed it up?  
#
#  I know a bit about what the search tree looks like. The leaves are N-1, N-5, 
#  N-9, etc. plus a 1 or 2 if needed on the left.  The rest of the nodes are 
#  N-3, N-7, N-11, etc. If the root node is x, the left tree is exactly the 
#  optimal search tree for x-1, so its cost should already be calculated.  I need
#  a fast way to build the optimal tree for x+1 .. N, so that I can find the 
#  optimal x quickly
#
#  My hunch that the optimal right tree is always a complete binary tree with 
#  2^k - 1 nodes was incorrect.  124 is the first N to show this.  It has an
#  optimal first choice of 105, with the search tree for the interval 106..124 
#  containing 9 = (2^3-1) + 2 nodes.
#
#  I have a new hunch that the right search tree is a complete binary tree.  I
#  can't prove it, but if so, calculating the optimal cost of the right tree
#  might be pretty easy for each trial first choice.  I can test this for the 
#  first 500 to 1000 or so trees, which I can build from the bruteChoice function
#
#  This holds true for x <= 800.  Since the optimal first choice is always >= N/2,
#  Two extra layers in the right search tree would add more than N to the optimal
#  right tree cost over the cost of the largest complete layer, while only one 
#  extra layer cannot add more than N to the optimal right tree cost.  Not sure
#  if that constitutes a proof.
#
#  So here is the solution strategy:
#    1. Assume that the optimal worst case search cost is known for 1 <= x <= N-1
#       This function is non-decreasing in x.  Call it C(x)
#    2. Calculating the optimal complete binary tree cost for N/2 <= x <= N-1
#       is not difficult.  This function is non-increasing in x. Call it B(x,N)
#    3. Find the lowest x where C(x-1) >= B(x+1,N)
#    4. The optimal strategy will be around x, since the total cost includes adding
#       x.  May need to search up one value of x and down a few values of x to
#       find the global minimum.
#
#
# =======================================================================
#
#  Binary search method is bust because right tree cost is not non-increasing.  
#  However, I can see that n-firstChoice is non-decreasing, and only ever 
#  increases by a power of 2.  So that limits the number of firstChoices I need 
#  to test by a lot.  The right sub-tree still has to be complete.
#
#  Why does the difference only increase by powers of 2?  I don't know really.
#  But it do.
#
# ========================================================================

import EulerUnitTest as eut
from Queue import Queue

class TreeNode:
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None
        self.cost = n

class Euler328:
    def __init__(self, talk=False):
        self.bruteCostMemo = {}
        self.choiceMemo = {}
        self.C = [-1] * 200001
        self.C[:4] = [0,0,1,2]
        self.firstChoice = [-1] * 200001
        self._binaryCostMethodCalled = 0
        self._talk = talk
        
    def _bruteCost(self, lo, hi):
        minCost = hi*(hi+1) # This is larger than the cost of any strategy
        minChoice = -1
        for x in range(hi-1, lo, -1):
            rightCost = self.bruteCost(x+1, hi)
            leftCost = self.bruteCost(lo, x-1)
            c = x + max(leftCost,rightCost)
            if c < minCost:
                minCost = c
                minChoice = x
        self.bruteCostMemo[(lo,hi)] = minCost
        self.choiceMemo[(lo,hi)] = minChoice
        return (minCost, minChoice)
        
    def bruteCost(self, lo, hi):
        if hi <= lo: return 0
        if hi-lo <= 2:
            self.choiceMemo[(lo, hi)] = hi - 1 
            return hi - 1
        if (lo, hi) in self.bruteCostMemo: return self.bruteCostMemo[(lo,hi)]
        minCost, minChoice = self._bruteCost(lo, hi)
        #print 'In Cost(): lo =', lo, ': hi =', hi, ': minCost =', minCost, ': minChoice =', minChoice
        #if lo == 1: self.C[hi] = minCost
        return minCost
        
    def bruteChoice(self, lo, hi):
        if hi <= lo: return None
        if hi-lo == 1: return lo
        if hi-lo == 2: return lo+1
        if (lo,hi) in self.choiceMemo: return self.choiceMemo[(lo,hi)]
        minCost, minChoice = self._bruteCost(lo, hi)
        return minChoice
        
    def bruteSum(self, n):
        return sum(self.bruteCost(1,x) for x in range(1, n+1))
        
    def buildTree(self, lo, hi):
        choice = self.bruteChoice(lo,hi)
        if choice is None: return None
        node = TreeNode(choice)
        node.left = self.buildTree(lo, choice-1)
        node.right = self.buildTree(choice+1, hi)
        return node
        
    def isTreeComplete(self, tree):
        # In order traversal to see if tree is complete binary tree
        q = Queue()
        q.put(tree)
        while not q.empty():
            node = q.get()
            if node is None:
                # Found a None, tree is complete iff everything else in the
                # queue is also a None
                while not q.empty():
                    if q.get() is not None: return False
            else:
                q.put(node.left)
                q.put(node.right)
        return True
        
    def costSum(self, n):
        return sum(self.cost(x) for x in range(1, n+1))
        
    def cost(self, n):
        if n < 0: return 0
        if self.C[n] != -1: return self.C[n]
        if n <= 40: 
            self.C[n] = self.bruteCost(1,n)
            self.firstChoice[n] = self.bruteChoice(1,n)
            return self.C[n]
        
        if self._talk and n%1000 == 0:
            print 'Calculating cost at', n
        
        if self.firstChoice[n-1] == -1: self.cost(n-1)
        diff = n - 1 - self.firstChoice[n-1]
        f = n - diff
        minCost = f + max(self.cost(f-1), self.completeBinaryCost(n, f))
        minFirst = f
        pow2 = 4
        while n-diff-pow2 > n//2:
            f = n - diff - pow2
            c = f + max(self.cost(f-1), self.completeBinaryCost(n, f))
            if c < minCost:
                minCost = c
                minFirst = f
            pow2 *= 2
        self.firstChoice[n] = minFirst
        self.C[n] = minCost
        return minCost
        
        ## Binary search to find the point where the right tree and left tree
        ## costs are equal
        #m = (n+1)%8
        #bot = n%8 + 1
        #top = n-7
        #while top - bot > 8:
        #    mid = 8*(((bot-m)//8 + (top-m)//8) // 2) + m
        #    if self.cost(mid-1) > self.completeBinaryCost(n, mid):
        #        top = mid
        #    else:
        #        bot = mid
        ## For every first choice <= bot, the right tree dominates
        ## For every first choice >= top, the left tree dominates
        ## Might be able to lower the cost of first choice bot, if
        ##   right tree cost grows slower than bot decreases <- right tree cost doesn't even grow sometimes.  bleh
        #while bot - 8 + self.completeBinaryCost(n,bot-8) <= bot + self.completeBinaryCost(n,bot):
        #    bot -= 8
        #    ## This part is incorrect.  The first minimum from the right is not 
        #    ## necessarily the global minimum, like I thought
        #    
        #if n == 936:
        #    print 'bot', bot
        #    print 'top', top
        #self.C[n] = min([x + max(self.C[x-1], self.completeBinaryCost(n,x)) for x in range(bot, top+5, 4)])
        #return self.C[n]
        
    def completeBinaryCost(self, n, firstChoice):
        self._binaryCostMethodCalled += 1
        numNodes = (n - firstChoice) // 2
        if numNodes == 1: return n-1
        topNodes = 0
        nextRow = 1
        while topNodes + nextRow <= numNodes:
            topNodes += nextRow
            nextRow *= 2
        bottomNodes = numNodes - topNodes
        topVal = n - 2*(topNodes // 2 + max(0, bottomNodes - nextRow//2)) - 1
        if bottomNodes == 0 or bottomNodes > nextRow//2:
            return topVal + self.completeBinaryCost(n, topVal)
        else:
            return topVal + max(self.completeBinaryCost(n, topVal), self.completeBinaryCost(topVal-1, firstChoice))
        
            
            

        
def printTree(tree):
    for line in treeLines(tree)[0]:
        print line
def treeLines(tree):
    if tree is None: return None, None
    valStr = str(tree.val)
    if tree.left is None and tree.right is None: return [valStr], len(valStr) // 2
    
    leftLines, leftRoot = treeLines(tree.left)
    leftWidth = 0 if leftLines is None else len(leftLines[0])
    rightLines, rightRoot = treeLines(tree.right)
    rightWidth = 0 if rightLines is None else len(rightLines[0])
    lines = []
    if tree.left is None:
        lines = rightLines
    elif tree.right is None:
        lines = leftLines
    else:
        rightRoot += leftWidth + 1
        for ix, ll in enumerate(leftLines):
            if ix < len(rightLines):
                lines.append(ll + ' ' + rightLines[ix])
            else:
                lines.append(ll + ' '*(rightWidth + 1))
        for ix in range(len(leftLines), len(rightLines)):
            lines.append(' '*(leftWidth+1) + rightLines[ix])
            
    # Build the top string with the root node
    rootIx = len(valStr)//2
    topString = valStr
    if rootIx > leftWidth:
        # pad every string on the left
        lines = [' '*(rootIx - leftWidth) + l for l in lines]
        leftRoot += rootIx - leftWidth
        rightRoot += rootIx - leftWidth
    else:
        # pad the top String
        topString = ' '*(leftWidth-rootIx) + valStr
        rootIx = leftWidth
    if len(topString) > len(lines[0]):
        # pad every string on the right
        offset = len(topString) - len(lines[0])
        lines = [l + ' '*offset for l in lines]
    else:
        # pad the top string
        topString += ' '*(len(lines[0]) - len(topString))
        
    # Build the links from root to children
    linkStr = ' '
    if tree.left is not None:
        linkStr = '/' + linkStr
        underScores = max(0, rootIx - 2 - leftRoot)
        linkStr = ' '*(rootIx-1-underScores) + '_'*underScores + linkStr
    if tree.right is not None:
        linkStr += '\\'
        underScores = max(0, rightRoot-rootIx - 2)
        linkStr += '_'*underScores
        linkStr += ' '*(len(topString) - len(linkStr))
        
    lines = [topString, linkStr] + lines
    return lines, rootIx 
        
        
if __name__ == '__main__':
    sol = Euler328()
    print '  Brute Force Methods  '
    print '-----------------------'
    print 'C(1) =', eut.testAssert(sol.bruteCost,0, 1,1)       # Should be 0
    print 'C(2) =', eut.testAssert(sol.bruteCost,1, 1,2)       # Should be 1
    print 'C(3) =', eut.testAssert(sol.bruteCost,2, 1,3)       # Should be 2
    print 'C(8) =', eut.testAssert(sol.bruteCost,12, 1,8)      # Should be 12
    print 'C(100) =', eut.testAssert(sol.bruteCost,400, 1,100) # Should be 400
    #print 'C(124) =', eut.testAssert(sol.bruteCost,555, 1,124) # Should be 555
    #print 'S(100) =', eut.testAssert(sol.bruteSum,17575, 100)  # Should be 17575
    #print 'S(200) =', eut.testAssert(sol.bruteSum,86342, 200)  # Should be 86342
    
    print ''
    print '  Search Tree From Brute Force  '
    print '--------------------------------'
    root = sol.buildTree(1,12)
    print 'Tree for n = 12'
    printTree(root)
    print ''
    print 'Tree for n = 100'
    tree = sol.buildTree(1,100)
    printTree(tree)
    print 'Tree for n = 125'
    tree = sol.buildTree(1,125)
    printTree(tree)
    print ''
    print '  Check Trees for completeness  '
    print '--------------------------------'
    print 'Completeness of search tree for n = 12', sol.isTreeComplete(root)
    print 'Completeness of search tree for n = 100', sol.isTreeComplete(tree)
    print 'Completeness of right sub tree for n = 100', sol.isTreeComplete(tree.right)
    incompleteRightTrees = [x for x in range(3,201) if not sol.isTreeComplete(sol.buildTree(sol.bruteChoice(1,x)+1,x))]
    print 'Search trees with incomplete right subtrees for x <= 200'
    print incompleteRightTrees
    print ''
    print '  Fast Search Methods  '
    print '-------------------------'
    sol = Euler328(talk = False)
    print 'C(1) =', eut.testAssert(sol.cost,0, 1)       # Should be 0
    print 'C(2) =', eut.testAssert(sol.cost,1, 2)       # Should be 1
    print 'C(3) =', eut.testAssert(sol.cost,2, 3)       # Should be 2
    print 'C(8) =', eut.testAssert(sol.cost,12, 8)      # Should be 12
    print 'C(100) =', eut.testAssert(sol.cost,400, 100) # Should be 400
    print 'C(124) =', eut.testAssert(sol.cost,555, 124) # Should be 555
    print 'S(100) =', eut.testAssert(sol.costSum,17575, 100)  # Should be 17575
    print 'S(200) =', eut.testAssert(sol.costSum,86342, 200)  # Should be 86342
    print 'S(10000) = {0}'.format(sol.costSum(10000))
    print 'S(200000) = {0}'.format(sol.costSum(200000))
    print ''
    print 'Diagnostics'
    print 'completeBinaryCost() called {0} times'.format(sol._binaryCostMethodCalled)