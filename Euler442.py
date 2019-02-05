###############################################################################
# Euler 442 - Eleven-free Integers
# Kelvin Blaser         2015.1.7
#
# Finding the inverse of E(n) will be easier than calculating E(n).  That is,
# it will be easier to calculate how many eleven-free numbers are less than or
# equal to n, than to calculate the nth eleven free number.  Since E(n) is
# monotonic, I can use a binary search on it's inverse (call it F) to find the
# m such that F(m) = n.
#
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Calculating F(m)
# ------------------
# To show how I will calculate F(m), I will work through an example.  Suppose
# I want to calculate F(234).  First, I calculate the powers of 11 that can
# possibly be in the number.  These are 11 and 11^2=121.  F(234) will be the
# number of three digit eleven-free numbers starting with 1 or 0 plus the
# number of three digit eleven-free numbers starting with 20, 21, or 22 plus
# the number of eleven-free numbers in the set {230, 231, 232, 233, 234} minus
# 1 since I counted 000.
#
# To calculate these numbers, I classify all numbers in the following ways:
#   0. Those which don't fit any of the below
#   1. Those which end in '1'  and are eleven-free (-> 11)
#   2. Those which end in '12' and are eleven-free (-> 121)
#   X. Those which are not eleven-free
#
# Consider the three digit numbers which start with 0 or 1.  The number 0 fits
# category 0 and the number 1 fits the category 1.  So I construct the vector
# (1, 1, 0)T.  Now I need to add two digits to 0 and 1.  There are 9 ways to
# add a digit to numbers in category 0 so that the remain in 0 (add one of
# {0,2,3,4,5,6,7,8,9}), one way to add a digit to get into category 1 (add a
# '1') and no ways to add a digit to get into category 2 or category X.
# Similarly, there are 8 ways to get from category 1 to 0, one way to get from
# 1 to 2, one way to get from 1 to X, and no ways to get from 1 to 1.  With a
# similar analysis on category 2, construct the matrix
#                   (9 8 9)
#               A = (1 0 0)
#                   (0 1 0)
# A times the column vector we constructed categorizes the two digit numbers
# that start with 0 or 1, and A^2 times the vector categorizes the three digit
# numbers that start with 0 or 1.  I don't include a row and column for
# category X, since we don't count those anyways.  Construct the column vector
# for the set {20, 21, 22} and multiply it by A^1, the column vector for the
# set {230, 231, 232, 233, 234} and multiply it by A^0 and sum all the results
# to categorize all the numbers less than or equal to 234.  Multipy on the
# left by the row vector (1,1,1) and subtract 1 to get F(234)
#                        (     (1)       (2)     (4) )
#       F(234) = (1 1 1) ( A^2 (1)  +  A (1)  +  (1) ) - 1
#                        (     (0)       (0)     (0) )
#
#                        ( (170)   (26)   (4) )
#       F(234) = (1 1 1) ( ( 17) + ( 2) + (1) ) - 1
#                        ( ( 1 )   ( 1)   (0) )
#
#                       (200)
#       F(234) = (1 1 1)( 20) - 1 = 221
#                       (  2)
# ----------------------------------------------------------------------------
# The hardest part of this will be constructing the matrix for arbitrarily
# large numbers of digits (powers of 11).
#
# Also note that some numbers can fit into more than one category.  For example
# 3161 fits into the category '1' (part of 11^1 = 11) and the category '161'
# (part of 11^5 = 161051).  In cases like this, the number has to go into the
# category with the largest string.  In this case '161'.
###############################################################################
import numpy as np

class ElevenFree(object):
    def __init__(self, num_digs):
        self.num_digs = num_digs
        self.calcPowers11()
        self.calcDigitStrings()
        self.makeMatrix()

    def makeMatrix(self):
        ''' Creates the matrix A which increases the number of digits of the
        numbers categorized in a vector by 1. This is done by multiplying the
        column vector on the left by A.'''
        n = self.num_categories
        A = np.zeros((n, n),dtype=np.int64)
        for base_str in self.category_strings:
            if base_str == '':
                base = 0
            else:
                base = 10*int(base_str)
            col = self.getCategoryIndex(base_str)
            for d in range(10):
                if not self.isElevenFree(base+d):
                    continue
                row = self.getCategoryIndex(base+d)
                A[row,col] += 1
        self.A = A

    def calcPowers11(self):
        ''' Make a list of powers of 11 that can possibly show up in numbers
        with self.num_digs or fewer digits. '''
        power11 = 11
        self.powers11 = []
        while power11 < 10**self.num_digs:
            self.powers11.append(power11)
            power11 *= 11

    def calcDigitStrings(self):
        ''' Uses the powers of 11 to create the strings used to match numbers
        to the category they belong to '''
        strings = set()
        for power11 in self.powers11:
            p11string = str(power11)
            for i in range(len(p11string)):
                strings.add(p11string[:i])
        self.category_strings = list(strings)
        self.category_strings.sort()
        self.num_categories = len(self.category_strings)

    def getCategoryIndex(self, n):
        ''' Takes a number n and returns the index of the category n belongs to
        n can be in string or integer form. '''
        if not self.isElevenFree(n):
            return -1
        n = str(n)
        category_str = ''
        for c in self.category_strings:
            if n.endswith(c):
                if len(c) > len(category_str):
                    category_str = c
        return self.category_strings.index(category_str)

    def isElevenFree(self, n):
        ''' Tests whether n is eleven free or not '''
        n = str(n)
        for power11 in self.powers11:
            if str(power11) in n:
                return False
        return True

    def F(self, m):
        ''' The inverse of the function asked for (E(n)).  F(m) is the number
        of eleven-free positive integers less than or equal to m. '''
        if self.isElevenFree(m):
            ans = 1
        else:
            ans = 0
        # Get the digits of m
        digits = []
        while m > 0:
            digits.append(m%10)
            m /= 10
        # Create the vector x
        x = np.zeros(self.num_categories, dtype=np.int64)
        # For each digit, multiply by A and then add the new numbers into
        # their correct categories
        for dig in digits[::-1]:
            x = self.A.dot(x)
            for d in range(dig):
                if self.isElevenFree(10*m+d):
                    x[self.getCategoryIndex(10*m+d)] += 1
            m = 10*m+dig
        for z in x:
            ans += z
        return ans - 1

    def E(self, n):
        ''' Uses binary search to on the inverse F(m) to find the m such that
        F(m) = n '''
        bot = n-1
        top = 2*n
        while self.F(top) < n:
            bot = top
            top = 2*top
        while top - bot > 1:
            mid = (top + bot) / 2
            if self.F(mid) < n:
                bot = mid
            else:
                top = mid
        return top

if __name__ == '__main__':
    Euler422 = ElevenFree(19)
    print 'E(%d) = %d'%(3,Euler422.E(3))
    print 'E(%d) = %d'%(200,Euler422.E(200))
    print 'E(%d) = %d'%(500000,Euler422.E(500000))
    print 'E(%d^%d) = %d'%(10,18,Euler422.E(10**18))
