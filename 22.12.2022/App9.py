a, b = [[]], [[]]
n = float(input())
lst1, lst2 = [], []
for i in range(len(a)):
    for j in range(len(a[i])):
        if j < i:
            lst1.append(a[i][j])
lsta = []
if max(lst1) < n:
    for i in range(len(a)):
        c = 0
        for j in range(len(a[i])):
            if a[j][i] < 0:
                c += 1
        lsta.append(c)
for i in range(len(b)):
    for j in range(len(b[i])):
        if j < i:
            lst2.append(b[i][j])
lstb = []
if max(lst2) < n:
    for i in range(len(b)):
        c = 0
        for j in range(len(b[i])):
            if b[j][i] < 0:
                c += 1
        lstb.append(c)
print(lsta)
print(lstb)
