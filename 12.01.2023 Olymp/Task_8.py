n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
if n % 2 == 1:
    lst = [0] + lst
    n = (n // 2) + 1
else:
    n = n // 2
lst1 = []
lst2 = []
for i in range(n):
    lst1.append(lst[i] + lst[-(i + 1)])
for i in range(n):
    for j in range(n):
        if j > i:
            lst2.append(abs(lst1[i] - lst1[j]))
print(min(lst2))
