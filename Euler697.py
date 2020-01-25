"""Euler 697 - Randomly Decaying Sequence

P(X < 1) = ln(c) - sum k = 0 .. n-1 | x^k * e^-x / k!
"""
from math import log, exp

class Euler697:
    def __init__(self, N):
        self.N = N
        self.log_factorials = self.CalculateLogFactorials(N)
        self.intp_counter = 0
        self.max_top = 1.0
        self.verbose = False

    def CalculateLogFactorials(self, N):
        logs = [log(n) if n else 0 for n in range(N+1)]
        for i in range(1, N+1):
            logs[i] += logs[i-1]
        return logs

    def LogP(self, x, lx, n):
        return (n - 1) * lx - self.log_factorials[n - 1] - x

    def IntP(self, x, n):
        ret = 0
        lx = log(x)
        c = 0.0
        for i in range(1, n+1):
            y = exp(self.LogP(x, lx, i)) - c
            t = ret + y
            c = (t - ret) - y
            ret = t
        self.intp_counter += 1
        return ret

    def __call__(self, n, eps=1e-9):
        if n > self.N:
            self.log_factorials = self.CalculateLogFactorials(n)
            self.N = n
        self.intp_counter = 0
        xbot, xtop = n, n
        ptop = self.IntP(xtop, n)
        while ptop > 0.25:
            xtop *= 2
            ptop = self.IntP(xtop, n)
            if self.verbose:
                print(f'IntP({xtop})\t= {ptop}\tCalled {self.intp_counter} times.')
        while (xtop - xbot) / xtop > eps:
            xmid = (xtop + xbot) / 2.0
            pmid = self.IntP(xmid, n)
            if self.verbose:
                print(f'IntP({xmid})\t= {pmid}\tCalled {self.intp_counter} times.')
            if pmid > 0.25:
                xbot = xmid
            else:
                xtop = xmid
        return ((xtop + xmid) / 2.0) / log(10.0)




if __name__ == '__main__':
    sol = Euler697(10)
    sol.verbose = True
    print(sol(10))
    print(sol(100))
    print(sol(1000))
    # print(sol(10000))
    # print(sol(100000))
    # print(sol(1000000))
    print(sol(10000000))
