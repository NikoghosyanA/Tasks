[n, m], s = map(int, input().split()), 0
for _ in range(m):
    l, r, k = map(int, input().split())
    s += (r - l + 1) - (k == 2) * ((r - 1) // 2 - l // 2 + 1)
print(s / n)
