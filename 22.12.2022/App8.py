a, b = [[]], [[]]
na, nb = False, False
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] < 0:
            na = True
    if na:
        break
for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j] < 0:
            nb = True
    if nb:
        break
if na:
    for i in range(len(b)):
        b[i] = [max(b[i])]
    print(b)
elif nb:
    for i in range(len(a)):
        a[i] = [max(a[i])]
    print(a)
