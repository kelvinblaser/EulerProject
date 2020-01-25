'''
Project Euler - Problem 411

Solution strategy
    1. Get the set of station points
    2. Sort them by (x,y) lexicographically
    3. Find the maximum path to each point by considering each of the maximum
       path branches that could lead to the point.
    4. Return maximum path to (n,n) corner
'''

from collections import defaultdict

def calculate_stations(n):
    x,y = 1,1
    stations = set()
    for i in range(2*n+1):
        if i % 10000 == 0:
            print(i)
        while x >= n:
            x -= n
        while y >= n:
            y -= n
        if (x,y) in stations: break
        stations.add((x,y))
        x *= 2
        y *= 3
    stations = list(stations)
    #stations = list(set((pow(2,i,n), pow(3,i,n)) for i in range(2*n+1)))
    stations.sort()
    return stations

def max_station_path(stations):
    max_paths_min_y = [0]
    for (n, (x, y)) in enumerate(stations):
        if n % 10000 == 0:
            print(n, (1000 * n // len(stations)) / 1000.0, x, y, len(max_paths_min_y))
        for i in range(len(max_paths_min_y)-1, -1, -1):
            if max_paths_min_y[i] <= y:
                d = i + 1
                if len(max_paths_min_y) == d:
                    max_paths_min_y.append(y)
                else:
                    max_paths_min_y[d] = min(max_paths_min_y[d], y)
                break
    return len(max_paths_min_y) - 1

def S(n):
    stations = calculate_stations(n)
    return max_station_path(stations)

if __name__ == '__main__':
    fmt_str = 'S({}) = {}'
    for n in range(1, 6):
        print(fmt_str.format(n, S(n)))
    print(fmt_str.format(22, S(22)))
    print(fmt_str.format(123, S(123)))
    print(fmt_str.format(10000, S(10000)))
    print()

    ans = 0
    fmt_str = 'k = {0}\t{1:30}SUM = {2}'
    exp_str = 'S({0}) = {1}'
    for k in range(1, 31):
        s = S(k**5)
        ans += s
        print(fmt_str.format(k, exp_str.format(k**5, s), ans))
    print('sum( S(k^5), 1 .. 30 ) =', ans)
