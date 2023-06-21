a, b = [[]], [[]]
lst1, lst2 = [], []
for i in range(len(a)):
    for j in range(len(a[i])):
        lst1.append(a[i][j])
for i in range(len(b)):
    for j in range(len(b[i])):
        lst2.append(b[i][j])
sma, smb = sum(lst1), sum(lst2)
sra, srb = sma / (len(a) * len(a[0])), smb / (len(b) * len(b[0]))
mn1, mn2 = False, False
if sra == srb:
    i1, i2 = -1, -1
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[j][i] == min(lst1):
                i1 = i
                mn1 = True
        if mn1:
            break
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[j][i] == min(lst2):
                i2 = i
                mn2 = True
        if mn2:
            break
    if i1 < i2:
        print('Answer: a', i1)
    elif i2 < i1:
        print('Answer: b', i2)
    else:
        print('Equal', i1, i2)
