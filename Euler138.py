count = 0
y = 2
L = 1

s = 0
while count < 12:
    y, L = (2*y + 5*L, y + 2*L)
    if y % 5 == 2:
        count += 1
        b = (y/5)*2
        s += L
        print '(b,h,L) = ('+str(b)+','+str(b+1)+','+str(L)+')'
    if y % 5 == 3:
        count += 1
        b = ((y/5)+1)*2
        s += L
        print '(b,h,L) = ('+str(b)+','+str(b-1)+','+str(L)+')'
print s
