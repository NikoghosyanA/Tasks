m, n = int(input()), int(input())
lst1, lst2 = [], []
for i in range(m):
    lst1.append(input())
for i in range(n):
    lst2.append(input())
c = 0
for i in lst1:
    if i not in lst2:
        c += 1
print(c)
