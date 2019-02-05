# Euler 294 - Sum of digits - experience #23
#
# Need to find all numbers k less than 10^n (i.e. have n digits allowing for 
# leading zeros) where k is divisible by 23 and the sum of the digits of k
# is exactly 23.
#
# Plan of attack:
#  1. Find all of the partitions of 23 such that each summand is less than 10
#     For example: 23 = 9+9+5 = 9+9+4+1 = 8+7+6+1+1, etc.
#  2. For each partition p find all solutions to the equation
#       sum( x_i * n_i, n_i in p ) = 0 mod 23 where x_i can only take the values
#       {1,2,3,4, ..., 20,21,22} (no 0's)
#      This works because k = sum(10^i * n_i, i) but 10^i can only take those
#      values mod 23.
#  3. For each solution for each partition, calculate the number of ways we could
#     drop the digits in the partition into the correct digit slots of k according
#     to the solution.
#         For example: 
#             One solution for the partition 9+9+5 is 
#             1x9 + 19x9 + 10x5 = 230 = 0 mod 23.
#             We know 10^0 = 1, 10^5 = 19, and 10^1 = 10, so there will be at 
#             at least one number k that works as long as n >= 5
#             Suppose n = 24.  Then there is one slot for 10^5 = 19, two slots
#             for 10^1 = 10^23 = 19 and two slots for 10^0 = 10^22 = 1.
#             This gives us the following four values for k:
#               1. 000000000000000000900059
#               2. 090000000000000000900050
#               3. 500000000000000000900009
#               4. 590000000000000000900000
#      The number of ways to build k with particular digits in particular slots
#      is a straightforward product of multi-nomial coefficients
#
# This plan of attack requires two loops.  Each loop has a reasonably large
# number of iterations, so hopefully it doesn't blow up too large.  I'll need a
# quick way to find all of the solutions in step 2.  I don't want to try every
# combination and see if it is a solution. That will likely take too long.

def generatePartitions(n, maxSummand):
    '''Generates the partitions of n with all summands less than or equal to 
    maxSummand'''
    if n == 0:
        yield []
        return
    if n == 1 and maxSummand > 0:
        yield [1]
        return
    
    for x in range(min(n, maxSummand), 0, -1):
        for p in generatePartitions(n-x, x):
            yield [x] + p
    return
    