###############################################################################
# Euler 369 - Badugi
# Kelvin Blaser     2015.1.16
#
# This is a mess of loops, because why not?
# Loop over n - number of cards
#   Loop over cards in each suit (3 loops)
#       Loop over number of ways to get badugi (3 loops)
###############################################################################
from itertools import combinations

def multinomial(n,k):
    if isinstance(k,int):
        k = [k,n-k]
    k = list(k)
    if not sum(k) == n:
        k.append(n-sum(k))

    num, den = 1,1
    for x in range(2,n+1):
        num *= x
    for y in k:
        for x in range(2,y+1):
            den *= x
    return num / den

def isBadugi(alphas):
    for a in alphas[0]:
        for b in alphas[1]:
            for c in alphas[2]:
                for d in alphas[3]:
                    if len(set([a,b,c,d])) == 4:
                        return True
    return False
    

def Euler369(N):
    alpha = 'abcdefghijklm'
    ans = 0
    for n in range(4,N+1):
        for suit1 in range(1,min(n//4,13)+1):
            new1 = suit1
            used1 = new1
            a1 = alpha[:used1]
            suit1_ways = multinomial(13,new1)
            for suit2 in range(suit1,min((n-suit1)//3,13)+1):
                for new2 in range(max(0,suit2-used1),min(suit2,13-used1)+1):
                    used2 = used1 + new2
                    suit2_ways = multinomial(13-used1, new2)
                    for c2 in combinations(alpha[:used1],suit2-new2):
                        a2 = ''.join(c2) + alpha[used1:used2]
                        for suit3 in range(suit2,min((n-suit1-suit2)//2,13)+1):
                            for new3 in range(max(0,suit3-used2),min(suit3,13-used2)+1):
                                used3 = used2 + new3
                                suit3_ways = multinomial(13-used2,new3)
                                for c3 in combinations(alpha[:used2],suit3-new3):
                                    a3 = ''.join(c3) + alpha[used2:used3]
                                    suit4 = n-suit1-suit2-suit3
                                    if suit4 > 13:
                                        continue
                                    suit_count = [0]*14
                                    suit_count[suit1] += 1
                                    suit_count[suit2] += 1
                                    suit_count[suit3] += 1
                                    suit_count[suit4] += 1
                                    suit_mult = multinomial(4,suit_count)
                                    for new4 in range(max(0,suit4-used3),min(suit4,13-used3)+1):
                                        used4 = used3 + new4
                                        suit4_ways = multinomial(13-used3,new4)
                                        for c4 in combinations(alpha[:used3],suit4-new4):
                                            a4 = ''.join(c4) + alpha[used3:used4]
                                            if not isBadugi([a1,a2,a3,a4]):
                                                continue
                                            #print n, a1, a2,a3,a4,suit1_ways,suit2_ways,suit3_ways,suit4_ways,suit_mult
                                            ans += suit1_ways*suit2_ways*suit3_ways*suit4_ways*suit_mult
        #print ''
        print n, ans
    return ans

if __name__ == '__main__':
    print Euler369(52)
    
