# Euler 163 - Cross Hatched Triangles
# Kelvin Blaser
# 2013.12.27
#
# O(n^2) counting of each type of triangle

def Euler163(n=36):
    ans = 0
    for x in range(n+1):
        for y in range(n-x+1):
            ans += n-x-y
            ans += min(x, n-x-y)

            ans += 6*(n-x-y)
            ans += 6*min(y, 2*x)

            ans += 3*min(y, n-x-y)
            ans += 3*min(x, n-x-y)

            ans += 6*((3*(n-x-y))//2)
            ans += 6*min(2*x, 3*y)

            ans += 3*(n-x-y)
            ans += 3*min(x, 3*y)

            ans += 2*min((3*(n-x-y))//2, 3*y)
            ans += 2*max(min((3*(n-x-y))//2-1, 3*y+1),0)
            ans += 2*max(min((3*(n-x-y))//2-2, 3*y+2),0)

    return ans

if __name__ == '__main__':
    print Euler163(), 'triangles'
