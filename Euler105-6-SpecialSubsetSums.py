# Special Subset Sums
# Euler 105 and 106
# Kelvin Blaser  2013-04-06
#               Yay!  I'm 27 years old

def isSpecialSumSet(A):
    """
    isSpecialSumSet(A)
    
    Tests a set A to see if it is a special sum set.

    Let S(A) be the sum of the elements in a finite set A
    A set A is a special sum set if for any two non-empty disjoint subsets,
    B and C, the following properties are true:
        1. S(B) != S(C)  :  The sum of subsets cannot be equal
        2. S(B) > S(C) whenever B contains more elements than C

    """
    N = len(A)
    # Make every subset B. (But not the empty set or A itself)
    # Could pare this down by a factor of 2 since this tests each pair
    # of subsets twice.
    for n in range(1, 2**N-1):
        B = makeSubSet(A,n)
        AminB = setMinus(A,B)
        # For each subset B, make every subset C from what is left.
        M = len(AminB)
        for m in range(1, 2**M):
            C = makeSubSet(AminB, m)
            # For each B and C, test the conditions
            if sum(C) == sum(B):
                return False
            if len(B) > len(C) and sum(B) <= sum(C):
                return False
            if len(C) > len(B) and sum(C) <= sum(B):
                return False
    return True
            
def makeSubSet(A, n):
    """
    makeSubSet(A, n)

    Returns the nth subset of A.  If A has N elements, there are 2**N subsets.
    The nth subset has the elements of A which correspond to the ones in the
    binary representation of n.

    For example, consider A with five elements and n = 19.  The binary
    representation of n is 10011.  Thus the 19th subset of A contains A[0],
    A[1], and A[4]; but not A[2] and A[3].

    The 0th subset is the empty set, while the (2**N-1)th is A itself.
    
    """
    N = len(A)
    if n < 0 or n >= 2**N:
        print 'Subset bounds exceeded: Returning Empty Set'
        return []

    subSet = []
    ix = 0
    while n > 0 and ix < N:
        if n%2:
            subSet.append(A[ix])
        n /= 2
        ix += 1
    return subSet

def setMinus(A,B):
    """
    setMinus(A,B)

    Returns A/B: ie, The set containing the elements of A which are not in B.
    """
    subSet = [el for el in A if el not in B]
    return subSet

def Euler105(filename='sets.txt'):
    ans = 0
    f = open(filename)
    for line in f:
        words = line.split(',')
        A = [int(word) for word in words]
        if isSpecialSumSet(A):
            #print A, ' is a special sum set.'
            ans += sum(A)
        else:
            #print A, ' is not a special sum set.'
            pass
    f.close()
    print ans
    return ans
            
    
