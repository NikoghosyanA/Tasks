from itertools import permutations

n, k = map(int, input().split())
lst = []
for i in range(n):
    lst.append(i+1)
p = permutations(lst)
count = 0
for i in list(p):
    i = list(i)
    b = 0
    for j in range(1, len(i)):
        b += i[j-1] * i[j]
    if b % k == 0:
        count += 1
print(count)
