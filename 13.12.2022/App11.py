lst = list(map(int, input().split()))
lst1 = []
for i in lst:
    if lst[-1] % 2 == 0:
        if i < lst[-1] and i % 2 == 1:
            continue
        else:
            lst1.append(i)
    elif lst[-1] % 2 == 1:
        if i < lst[-1] and i % 2 == 0:
            continue
        else:
            lst1.append(i)
print(*set(lst1))
