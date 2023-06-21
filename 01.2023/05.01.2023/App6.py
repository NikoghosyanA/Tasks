n = int(input())
lst1, lst2 = [], []
for i in range(n):
    k, v = map(int, input().split())
    lst1.append(k), lst2.append(v)

for i in range(n - 1):
    for j in range(n - i - 1):
        if lst2[j] > lst2[j + 1]:
            lst2[j], lst2[j + 1] = lst2[j + 1], lst2[j]
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
lst1, lst2 = lst1[::-1], lst2[::-1]
for i in range(n):
    print(lst1[i], lst2[i])
