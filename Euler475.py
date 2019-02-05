# Answer : 75780067

def choose2(a):
    return (a*(a-1)) / 2
    
def count_trios(key, memo, m):
    try:
        return memo[key]
    except KeyError:
        pass
    if key == (0,0,0,0):
        return 1
    x,y,z,w = key
    if x < 0 or y < 0 or z < 0 or w < 0:
        return 0
    ans = 0
    if x != 0:
        ans += choose2(x-1) * count_trios((x-3,y+3,z,w), memo, m) * 4 * 4
        ans += (x-1) * y * count_trios((x-2,y+1,z+1,w), memo, m) * 4 * 3
        ans += (x-1) * z * count_trios((x-2,y+2,z-1,w+1), memo, m) * 4 * 2
        ans += (x-1) * w * count_trios((x-2,y+2,z,w-1), memo, m) * 4
        ans += choose2(y) * count_trios((x-1,y-1,z+2,w), memo, m) * 3 * 3
        ans += y * z * count_trios((x-1,y,z,w+1), memo, m) * 3 * 2
        ans += y * w * count_trios((x-1,y,z+1,w-1), memo, m) * 3
        ans += choose2(z) * count_trios((x-1,y+1,z-2,w+2), memo, m) * 2 * 2
        ans += z * w * count_trios((x-1,y+1,z-1,w), memo, m) * 2
        ans += choose2(w) * count_trios((x-1,y+1,z,w-2), memo, m)
        memo[key] = ans % m
        return memo[key]
    if y != 0:
        ans += choose2(y-1) * count_trios((0,y-3,z+3,w), memo, m) * 3 * 3
        ans += (y-1) * z * count_trios((0,y-2,z+1,w+1), memo, m) * 3 * 2
        ans += (y-1) * w * count_trios((0,y-2,z+2,w-1), memo, m) * 3
        ans += choose2(z) * count_trios((0,y-1,z-1,w+2), memo, m) * 2 * 2
        ans += z * w * count_trios((0,y-1,z,w), memo, m) * 2
        ans += choose2(w) * count_trios((0,y-1,z+1,w-2), memo, m)
        memo[key] = ans % m
        return memo[key]
    if z != 0:
        ans += choose2(z-1) * count_trios((0,0,z-3,w+3), memo, m) * 2 * 2
        ans += (z-1) * w * count_trios((0,0,z-2,w+1), memo, m) * 2
        ans += choose2(w) * count_trios((0,0,z-1,w-1), memo, m)
        memo[key] = ans % m
        return memo[key]
    if w != 0:
        ans += choose2(w-1) * count_trios((0,0,0,w-3), memo, m)
        memo[key] = ans % m
        return memo[key]

def Euler475(n, m, memo={}):
    return count_trios((n/4,0,0,0), memo, m)

if __name__ == '__main__':
    print Euler475(12,1000000007)
    print Euler475(24,1000000007)
    print Euler475(600,1000000007)
                                     
                                       
