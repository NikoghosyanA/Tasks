from itertools import combinations

n = int(input())
lst = []
for i in range(n):
    lst.append(i)
ans = 0
if n >= 2:
    for i in range(2, n+1):
        comb = list(combinations(lst, i))
        ans += len(comb)
print(ans)
