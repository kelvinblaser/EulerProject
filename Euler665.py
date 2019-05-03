# Euler 665 - Proportionate NIM
#   Kelvin Blaser   2019.04.19

import datetime
import json


def losing_position_sum(N):
    s = 0
    l_positions = [None]*(N+1)
    diags = [False]*(N+1)
    diag2s = set()
    l_positions[0] = 0
    diags[0] = True
    diag2s.add(0)

    diag_min = 1
    d2_lo = -1
    d2_hi = 1

    for n in range(1, N//2 + 1):
        if l_positions[n] is not None: continue
        m = n + diag_min - 1 # Start searching above the slope 1 diagonal band
        while m < N - n:
            if 2*n - d2_hi < m:
                # Skip over the slope 2 diagonal band
                m = max(m, 2*n - d2_lo - 1)
                if m >= N-n: break
            m += 1
            if l_positions[m] is not None: continue
            if diags[m-n]: continue
            if 2*m - n in diag2s: continue
            if 2*n - m in diag2s: continue
            l_positions[n] = m
            l_positions[m] = n

            # Update the slope 1 diagonals and band
            diags[m-n] = True
            while diags[diag_min]:
                diag_min += 1

            # Update the slope 2 diagonals and band
            diag2s.add(2*m - n)
            diag2s.add(2*n - m)
            while d2_lo in diag2s:
                d2_lo -= 1
            while d2_hi in diag2s:
                d2_hi += 1

            # Add to the running sum
            s += m + n
            break

    return s

if __name__ == '__main__':
    print('f({0}) = {1}'.format(10,   losing_position_sum(10)))    # Should be 21
    print('f({0}) = {1}'.format(100,  losing_position_sum(100)))   # Should be 1164
    print('f({0}) = {1}'.format(1000, losing_position_sum(1000)))  # Should be 117002
    start = datetime.datetime.now()
    print('f({0}) = {1}'.format(10**7, losing_position_sum(10**7)))
    print('Elapsed time : {}'.format(datetime.datetime.now() - start))
