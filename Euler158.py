# Euler 158 - Strings in which exactly one letter comes lexicographically after
#             its neighbor to the left
#  Kelvin Blaser 2013-10-14

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def p(n, memo):
    if n > 26 or n < 2:
        return 0
    #return sum([f([ch], n-1, False, ch, memo) for ch in LETTERS])
    return before(n, 26, 0, memo)

def before(n, n_less, n_greater, memo):
    if n == 1:
        return n_greater
    if (n_less+n_greater) < n:
        return 0
    key = (n, n_less, n_greater)
    if memo.has_key(key):
        return memo[key]
    ans = sum([after(n-1, x+n_less, memo) for x in range(n_greater)])
    ans += sum([before(n-1, n_less-x-1, x+n_greater, memo)
                for x in range(n_less)])
    memo[key] = ans
    return ans

def after(n, n_less, memo):
    if n == 1:
        return n_less
    if n_less < n:
        return 0
    key = (n, n_less)
    if memo.has_key(key):
        return memo[key]
    ans = sum([after(n-1, x, memo) for x in range(n_less)])
    memo[key] = ans
    return ans
        

##def f(used, n, after, last, memo):
##    used.sort
##    key = (tuple(used), n, after, last)
##    if memo.has_key(key):
##        return memo[key]
##
##    if after:
##        if n == 1:
##            ans  = sum([1 for ch in LETTERS if ch < last and ch not in used])
##            memo[key] = ans
##            return ans
##        ans = sum([f(used+[ch], n-1, True, ch, memo) for ch in LETTERS
##                   if ch < last and ch not in used])
##        memo[key] = ans
##        return ans
##    if n == 1:
##        ans = sum([1 for ch in LETTERS if ch > last and ch not in used])
##        memo[key] = ans
##        return ans
##    ans = sum([f(used+[ch], n-1, True, ch, memo) for ch in LETTERS
##               if ch > last and ch not in used])
##    ans += sum([f(used+[ch], n-1, False, ch, memo) for ch in LETTERS
##                if ch < last and ch not in used])
##    memo[key] = ans
##    return ans

memo = {}
for n in range(1, 27):
    print n, '\t', p(n,memo)
