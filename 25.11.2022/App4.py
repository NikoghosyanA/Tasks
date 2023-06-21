n, m = map(int, input('Задайте диапазон(a b): ').split())
lst1, lst2, lst3 = [], [], []
for i in range(n, m):
    c1, c2 = 0, 0
    for j in range(2, i):
        if i != 2 and i % j == 0:
            c1 += 1
    if c1 == 0:
        lst1.append(i)
    for j in range(2, i):
        if i % j == 0 and i > 3:
            c2 += 1
    if c2 >= 1:
        lst2.append(i)
for i in range(n, m):
    for j in lst1:
        if i % j == 0:
            lst3.append(i)
            break
