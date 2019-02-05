################################################################################
# Euler 359 - Hilbert's New Hotel
# Kelvin Blaser      2015.02.20
#
# By filling in the hotel rooms, one sees that the diagonals where f+r = const
# fill two diagonals at a time.  That is, diagonal 2 and 3 fill completely
# before diagonals 4 and 5 start filling.  4 and 5 fill before 6 and 7 etc.
#
# You can work out the pattern to quickly determine P(f,r).  Then it is just a
# matter of calculating the divisors of 71328803586048 = 2^27 * 3^12 and calling
# P(f,r) for each f*r = 71328803586048
################################################################################

def P(f,r):
    n = (f+r-2)//2
    if f%2 == 1 and f != 1:
        if r%2 == 1:
            q = (f-1)/2
        else:
            q = 2*n - (f-3)/2
    else:
        if (f+r)%2 == 1:
            q = 4*n+3 - f//2
        else:
            q = 2*n+1 + f//2
    return n*(2*n+1) + q

def Euler359():
    N = 3**12 * 2**27  # 71328803586048
    threes = [3**n for n in range(13)]
    twos = [2**n for n in range(28)]
    divs = [x*y for x in twos for y in threes]
    divs.sort()
    return sum(P(f,N/f) for f in divs)


