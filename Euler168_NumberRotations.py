# Euler 168 - Number Rotations
# http://projecteuler.net/problem=168
#
# Kelvin Blaser - 2014.02.11

def find_rotation_list(k, a0):
    a = [0]*100
    c = [0]*100
    a[0] = a0
    c[0] = (a0*k)/10
    a[1] = (a0*k)%10
    for i in range(1,99):
        c[i]   = (a[i]*k + c[i-1]) / 10
        a[i+1] = (a[i]*k + c[i-1]) % 10
        if (a[i+1] * k + c[i]) % 10 == a0 and (a[i+1]*k+ c[i])/10 == 0:
            if a[i+1] == 0:
                return None
            return a[:i+2]
    return None

def first_five(a_list):
    x = 0
    for i in range(5):
        x *= 10
        x += a_list[4-i]
    return x

def digit_string(a_list):
    s = ''
    for d in a_list:
        s = str(d)+s
    return s

def repunit(n):
    ans = 0
    for i in range(n):
        ans *= 10
        ans += 1
    return ans

def Euler168():
    ans = sum(sum(j*repunit(n) for n in range(2,5)) for j in range(1,10))
    ans += sum(j*repunit(5)*96 for j in range(1,10))
    print ans
    for k in range(2,10):
        for a0 in range(1,10):
            a_list = find_rotation_list(k,a0)
            if a_list:
                print '%d: %s'%(k,digit_string(a_list))
                ans += first_five(a_list) * (100 / len(a_list))
    return ans%100000
