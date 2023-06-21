n = int(input())
ans = 0
if n % 2 == 0:
    ans = n * (n + 2) * (2 * n + 1) / 8
else:
    ans = (n + 1) * (2 * n * n + 3 * n - 1) / 8
print(round(ans))
