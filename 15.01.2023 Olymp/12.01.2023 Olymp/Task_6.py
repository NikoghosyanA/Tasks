l, r = map(int, input().split())
c = 0
for i in range(l, r + 1):
    lst = []
    for j in range(10):
        if str(i).count(str(j)) <= 2:
            lst.append(1)
        else:
            lst.append(0)
    if 0 not in lst:
        c += 1
print(c)
