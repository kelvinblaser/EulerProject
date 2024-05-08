"""Euler 816 - Shortest Distance Among Points

https://projecteuler.net/problem=816

1. Make the list of points.
2. Sort the list of points by x value.
3. Iterate over each pair of points keeping track of the shortest distance.
  3a. Shortcut the iteration when ever the difference of the x values is larger
      than the shortest distance found.
"""

MOD = 50515093

def make_points(k: int) -> list[tuple[int, int]]:
    s = 290797
    points = []
    for _ in range(k):
        x = s
        s = (s * s) % MOD
        y = s
        s = (s * s) % MOD
        points.append((x, y))
    return points

def d(k: int) -> float:
    points = make_points(k)
    points.sort()
    min_square_dist = 2 * MOD * MOD  
    for n, p1 in enumerate(points):
        x1, y1 = p1
        n2 = n + 1
        while n2 < len(points):
            x2, y2 = points[n2]
            n2 += 1
            dx2 = (x1 - x2) ** 2
            if dx2 >= min_square_dist:
                break
            sd = dx2 + (y1 - y2) ** 2
            if sd < min_square_dist:
                min_square_dist = sd
    return min_square_dist ** 0.5

if __name__ == '__main__':
    for k in [14, 2_000_000]:
        print(f'd({k}) = {d(k)}')
