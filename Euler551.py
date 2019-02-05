# Euler 551
#
# Kelvin Blaser 9-4-2018
#
# We can solve this problem by splitting the digits of numbers a_n in the 
# sequence into two halves, a prefix and suffix.  Denote a_n  = p_n|s_n
# Now s_n will change on every iteration, but for judicious choice of split
# location p_n will be the same for many iterations.  Further more, there are
# not many values the digit sum (ds) of p_n can take on, relative to the number
# of values p_n itself can take on.  So we can precalculate the sequences
# s_n takes for the possible values of ds(p_n) and calculate large jumps in n
# for each increment in p_n
#
# Take the 10^6 example:
# Suppose every value a_n has 6 or fewer digits.  We can get an upper limit on 
# a_10^6 by assuming every digit is 9.  Thus each ds(a_n) <= 54 and
# a_10^6 <= 54x10^6.  Oops this breaks our suppposition.  But now assume every
# a_n has 8 or fewer digits.  Thus each ds(a_n) <= 72 and a_10^6 <= 72x10^6
# So now we know that every a_n has 8 or fewer digits.
#
# Let's split a_n into a prefix of 4 digits and a suffix of 4 digits.  Now I
# can just calculate 4x9 = 36 sequences of ~10^4 iterations.  One sequence for 
# each possible digit sum of the 10^4 prefixes.  Then I can (somehow?) jump
# from one prefix to the next 10^4 times until I home in on the a_n for 
# n = 10^6.
#
# Now do it again for 10^15:
# Suppose every value has 15 or fewer digits.  Then ds(a_n) <= 135 and 
# a_10^15 <= 135x10^15.  Breaks the supposition.  Suppose every value has 18 or
# fewer digits.  Then ds(a_n) <= 162 and a_10^15 <= 162x10^15.  Nice.
#
# So now do I split 9|9 or 10|8.  If I split 9|9 I will need space for 81*10^9
# integer values.  Not enough memory.  I have to trade time for space.  If 
# I split 10|8, I will need 90x10^8 integer values.  Still too much.  Looks like
# this is going to take a long time to run.  I have to split 11|7.
#
# Actually, note the change in the solve10to15() method. I can split 9|9, 
# because I don't need to store data for 10^9 starting suffixes when only
# 18*9 = 162 starting suffixes are possible.  This is because the ds(a_n) for
# the a_n immediately before a prefix transition can be at most 162.

def digSum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve10to6():
    # split 4|4
    # Precalculate the jump from one prefix to the next given a starting suffix
    # Also precalculate which suffix the next jump starts at
    suffix_jump = [[0]*(10**4) for _ in range(37)]
    suffix_end = [[0]*(10**4) for _ in range(37)]
    
    for ds in range(37):
        for suffix in range(10**4-1, -1, -1):
            next_suffix = suffix + ds + digSum(suffix)
            if next_suffix >= 10**4:
                suffix_jump[ds][suffix] = 1
                suffix_end[ds][suffix] = next_suffix % 10**4
            else:
                suffix_jump[ds][suffix] = suffix_jump[ds][next_suffix] + 1
                suffix_end[ds][suffix] = suffix_end[ds][next_suffix]
    
    # Now start going through prefixes
    n = 1
    sf = 1
    pf = 0
    while n <= 10**6:
        jump = suffix_jump[digSum(pf)][sf]
        if n + jump > 10**6: break # If the jump is too big, we are done jumping
        n += jump
        sf = suffix_end[digSum(pf)][sf]
        pf += 1
    # Now get the rest of the way from n to 10^6
    a = pf * 10**4 + sf
    while n < 10**6:
        a += digSum(a)
        n += 1
    return a
    
def solve10to15():
    # Split 9|9
    # Precalculate the jump from one prefix to the next given a starting suffix
    # Also precalculate which suffix the next jump starts at
    suffix_calculated = [[False]*162 for _ in range(82)]
    suffix_calculated[0][0] = True  # Avoid the infinite loop 0 -> 0 -> 0 etc.
    suffix_jump = [[0]*162 for _ in range(82)]
    suffix_end = [[0]*162 for _ in range(82)]
    
    for ds in range(82):
        print 'ds =', ds
        for suffix in range(162):
            if suffix_calculated[ds][suffix]: continue
            jump = 0
            next_suffix = suffix
            while next_suffix < 10**9:
                jump += 1
                next_suffix += ds + digSum(next_suffix)
            co_suffix = suffix
            while co_suffix < 162:
                suffix_calculated[ds][co_suffix] = True
                suffix_jump[ds][co_suffix] = jump
                suffix_end[ds][co_suffix] = next_suffix % 10**9
                jump -= 1
                co_suffix += ds + digSum(co_suffix)
    print suffix_jump[0]
    print suffix_end[0]
    
    # Now start going through prefixes
    n = 1
    sf = 1
    pf = 0
    while n <= 10**15:
        jump = suffix_jump[digSum(pf)][sf]
        if n + jump > 10**15: break # If the jump is too big, we are done jumping
        n += jump
        sf = suffix_end[digSum(pf)][sf]
        pf += 1
    # Now get the rest of the way from n to 10^15
    a = pf * 10**9 + sf
    while n < 10**15:
        a += digSum(a)
        n += 1
    return a
    
if __name__ == '__main__':
    print 'a_10^6 = {0}'.format(solve10to6())
    print 'a_10^15 = {0}'.format(solve10to15())