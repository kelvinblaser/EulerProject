###############################################################################
# Euler 290 - Digital Signature
# Kelvin Blaser     2015.1.13
#
# Let di be the ith digit of n and ai be the ith digit of 137n
#          n = [d17 d16 ... d3 d2 d1 d0]
#       137n = [a20 a19 ... a3 a2 a1 a0]
#
# Using the multiplication algorithm I learned in grade school, I can calculate
# ai from the various di.
#                  d17  d16 ...  d3  d2  d1  d0
#                      x              1   3   7
#              ---------------------------------
#                 7d17 7d16 ... 7d3 7d2 7d1 7d0
#            3d17 3d16 3d15 ... 3d2 3d1 3d0  0
#       1d17 1d16 1d15 1d14 ... 1d1 1d0  0   0
#    -------------------------------------------
#    a20 a19  a18  a17  a16 ...  a3  a2  a1  a0
#
# Let ci be the carry value when calculating ai, then
#           ai = (7di + 3di-1 + di-2 + ci-1) % 10
#           ci = (7di + 3di-1 + di-2 + ci-1) // 10
#
# This lends itself to dynamic programming, since ai only depends on four
# values.  I can just keep track of the number of digits used, the running
# difference sum(ai)-sum(di) [This needs to be zero at the end to have a valid
# n], the previous carry ci-1, and the two previous digits di-1 and di-2.
###############################################################################

class Euler290(object):
    def __init__(self, num_digits):
        self.num_digits = num_digits
        self.cache = {}
        self.solution = self.solve()

    def solve(self, digits=0, difference=0, d1=0, d2=0, carry=0):
        # The key for caching is (digits, difference, d1, d2, carry)
        
        if digits >= self.num_digits:  # If nearing the end (di can only be 0)
            if d1 == 0 and d2 == 0 and carry == 0: # If at the end
                if difference == 0:
                    return 1
                else:
                    return 0
            d_max = 0
        else:
            d_max = 9

        key = (digits, difference, d1, d2, carry)
        try:
            return self.cache[key]
        except KeyError:
            pass

        ans = 0
        for d in range(d_max+1):
            q = (7*d + 3*d1 + d2 + carry)
            a = q % 10
            c = q // 10
            ans += self.solve(digits+1, difference+a-d, d, d1, c)
            
        self.cache[key] = ans
        return ans

if __name__ == '__main__':
    print '1 digit: %d'%(Euler290(1).solution,)
    print '2 digit: %d'%(Euler290(2).solution,)
    print '3 digit: %d'%(Euler290(3).solution,)
    print '4 digit: %d'%(Euler290(4).solution,)
    print '5 digit: %d'%(Euler290(5).solution,)
    print '6 digit: %d'%(Euler290(6).solution,)
    print '18 digit: %d'%(Euler290(18).solution,)
        
