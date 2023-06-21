n, m = 8, 3
a = [[]]
c = 0
for i in range(n):
    for j in range(m):
        if a[i][j] >= 0:
            c += 1
print(c)
b = [[]]
for i in range(n):
    for j in range(m):
        b[i].append(-a[i][j])
print(b)
