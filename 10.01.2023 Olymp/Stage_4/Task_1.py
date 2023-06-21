n, k = map(int, input().split())
lst = list(map(int, input().split()))
c1, c2 = 0, 0
goal = k - n + 1
index = 0
for i in range(len(lst)):
    if lst[i] == 1:
        c1 += 1
    elif lst[i] == 2:
        c2 += 1
    if c1 == goal:
        index = i + 1
        break
    if c2 == goal:
        index = i + 1
        break
lst1 = []
for i in range(len(lst)):
    if i < index:
        lst1.append(0)
    else:
        lst1.append(1)
print(index)
print(*lst1)
