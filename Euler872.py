"""Euler 872 - Recursive Tree

A couple things I noticed when building trees of different sizes.

1. An alternate way to construct T(n+1) from T(n)
   I noticed that T(n+1) has basically the same shape as T(n), except the
   numbers in each node increase by one, and you have to figure out where the
   new "1" node goes.

   If we re-label each node k in T(n) with n - k, then each tree is just a
   sub-tree of some infinite tree rooted with "0"

   The path from n to k in T(n) is the same as the pathe from 0 to n - k in the
   infinite tree.  So if we can walk that path, we can get the sum as long as
   we remember to convert the labels back to k from n - k.

2. In the infinite tree, if you write the label as a binary number, then the 
   children, grand-children, etc of that node all have the label as a suffix.
   Furthermore, the direct children are all the concatenation of a power of 2
   and the suffix.

   So walking the path from 0 to k is just a matter of parsing the binary
   representation of k.  Each stop on the path corresponds to a "1" in the
   binary representation, and its value in the infinite tree is the suffix of
   the representation starting from that "1"

   So for example, the path to k = 43 in the infinite tree would look like:

    k = 43 = 101011 base 2
    0 (0) -> 1 (1) -> 11 (3) -> 1011 (11) -> 101011 (43)

"""
from typing import Generator

def infinite_tree_path(k: int) -> Generator[int, None, None]:
    yield 0
    suffix, pow2 = 0, 1
    while k:
        bit = k % 2
        suffix += pow2 * bit
        if bit:
            yield suffix
        k //= 2
        pow2 *= 2

def f(n: int, k: int) -> int:
    s = 0
    for v in infinite_tree_path(n - k):
        s += n - v
    return s

if __name__ == '__main__':
    for n, k in [(6, 1), (10, 3), (10**17, 9**17)]:
        print(f'f({n}, {k}) = {f(n, k)}')