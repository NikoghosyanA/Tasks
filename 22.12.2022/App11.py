a, b = [[]], [[]]
n = float(input())
ca, cb = 0, 0
for i in range(len(a)):
    if 0 in a[i]:
        ca += 1
for i in range(len(b)):
    if 0 in b[i]:
        cb += 1
if ca == cb:
    for i in range(len(a)):
        aa = min(a[i])
        bb = min(a[i])
        i1, j1, i2, j2 = -1, -1, -1, -1
        for j in range(len(a[i])):
            if 0 > a[i][j] >= aa:
                aa = a[i][j]
                i1, j1 = i, j
            if b[i][j] < 0 and b[i][j] >= bb:
                bb = b[i][j]
                i2, j2 = i, j
        a[i1][j1], b[i2][j2] = b[i2][j2], a[i1][j1]
print(a)
print(b)
