n = int(input())
c1, c2 = 0, 0
lst, lst1 = [], []
for _ in range(n):
    m = int(input())
    for _ in range(m):
        col = input()
        lst.append(col)
for i in range(len(lst)):
    for j in range(len(lst)):
        if i < j:
            if lst[i] not in lst1 and lst[i] == lst[j]:
                lst1.append(lst[i])
                c1 += 1
for k in lst:
    for h in lst1:
        if k == h:
            c2 += 1
print(c1, c2)
