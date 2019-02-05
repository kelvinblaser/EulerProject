# Euler 179
# Kelvin Blaser  2013-04-11
import scipy as sp

N = 10**7
num_divs = sp.ones(N)
nums = sp.ones(N)
for ix in range(2,N):
    nums[ix] = ix
for ix in range(2, N):
    if nums[ix] == ix:
        print ix
        for jx in range(1, N/ix+1):
            count = 1
            if jx*ix < N:
                while nums[jx*ix] % ix == 0:
                    nums[jx*ix] /= ix
                    count += 1
                num_divs[jx*ix] *= count

count = 0
for ix in range(2, N-1):
    if num_divs[ix] == num_divs[ix+1]:
        count += 1
print count
