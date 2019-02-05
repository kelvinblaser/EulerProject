# Euler 253
# 2019.1.31
#
# Dynamic programming getting the full distribution
#
# Takes about 15 min

import time

class Caterpillar:
    def __init__(self, L, talk=False):
        self.L = L
        self.cache = {}
        self.talk = talk
        
    def bitNot(self, n):
        L = self.L
        return ((1 << L) - 1) - n
        
    def standardize(self, n):
        L = self.L
        leftGap, rightGap = 0, L
        notN = self.bitNot(n)
        while notN & (1 << leftGap):
            leftGap += 1
        while notN & (1 << (rightGap-1)) and rightGap > leftGap:
            rightGap -= 1
        if rightGap == leftGap: return n, 0
        
        gaps = []
        ix = leftGap
        while ix < rightGap:
            bar = 0
            while n & (1 << ix) and ix < rightGap:
                bar += 1
                ix += 1
            if ix == rightGap: break
            g = 0
            while notN & (1 << ix):
                g += 1
                ix += 1
            gaps.append(g)
        gaps.sort()
        
        x = 0
        # Standardize the ends
        leftGap, rightGap = min(leftGap, L-rightGap), L-max(leftGap, L-rightGap)
        # Place the interior gaps
        ix = leftGap
        for g in gaps:
            x += (1 << ix)
            ix += g+1
        # Fill in the rest of the interior
        while ix < rightGap:
            x += (1 << ix)
            ix += 1
        return x, len(gaps)+1
        
    def calcDistribution(self, state, maxBars):
        # Precondition: state is standardized and maxBars >= the # of bars in state
        ans = [0]*((self.L+1)//2 + 1)
        if state == (1 << self.L)-1: 
            ans[maxBars] += 1
            return ans
        if (state, maxBars) in self.cache:
            return self.cache[(state, maxBars)]
            
        if state == 0:
            fullStart = time.clock()
            
        for ix in range(self.L):
            if self.talk and state == 0:
                print 'Calculating {0} / {1}'.format(ix+1, self.L),
                start = time.clock()
            if state & (1 << ix): continue
            newState = state + (1 << ix)
            newState, bars = self.standardize(newState)
            bars = max(maxBars, bars)
            delta = self.calcDistribution(newState, bars)
            for i in range(len(delta)):
                ans[i] += delta[i]
            if self.talk and state == 0:
                end = time.clock()
                print 'Took {0} s'.format(end-start)
                
        if self.talk and state == 0:
            print 'Took {0} s total'.format(time.clock() - fullStart)
                
        self.cache[(state, maxBars)] = ans
        return ans
        
    def calcStats(self):
        dist = self.calcDistribution(0,0)
        mostLikely = 0
        most = 0
        s = 0
        ave = 0
        for x in range(len(dist)):
            if dist[x] > most:
                most = dist[x]
                mostLikely = x
            s += dist[x]
            ave += x * dist[x]
        return mostLikely, float(ave) / s
    
    
if __name__ == '__main__':
    sol = Caterpillar(10)
    sol.standardize(0b0101000100)
    print ''
    print '  Ten piece Caterpillar  '
    print '-------------------------'
    print ''
    dist = sol.calcDistribution(0,0)
    print '     M  | Possibilities'    
    print '-------------------------'
    for x in range(1, len(dist)):
        print '     {0:2} | {1:7}'.format(x, dist[x])  
    print '-------------------------'
    print 'Most Likely : {0}\nAverage     : {1:.6f}'.format(*sol.calcStats())
    
    print ''
    print ''
    print '  Twenty piece Caterpillar  '
    print '----------------------------'
    sol20 = Caterpillar(20, True)
    dist = sol20.calcDistribution(0,0)
    print ''
    print '   M  | Possibilities'    
    print '----------------------------'
    for x in range(1, len(dist)):
        print '   {0:2} | {1:18}'.format(x, dist[x])  
    print '----------------------------'
    print 'Most Likely : {0}\nAverage     : {1:.6f}'.format(*sol20.calcStats())
    
    print ''
    print ''
    print '   Forty piece Caterpillar  '
    print '----------------------------'
    sol40 = Caterpillar(40, True)
    dist = sol40.calcDistribution(0,0)
    print ''
    print '   M  |                 Possibilities'    
    print '----------------------------------------------------------'
    for x in range(1, len(dist)):
        print '   {0:2} | {1:48}'.format(x, dist[x])  
    print '----------------------------------------------------------'
    print 'Most Likely : {0}\nAverage     : {1:.6f}'.format(*sol40.calcStats())