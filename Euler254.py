# Euler 254
# Kelvin Blaser
# 2019.01.31
#
# g(150) is a very large number.  Billions of digits.  I only need the sum of
# its digits, but how do I find them?
#
# There are many n which map to a particular f(n), and there are many f(n) which 
# map to a particular s(f(n)).  For a particular x, all the f(n) which map to x
# under s() are numbers whose digits make up a partition of x and the components
# of the partition are between 0 and 9.  For any particular x, there are infinite
# number of these, since trailing zeros can be allowed.  Fortunately, I can 
# ignore partitions that are too long.
#
# Given a candidate y, a greedy algorithm will give the smallest n for 
# which f(n) = y.  This is because n! divides (n+1)!, so it would never make
# sense to take mulitiple n's as digits when a single (n+1) would do.  Once
# the set of digits is known, the order is determined by placing the lowest
# digits in the highest power slots.
#
# So I search in the space of partitions of x for the candidates y such that 
# s(y) = x.  Then I use a greedy algorithm to find the least n such that 
# f(n) = y.  I find the smallest such n.  There are way too many partitions of 
# 150 to search directly.  Fortunately, there is a way to skip most of the 
# search space, since once I've found one candidate n, I can ignore partitions
# which are gauranteed to yeild larger n's.
#
# An example might be illuminating.
#
#  x = 5 has many partitions.  Here are a few of them.  Keep in mind that all
#  permutations of these partitions are also valid as long as they don't have 
#  a leading zero.
#
#   5 = 5
#   5 = 5+0
#   5 = 5+0+0
#   ...
#   5 = 4+1
#   5 = 4+1+0
#   5 = 4+0+1
#   ...
#   5 = 3+2
#   5 = 3+1+1
#   5 = 2+2+1
#   5 = 2+1+1+1
#   5 = 1+1+1+1+1
#
#  Lets consider the partition 5 = 1+4
#  This gives us candidate f(n) = y = 14
#  Greedy algorithm gives 14 = 3! + 3! + 2!  ==> n = 233
#  So I have a candidate solution for g(5) that has 3 digits.  Now consider
#  f(999), where I've replaced all 3 digits with 9's.  
#     f(999) = 3 x 9! = 3 x 362880 = 1088640. 
#  Any partition which yields a number larger than 1088640 is guaranteed to yield
#  an n with more than 3 digits.  I don't need to consider partitions with more
#  than 7 parts.  I've reduced the search space from infinite to finite size.
#  This may still seem like a large search space, but consider what it does for
#  g(150)
#
#  If x = 150, the smallest partition is 
#       x = 150 = 6 + (9 x 16)  => f(n) = y = 69,999,999,999,999,999
#  To get the smallest n, again use the greedy algorithm.
#       y = (192901234567 x 9!) + (8 x 8!) + (6 x 6!) + 5! +4! + (2 x 3!) + 2! + 1!
#  The digital representation of the smallest n is a 1 followed by a 2 followed
#  by two 3's followed by a 4 followed by a 5 followed by six 6's followed by 
#  eight 8's followed by 192,901,234,567 9's  for a total of 192,901,234,587
#  digits.  If all of those digits were 9's, y' would be 
#   y' = f(192,901,234,587 9's) = 192,901,234,587 x 9! = 70000000006930560.
#  So for x = 150, I only need to consider partitions of length 17 or less.
#  This keeps the search space manageable.
#
#  Once I've found the digital representation of g(i), calculating sg(i) is easy.

class Euler254:
    def __init__(self):
        #self.gVec = [[0]*(10) for x in range(150)]
        self.facts = [1]*(10)
        for x in range(2, 10):
            self.facts[x] = x * self.facts[x-1]
            
    def leastPartition(self, x):
        return [x%9] + [9]*(x//9)
        
    def partitionToInteger(self, partition):
        y = 0
        for d in partition:
            y *= 10
            y += d
        return y
        
    def candidateN(self, partInt):
        n = [0]*10
        for d in range(9,0,-1):
            n[d] = partInt // self.facts[d]
            partInt -= n[d]*self.facts[d]
        return n
        
    def candidateLess(self, n1, n2):
        digits1, digits2 = sum(n1), sum(n2)
        if digits1 != digits2:
            return digits1 < digits2
        for d in range(1,10):
            if n1[d] != n2[d]:
                return n1[d] > n2[d]
        return False
        
    def maxLengthFromCandidate(self, n):
        digits = sum(n)
        return len(str(digits*self.facts[9]))
        
    def candidateToStr(self, n):
        s = ''.join(str(d)*n[d] for d in range(1,9))
        if sum(n) <= 60:
            s += str(9)*n[9]
        else:
            s = '{0:37}'.format(s+'9') + ' ... ' + str(n[9]) +' 9\'s'
        return s
        
    def partitions(self, x, maxLength, first=True):
        if x == 0:
            return [[0]*i for i in range(maxLength+1)]
        if maxLength == 1:
            if x < 10:
                return [[x]]
            else:
                return None
                
        parts = []
        dMin = 1 if first else 0
        for d in range(min(x,9), dMin-1,-1):
            newParts = self.partitions(x-d, maxLength-1, False)
            if newParts is None: break
            for np in newParts:
                parts.append([d] + np)
        if len(parts) == 0:
            return None
        return parts
        
    def g(self, x):
        leastPartition = self.leastPartition(x)
        initialY = self.partitionToInteger(leastPartition)
        initialCandidate = self.candidateN(initialY)
        maxLength = self.maxLengthFromCandidate(initialCandidate)
        
        nMin = None
        for partition in self.partitions(x,maxLength):
            y = self.partitionToInteger(partition)
            n = self.candidateN(y)
            if nMin is None or self.candidateLess(n, nMin):
                nMin = n
        return nMin
        
    def sg(self, x):
        g = self.g(x)
        return g, sum(d*g[d] for d in range(1,10))
        
    def solve(self, talk=False):
        ans = 0
        for x in range(1,151):
            g, sg = self.sg(x)
            ans += sg
            if talk:
                gString = 'g({0}) = {1}'.format(x, self.candidateToStr(g))
                sgString = 'sg({0}) = {1:13}'.format(x, str(sg))
                print 'Sum = {2:13} | {1:23} | {0}'.format(gString, sgString, str(ans))
        return ans
            
            
if __name__ == '__main__':
    sol = Euler254()
    print 'Factorials:', sol.facts
    print 'Least partition: {0} = sum({1})'.format(47, sol.leastPartition(47))
    part = [3,5,2,1,6,7,0,7,5]
    print 'Partition to integer: {0} -> {1}'.format(part, sol.partitionToInteger(part))
    print 'Candidate from Integer: y = {0} => f({1}) = {0}'.format(5, sol.candidateN(5))
    n1 = [0,1,2,0,0,0,0,0,0,0,0]
    n2 = [0,2,2,0,0,0,0,0,0,0,0]
    n3 = [0,2,1,0,0,0,0,0,0,0,0]
    print 'Candidate compare: {0} < {1}? {2}'.format(n1, n2, sol.candidateLess(n1,n2))
    print 'Candidate compare: {0} < {1}? {2}'.format(n2, n1, sol.candidateLess(n2,n1))
    print 'Candidate compare: {0} < {1}? {2}'.format(n1, n3, sol.candidateLess(n1,n3))
    print 'Candidate compare: {0} < {1}? {2}'.format(n3, n1, sol.candidateLess(n3,n1))
    print 'Max Length: {0} => maxLength = {1}'.format(n1, sol.maxLengthFromCandidate(n1))
    print ''
    x = 5
    ml = 3
    print 'Partitions of {0} with maxLength {1}'.format(x, ml)
    print '------------------------------------'
    for part in sol.partitions(x,ml):
        print '  {0} = {1}'.format(x, '+'.join([str(d) for d in part]))
    print 'g(5) = {0}'.format(sol.g(5))
    print '\nsum(sg(x) for x = 1..150) = {0}'.format(sol.solve(True))
    
    