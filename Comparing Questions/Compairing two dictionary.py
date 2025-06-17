'Comapre 2 Dictionary'

d1 = {1:2, 2:3, 3:4}
d2 = {1:2, 2:3, 3:4}

flag=0
for i in d1:
    if d1[i] != d2[i]:
        flag = 1
        break
if flag == 0:
    print('Yes')
else:
    print('No')