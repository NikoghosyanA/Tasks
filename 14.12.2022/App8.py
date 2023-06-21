import random

n, m = int(input()), int(input())
mt = []
for i in range(n):
    lst = []
    for j in range(m):
        lst.append(random.randint(-50, 50))
    mt.append(lst)
print(mt)
lst1 = []
for i in range(n):
    sm = 0
    for j in range(m):
        if mt[i][j] % 2 == 0:
            sm += mt[i][j]
    lst1.append(sm/m)
    print(i, sm/m)
print(max(lst1))
