# Euler 259 - Reachable Numbers
# https://projecteuler.net/problem=259
# Kelvin Blaser   2014.12.16

from fractions import Fraction

class Euler259(object):
    CON, ADD, SUB, MUL, DIV = (0,1,2,3,4)

    def __init__(self):
        self.solve()

    def solve(self):
        numList = [1,2,3,4,5,6,7,8,9]
        self.reachables = set()
        for n in xrange(5**8):
            if n%5**4 == 0:
                print n, len(self.reachables)
            opList = self.n2opList(n)
            self.condense(numList, opList)
        self.solution = sum(self.reachables)
            
    def n2opList(self,n):
        opList = []
        for i in range(8):
            opList.append(n%5)
            n /= 5
        return opList

    def condense(self, numList, opList):
        if not opList:
            x = numList[0]
            if x > 0:
                if isinstance(x,Fraction):
                    if x.denominator == 1:
                        self.reachables.add(int(x))
                        #print int(x)
                else:
                    self.reachables.add(x)
                    #print x
        if self.CON in opList:
            ix = opList.index(self.CON)
            x = self.op(self.CON, numList[ix], numList[ix+1])
            self.condense(numList[:ix]+[x]+numList[ix+2:],
                          opList[:ix]+opList[ix+1:])
        else:
            for ix in range(len(opList)):
                x = self.op(opList[ix], numList[ix], numList[ix+1])
                if not x:
                    continue
                self.condense(numList[:ix]+[x]+numList[ix+2:],
                              opList[:ix]+opList[ix+1:])
    
    def op(self, OP, x,y):
        if OP == self.CON:
            return int(str(x)+str(y))
        elif OP == self.ADD:
            return x+y
        elif OP == self.SUB:
            return x-y
        elif OP == self.MUL:
            return x*y
        elif OP == self.DIV:
            if y == 0:
                return None
            return Fraction(x) / Fraction(y)

if __name__ == '__main__':
    print Euler259().solution
