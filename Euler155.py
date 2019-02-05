# Euler 155 - Counting Capacitor Circuits
# Kelvin Blaser   2013-10-19

import fractions as fr

circuits_dict = {1 : set([fr.Fraction(1)])}
for n in range(2,19):
    circuits_dict[n] = set()
    for x in range(1,n/2+1):
        for val1 in circuits_dict[x]:
            for val2 in circuits_dict[n-x]:
                circuits_dict[n].add(val1+val2)
                circuits_dict[n].add(val1*val2 / (val1 + val2))
    print n, sum([len(circuits_dict[y]) for y in range(1,n+1)])
print len(circuits_dict[18])
