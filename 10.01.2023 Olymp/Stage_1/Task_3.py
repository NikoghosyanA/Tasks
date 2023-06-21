from itertools import combinations

n, k = map(int, input().split())
s = input()
lst = [str(i+1) for i in range(n)]
comb = combinations(lst, k)
nxt = False
lst1 = []
for i in comb:
    if nxt:
        lst1 = list(i)
        break
    if ' '.join(i) == s:
        nxt = True
if len(lst1) > 0:
    print(' '.join(lst1))
else:
    print(-1)
