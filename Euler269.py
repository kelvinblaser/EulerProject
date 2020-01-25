# Euler 269
#
# For x > 0, Pn(x) > 0 for positive n.  Any integer roots of Pn(x) must divide the final
# digit of n.  The only possible integer roots are -9, -8, -7, ... -2, -1, 0.
#
# vn = vo * (-dc) + d

import math
import functools

def lcm(a, b):
    return a*b // math.gcd(a,b)

POLY_VALUE_LIMIT = [1, 10**100, 10, 5, 4, 3, 2, 2, 2, 2]
POLY_COUNT = {}

@functools.lru_cache(maxsize=None)
def root_combos():
    combos = [()]
    ix = 0
    while ix < len(combos):
        l = 1
        for r in combos[ix]:
            if not r == 0:
                l = lcm(l, r)
        for d in range(max((-1,) + combos[ix]) + 1, 10):
            if d == 0 or lcm(l, d) < 10:
                combos.append(combos[ix] + (d,))
        ix += 1
    return combos[1:]

@functools.lru_cache(maxsize=None)
def poly_count(num_digits, domain_combo, val_combo):
    if num_digits == 0:
        return 1 if all([v == 0 for v in val_combo]) else 0
    count = 0
    for d in range(10):
        new_vals = [[]]
        for ix in range(len(domain_combo)):
            if domain_combo[ix] == 0:
                if d == val_combo[ix]:
                    new_vals = [new_vals[0][:] +[x] for x in range(10)]
                else:
                    break
            elif (val_combo[ix] - d) % domain_combo[ix] == 0:
                for jx in range(len(new_vals)):
                    new_vals[jx].append((val_combo[ix] - d) // (-domain_combo[ix]))
            else:
                break
        else:
            for new_val in new_vals:
                count += poly_count(num_digits - 1, domain_combo, tuple(new_val))
    return count

def Euler269(num_digits):
    count = 0
    for domain_combo in root_combos():
        zeros = tuple([0]*len(domain_combo))
        count += (-1)**(len(domain_combo) + 1) * poly_count(num_digits, domain_combo, zeros)
    return count

if __name__ == '__main__':
    print(Euler269(1))
    print(Euler269(5))
    print(Euler269(16))
