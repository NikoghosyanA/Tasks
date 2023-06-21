lst = list(map(int, input().split()))
lst1 = []
for i in lst:
    if (sum(lst) / len(lst)) - lst[0] <= i <= lst[0] + (sum(lst) / len(lst)):
        lst1.append(i)
print(*set(lst1))
