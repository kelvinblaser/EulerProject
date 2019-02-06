# Euler 256 - Tatami-free Rooms
# Kelvin Blaser     2019.02.06
#
# See "Counting Fixed-Height Tatami Tilings" - F Ruskey & J Woodcock
# www.kurims.kyoto-u.ac.jp/EMIS/journals/EJC/Volume_16/PDF/v16i1r126.pdf
#
# Consider rooms of with m and length n with m <= n.  It is proved in the above
# paper that if m >= 3 is odd, n = x(m-1) + y(m+1) for integers x,y >= 0 and if
# m >= 4 is even, n = x(m-1) + y(m+1) + z for integers x,y >= 0 and z in {-1,0,1}
#
# This gives an algorithm for finding which n > m can't yield a tatami tiling.
# We count the number of such (m,n) where m*n = s

def intRoot(n):
    r = int(n**0.5)
    while r*r > n: r-=1
    while (r+1)**2 <= n: r += 1
    return r
    
def tatamiFree(sMax, N):
    tf = [0] * (sMax+1)
    for m in range(7, intRoot(sMax)+1):
        # For any m, we have series of runs of n which can be reached
        # and gaps of n which cannot be reached.  
        # The runs grow, and the gaps shrink until eventually there are no
        # more n which cannot be reached.
        #
        # Take m = 9 and 10 as prototypical examples
        # m = 9:
        # n = 0 2 4 6 8 10 12 14 16 18 20 22 24 ...
        #     x o o o x x  o  o  x  x  x  o  x  ... x
        # For odd m, the runs/gaps grow/shrink by 1, but we only consider even n
        #
        # m = 10
        # n = -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ...
        #      x x x o o o o o o x x x  x  x  o  o  o  o  x  x  x  x  x  x  x  o  o  x  ... x
        # For even m, the runs/gaps grow/shrink by 2, but we have to consider odd and even n
        if m%2 == 0: 
            run = 5
            gap = m-6
            delta = 1
            start = m-2
        else:
            run = 2
            gap = (m-5)//2
            delta = 2
            start = m-1
        while gap > 0 and m*start <= sMax:
            start += run*delta
            for n in range(start, start + gap*delta, delta):
                if m*n > sMax: break
                tf[m*n] += 1
            start += gap*delta
            run += (3-delta)
            gap -= (3-delta)
    maxFound = 0
    maxFoundAt = 0
    for x in range(sMax+1):
        if tf[x] == N: return x
        if tf[x] > maxFound:
            maxFound = tf[x]
            maxFoundAt = x
    print 'Max {0} found at s={1}'.format(maxFound, maxFoundAt)
    return -1
    
if __name__ == '__main__':
    print 'tatamiFree(69, 1) = {0}'.format(tatamiFree(69,1)) # Should be -1
    print 'tatamiFree(70, 1) = {0}'.format(tatamiFree(70,1)) # Should be 70
    print 'tatamiFree(1200, 5) = {0}'.format(tatamiFree(1200,5)) # Should be -1
    print 'tatamiFree(1500, 5) = {0}'.format(tatamiFree(1500,5)) # Should be 1320
    print 'tatamiFree(10^6, 200) = {0}'.format(tatamiFree(10**6,200)) 
    print 'tatamiFree(10^7, 200) = {0}'.format(tatamiFree(10**7,200)) 
    print 'tatamiFree(10^8, 200) = {0}'.format(tatamiFree(10**8,200)) 