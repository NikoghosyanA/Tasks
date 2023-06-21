n = int(input())
a = list(map(int, input().split()))
suma = sum(a)
res = suma
t, l, r = 0, 0, 0
for i in range(n - 1):
    t += a[i]
    s1 = t / (i + 1)
    s2 = (suma - t) / (n - i - 1)
    s11 = sum([j - s1 for j in a[:i + 1] if j > s1]) + sum([j - s2 for j in a[i + 1:] if j > s2])
    if res > s11:
        res = s11
        l = i + 1
        r = n - i - 1
print(l, r)
