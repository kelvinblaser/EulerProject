# Euler 689
from __future__ import division
from __future__ import print_function

import math
import collections

PI = math.pi
BASEL = PI*PI / 6

Interval = collections.namedtuple('Interval', ('partial_sum', 'level', 'multiplicity'))

class Euler689(object):
    def __init__(self):
        self.basel_diff = [BASEL]

    def p(self, a, eps=10**9):
        if a > BASEL:
            return 0.0
        if a < 0:
            return 1.0

        q = collections.deque()
        q.append(Interval(0.0, 0, 1))
        prob, sigma, est = 0.0, 1.0, 1 - a / self.basel_diff[0]
        ll = -1
        while sigma > eps:
            ps, l, m = q.popleft()
            if l > ll:
                if len(q) > 10000:
                    q.appendleft(Interval(ps, l, m))
                    q = self.recombine(q)
                    ps, l, m = q.popleft()
                print(l, prob, prob + est, sigma, len(q))
                ll = l
            sigma -= m * 2**(-l)
            est -= m * 2**(-l) * (1 - ((a - ps) / self.basel_diff[l]))
            l += 1
            if len(self.basel_diff) <= l:
                self.basel_diff.append(self.basel_diff[-1] - 1 / (l * l))
            # Left half
            if ps + self.basel_diff[l] >= a:
                q.append(Interval(ps, l, m))
                sigma += m * 2**(-l)
                est += m * 2**(-l) * (1 - ((a - ps) / self.basel_diff[l]))
            # Right half
            if ps + 1 / (l * l) >= a:
                prob += m * 2**(-l)
            else:
                q.append(Interval(ps + 1 / (l * l), l, m))
                sigma += m * 2**(-l)
                est += m * 2**(-l) * (1 - ((a - ps - 1 / (l * l)) / self.basel_diff[l]))
        return prob, prob + est, sigma

    def recombine(self, q):
        vals = [x for x in q]
        vals.sort()
        ix = 0
        new_q = collections.deque()
        while ix < len(vals):
            ps, l, m = vals[ix]
            ix += 1
            if ix < len(vals):
                nps, nl, nm = vals[ix]
                ps = (ps + nps) / 2.0
                m += nm
                ix += 1
            new_q.append(Interval(ps, l, m))
        return new_q

if __name__ == '__main__':
    e = Euler689()
    print(e.p(0.5, 0.0001))
