m, n, k = map(int, input().split())
c2 = 0
lst = []
for i in range(k):
    c1 = 0
    r, c, d = map(int, input().split())
    for h in range(1, m+1):
        for j in range(1, n+1):
            if abs(h - r) + abs(j - c) <= d and (h, j) not in lst:
                lst.append((h, j))
                c1 += 1
    c2 += c1
print(m*n - c2)
