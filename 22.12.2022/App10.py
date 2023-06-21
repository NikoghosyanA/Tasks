a, b = [[]], [[]]
n = float(input())
na, nb = False, False
for i in range(len(a)):
    for j in range(len(a[i])):
        if j > i:
            if a[i][j] % n != 0:
                na = True
    if na:
        break
for i in range(len(b)):
    for j in range(len(b[i])):
        if j > i:
            if b[i][j] % n != 0:
                nb = True
    if nb:
        break
if na:
    c = 0
    for i in range(len(b)):
        if sum(b[i]) < 0:
            c += 1
    print(c)
elif nb:
    c = 0
    for i in range(len(a)):
        if sum(a[i]) < 0:
            c += 1
    print(c)
