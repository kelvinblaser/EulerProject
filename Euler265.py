class binaryRun:
    def __init__(self, order):
        self.run = [0]*order
        self.order = order
        self.used = [0]

    def copy(self, other):
        other.run = list(self.run)
        other.order = self.order
        other.used = list(self.used)

    def can_add(self, n):
        if self.calc_num(n) in self.used:
            return False
        else:
            return True

    def calc_num(self, bit=None):
        l = len(self.run)
        ans = 0
        if bit == None:
            for ix in range(self.order):
                ans *= 2
                ans += self.run[l-self.order+ix]
        else:
            for ix in range(self.order-1):
                ans *= 2
                ans += self.run[l-self.order + ix + 1]
            ans *= 2
            ans += bit
        return ans

    def calc_ring(self):
        ans = 0
        for ix in range(2**self.order):
            ans *= 2
            ans += self.run[ix]
        return ans
            

N=5
x = binaryRun(N)
run_list = [x]
for i in range(2**N - N):
    to_add = []
    to_remove = []
    for x in run_list:
        if x.can_add(0):
            if x.can_add(1):
               y = binaryRun(N)
               x.copy(y)
               y.run = y.run + [1]
               y.used.append(y.calc_num())
               to_add.append(y)
            x.run = x.run + [0]
            x.used.append(x.calc_num())
        elif x.can_add(1):
            x.run = x.run + [1]
            x.used.append(x.calc_num())
        else:
            to_remove.append(x)


    for x in to_add:
        run_list.append(x)
    for x in to_remove:
        run_list.remove(x)
    print 'Level: ', i, 'Num Lists: ', len(run_list)
    #for x in run_list:
    #    print x.run

for i in range(N-1):
    to_remove = []
    for x in run_list:
        if not x.can_add(0):
            to_remove.append(x)
        else:
            x.run = x.run + [0]
            x.used.append(x.calc_num())
    for x in to_remove:
        run_list.remove(x)

    print 'New Level: ', i, 'Num Lists: ', len(run_list)
    #for x in run_list:
    #    print x.run

ans = 0
for x in run_list:
    ans += x.calc_ring()
print 'Total: ', ans


            
