m, n = int(input()), int(input())
kn = 0
c = 1
mxc = 0
for i in range(n):
    kn += c
    c += 2
print(kn + ((c - 2) * m))
