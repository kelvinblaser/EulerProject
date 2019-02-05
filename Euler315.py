################################################################################
# Euler 315 - Digital Root Clocks
# Kelvin Blaser      2015.02.21
#
#-------------------------------------------------------------------------------
#  ENCODE DIGITS
# We can represent each digit as a 7 bit string corresponding to which of the
# 7 segments in the display light up when the number shows.
#                                     0  
#   0 - 0b1111011                   ____
#   1 - 0b1001000                1 |  2 | 3
#   2 - 0b0111101                  |____|
#   3 - 0b1101101                  |    |
#   4 - 0b1001110                4 |____| 6
#   5 - 0b1100111                     5
#   6 - 0b1110111
#   7 - 0b1001011
#   8 - 0b1111111
#   9 - 0b1101111
#
#  Note that they use a weird representation for the number 7, where segment
#  1 is lit.  Most 7-seg displays I've seen do not light segment 1 for a 7.
#
#-------------------------------------------------------------------------------
#  Digital Roots
# It's fairly straight-forward to build the digital root sequence for a given
# number.  Just add the digits and stop when you get a 1 digit number
#
#-------------------------------------------------------------------------------
#  Digitsl Root Clock costs
# Sam's Clock:
# For each digit in the numbers in the digital root sequence, count the number
# of ones in the 7 segment display encoding for that digit twice (on then off).
#
# Max's Clock:
# Do the same as with Sam's clock, but subtract twice the number of segments
# which do not have to turn off then back on for each transition in the digital
# root sequence.  This number is the sum of the number of ones in the bitwise
# and of the digits in the same decimal place of the two numbers in the
# transition, not including leading zeros.
#   For example:   137 --> 11  We would subtract twice the number of ones in
# binary representation of
#    encoding[3] & encoding[1] + encoding[7] & encoding[1]
#    count_ones(0b1001000) + count_ones(0b1001000) = 4
# Thus we would subtract 8 for this transistion.
#
# The difference between the two clocks is just the sum of the numbers we
# subtracted, so that is the only thing we need to calculate.
################################################################################

from Primes import MakePrimeList
from bisect import bisect
import scipy as sp

SEG7ENC = [0b1111011, 0b1001000, 0b0111101, 0b1101101, 0b1001110,
           0b1100111, 0b1110111, 0b1001011, 0b1111111, 0b1101111]
TRANSBIN = sp.zeros((10,10),dtype=int)
for i in range(10):
    TRANSBIN[i,i] = bin(SEG7ENC[i]).count('1')
    for j in range(i):
        TRANSBIN[i,j] = bin(SEG7ENC[i] & SEG7ENC[j]).count('1')
        TRANSBIN[j,i] = TRANSBIN[i,j]

def print7seg(n):
    code = SEG7ENC[n%10]
    segs = [(2**i) & code for i in range(7)]
    # Line 0
    if segs[0] == 0:
        print ''
    else:
        print ' ____ '
    # Line 1 and 2
    if segs[1]:
        line1 = '|  '
        line2 = '|'
    else:
        line1 = '   '
        line2 = ' '
    if segs[2]:
        line2 += '____'
    else:
        line2 += '    '
    if segs[3]:
        line1 += '  |'
        line2 += '|'
    print line1
    print line2
    # Line 3 and 4
    if segs[4]:
        line1 = '|  '
        line2 = '|'
    else:
        line1 = '   '
        line2 = ' '
    if segs[5]:
        line2 += '____'
    else:
        line2 += '    '
    if segs[6]:
        line1 += '  |'
        line2 += '|'
    print line1
    print line2
    
    

def transDiff(x,y):
    ret = 0
    while x > 0 and y > 0:
        ret += TRANSBIN[x%10,y%10]
        x /= 10
        y /= 10
    return ret

def digitalRootTransDiff(n):
    x_next = n
    x_prev = n
    ret = 0
    while x_next > 9:
        x_prev = x_next
        x_next = 0
        y = x_prev
        while y > 0:
            x_next += y%10
            y /= 10
        ret += transDiff(x_next,x_prev)
    return ret

def Euler315():
    ps = MakePrimeList(2*10**7)
    ret = 0
    n = bisect(ps,10**7)
    print ps[n-1],ps[n],ps[n+1],ps[-1]
    print ps[n:][0]
    for p in ps[n:]:
        ret += digitalRootTransDiff(p)
    return 2*ret

if __name__ == '__main__':
    print Euler315()
    pass
