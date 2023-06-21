from itertools import combinations

n, k = map(int, input().split())
t = list(map(int, input().split()))
lst = [i+1 for i in range(n-1)]
ans = []
mx = 0
comb = combinations(lst, k - 1)
for i in comb:
    s = 0
    for j in range(k):
        if j == 0:
            s += min(t[:i[j]])
        elif j == k - 1:
            s += min(t[i[j-1]:])
        else:
            s += min(t[i[j-1]:i[j]])
    if s > mx:
        mx = s
        ans = list(i)
print(mx)
print(*ans)
