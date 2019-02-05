from fractions import Fraction, gcd
from collections import defaultdict

class Euler236:
    def __init__(self):
        self.N = [[5248, 1312, 2624, 5760, 3936],[640, 1888, 3776, 3776, 5664]]
        self.S = [sum(self.N[x]) for x in range(2)]
        
    def ratiosToTry(self):
        na = self.N[0][0]
        nb = self.N[1][0]
        for xa in range(1, na+1):
            den = xa*nb
            for xb in range(1, nb+1):
                num = xb*na
                if num <= den: continue
                g = gcd(num, den)
                yield (num // g, den // g)
        return
        
    def tryRatio(self, m):
        xa = [1]*5
        xb = [1]*5
        nMax = [1]*5
        for i in range(5):
            num = m[0] * self.N[1][i]
            den = m[1] * self.N[0][i]
            g = gcd(num, den)
            xa[i] = den // g
            xb[i] = num // g
            nMax[i] = min(self.N[0][i]//xa[i], self.N[1][i]//xb[i])
            if nMax[i] == 0: return False
        
        num = self.S[0]*m[0]
        den = self.S[1]*m[1]
        g = gcd(num, den)
        a,b = num // g, den // g
        k = [0]*5
        for i in range(5):
            k[i] = b*xa[i] - a*xb[i]
        # now need to see if solution exists for sum(n[i]*k[i]) == 0 with
        # 1 <= n[i] <= nMax[i]
        positives = [(i, k[i]) for i in range(5) if k[i] > 0]
        negatives = [(i, -k[i]) for i in range(5) if k[i] < 0]
        if len(positives) == 0 and len(negatives) == 0: return True
        if len(positives) == 0 or len(negatives) == 0: return False
        
        # Find all possible positive values from positive k and all possible
        # negative values from negative k and then use two pointer technique
        # to find any matches.
        #print m
        posvals = set([0])
        for i, kk in positives:
            nums = [kk*n for n in range(1, nMax[i]+1)]
            newPosvals = set()
            for x in posvals:
                for y in nums:
                    newPosvals.add(x+y)
            posvals = newPosvals
            #print '\t', i, kk, len(posvals), min(posvals), max(posvals)
            
        negvals = set([0])
        for i, kk in negatives:
            nums = [kk*n for n in range(1, nMax[i]+1)]
            newNegvals = set()
            for x in negvals:
                for y in nums:
                    newNegvals.add(x+y)
            negvals = newNegvals
            #print '\t', i, -kk, len(negvals), min(negvals), max(negvals)
        
        posvals = list(posvals)
        negvals = list(negvals)
        posvals.sort()
        negvals.sort()
        px, nx = 0, 0
        while px < len(posvals) and nx < len(negvals):
            if negvals[nx] == posvals[px]:
                return True
            if negvals[nx] < posvals[px]:
                nx += 1
            else:
                px += 1
        return False
        
    def solve(self):
        cache = {}
        solutions = set()
        for m in self.ratiosToTry():
            try:
                x = cache[m]
            except KeyError:
                cache[m] = self.tryRatio(m)
            if cache[m]:
                oldNum = len(solutions)
                solutions.add(Fraction(m[0], m[1]))
                if len(solutions) > oldNum:
                    sols = list(solutions)
                    sols.sort()
                    print len(cache), sols[0], sols[-1]
        solutions = [x for x in solutions]
        solutions.sort()
        print 'Solutions = [{0}]'.format(', '.join(['{0}/{1}'.format(f.numerator, f.denominator) for f in solutions]))
        print 'Num Solutions: {0}'.format(len(solutions))
        print 'Smallest: {0}\nLargest: {1}'.format(solutions[0], solutions[-1])
        
if __name__ == '__main__':
    e = Euler236()
    e.solve()

#def calculateSpoilRatios():
#    ratios = [defaultdict(int) for _ in range(5)]
#    #  N[i][j] is the number of product j provided by supplier i
#    N = [[5248, 1312, 2624, 5760, 3936],[640, 1888, 3776, 3776, 5664]]
#    for j in range(5):
#        print j
#        for a in range(1, N[0][j]+1):
#            for b in range(1, N[1][j]+1):
#                num = b * N[0][j]
#                den = a * N[1][j]
#                if num < den: continue
#                g = gcd(num, den)
#                m = (num // g, den // g)
#                ratios[j][m] += 1
#    return ratios

#productMap = {}
#productMap['Beluga Caviar'] = (5248, 640)
#productMap['Christmas Cake'] = (1312, 1888)
#productMap['Gammon Joint'] = (2624, 3776)
#productMap['Vintage Port'] = (5760, 3776)
#productMap['Champagne Truffles'] = (3936, 5664)

#  N[i][j] is the number of product j provided by supplier i
#N = [[5248, 1312, 2624, 5760, 3936],[640, 1888, 3776, 3776, 5664]]
#S = [sum(N[x]) for x in range(2)]
#mTried = 0
#
#def calcSolution(m, cache):
#    global mTried
#    try:
#        return cache[(m.numerator, m.denominator)]
#    except KeyError:
#        pass
#    
#    A = [0]*5
#    B = [0]*5
#    M = [0]*5
#    for i in range(5):
#        f = m*N[1][i] / N[0][1]
#        
#        B[i], A[i] = f.numerator, f.denominator
#        M[i] = min(N[0][i] // A[i], N[1][i] // B[i])
#        if A[i] > N[0][i] or B[i] > N[1][i]:
#            cache[(m.numerator, m.denominator)] = False
#            return cache[(m.numerator, m.denominator)]
#    f = m * S[0] / S[1]
#    YA, YB = f.numerator, f.denominator
#    Z = [YB*A[i] - YA*B[i] for i in range(5)]
#    if sum(1 for z in Z if z > 0) == 5 or sum(1 for z in Z if z < 0) == 5:
#        cache[(m.numerator, m.denominator)] = False
#        return cache[(m.numerator, m.denominator)]
#    
#    K = [0]*4
#    if mTried % 10 == 0:
#        print 'm Tried =', mTried
#    mTried += 1
#    print m, M
#    for K[0] in range(1, M[0] + 1):
#        for K[1] in range(1, M[1] + 1):
#            for K[2] in range(1, M[2] + 1):
#                for K[3] in range(1, M[3] + 1):
#                    partialDot = sum(K[i]*Z[i] for i in range(4))
#                    if partialDot % Z[4] != 0:
#                        continue
#                    K5 = -partialDot / Z[4]
#                    if K5 >= 1 and K5 <= min(N[0][4] // A[4], N[1][4] // B[4]):
#                        cache[(m.numerator, m.denominator)] = True
#                        return cache[(m.numerator, m.denominator)]
#        
#    cache[(m.numerator, m.denominator)] = False
#    return cache[(m.numerator, m.denominator)]
#
#def Euler236(cache):
#    global mTried
#    solutions = set([])
#    mTried = 0
#    NB0 = N[1][0]
#    NA0 = N[0][0]
#    for XB in range(1, NB0 + 1):
#        for XA in range(1, (XB*NA0)//NB0+1):
#            m = Fraction(XB*NA0, XA*NB0)
#            if m > 1:
#                if len(cache) % 100000 == 0:
#                    print len(cache), 'solutions tested'
#                if calcSolution(m, cache):
#                    l = len(solutions)
#                    solutions.add(m)
#                    if len(solutions) > l:
#                        print len(solutions), m, max(solutions)
#    solutions = list(solutions)
#    solutions.sort()
#    print solutions
#    print solutions[-1]
#    return solutions