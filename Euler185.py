# Euler 185 - Number Mind
# Kelvin Blaser     2013-10-29   
import itertools as it
import copy

class Trial:
    def __init__(self, string, num_correct,
                 corr_list = [],
                 incorr_list = [],
                 unknown_list=None):
        self.string = string
        self.num_correct = num_correct
        self.corr = corr_list
        self.incorr = incorr_list
        if unknown_list is None:
            self.unknown = range(len(string))
        else:
            self.unknown = unknown_list

    def __str__(self):
        s = '('+self.string+', '+str(self.num_correct)
        s += ')\n'
        s += 'correct:   '+str(self.corr)+'\n'
        s += 'incorrect: '+str(self.incorr)+'\n'
        s += 'unknown:   '+str(self.unknown)
        return s
    def __repr__(self):
        s = '('+self.string+', '+str(self.num_correct)
        s += ')\n'
        s += 'correct:   '+str(self.corr)+'\n'
        s += 'incorrect: '+str(self.incorr)+'\n'
        s += 'unknown:   '+str(self.unknown)
        return s

    def mv_corr(self, i):
        if i not in self.corr:
            if i in self.unknown:
                self.unknown.remove(i)
            self.corr.append(i)
    def mv_incorr(self, i):
        if i not in self.incorr:
            if i in self.unknown:
                self.unknown.remove(i)
            self.incorr.append(i)

def solve(trials):
    if len(trials) == 0:
        return None
    t = trials[0]
    for comb in it.combinations(t.unknown,t.num_correct):
        #print t.string, t.unknown, comb
        tri = [copy.deepcopy(trials[i]) for i in range(1,len(trials))]
        #for i in comb:
         #   st = st[:i] + t.string[i] + st[i+1:]
        for x in tri:
            for i in range(len(t.string)):
                if i in comb:
                    if t.string[i] == x.string[i]:
                        x.mv_corr(i)
                        x.num_correct -= 1
                    else:
                        x.mv_incorr(i)
                else:
                    if t.string[i] == x.string[i]:
                        x.mv_incorr(i)
        if all([x.num_correct == 0 and len(x.unknown)==0 for x in tri]):
            s = '*' * len(t.string)
            for i in comb:
                s = s[:i]+t.string[i]+s[i+1:]
                t.mv_corr(i)
            return s
        if not any([x.num_correct < 0 or len(x.unknown) < x.num_correct
                    for x in tri]):
            s = solve(tri)
            if s is not None:
                for i in comb:
                    s = s[:i]+t.string[i]+s[i+1:]
                return s
    return None
        
    

raw = [('5616185650518293', 2),
       ('3847439647293047', 1),
       ('5855462940810587', 3),
       ('9742855507068353', 3),
       ('4296849643607543', 3),
       ('3174248439465858', 1),
       ('4513559094146117', 2),
       ('7890971548908067', 3),
       ('8157356344118483', 1),
       ('2615250744386899', 2),
       ('8690095851526254', 3),
       ('6375711915077050', 1),
       ('6913859173121360', 1),
       ('6442889055042768', 2),
       ('2321386104303845', 0),
       ('2326509471271448', 2),
       ('5251583379644322', 2),
       ('1748270476758276', 3),
       ('4895722652190306', 1),
       ('3041631117224635', 3),
       ('1841236454324589', 3),
       ('2659862637316867', 2)]

##raw = [('90342',2),('70794',0),('39458',2),('34109',1),('51545',2),('12531',1)]

trials = [Trial(p[0], p[1], [], []) for p in raw if p[1] != 0]
nulls = [Trial(p[0], 0, [], range(len(p[0])), []) for p in raw if p[1] == 0]
for n in nulls:
    for t in trials:
        for i in range(len(t.string)):
            if t.string[i] == n.string[i]:
                t.mv_incorr(i)
print solve(trials)
