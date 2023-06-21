n = int(input())
m = int(input())
if n > m:
    n = m
L = 0
R = n + 2
while R - L > 1:
    mid = (L + R) // 2
    if (mid + n) * (n - mid + 1) // 2 >= m:
        L = mid
    else:
        R = mid
if (L + n) * (n - L + 1) // 2 < m:
    print(0)
else:
    for i in range(R, n + 1):
        print(i // 2)
    s = (R + n) * (n - R + 1) // 4
    if m - s > 0:
        print(m - s)
