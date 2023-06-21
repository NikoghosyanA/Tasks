from math import factorial

x, k = map(int, input().split())
n = (x // 5) + k
ans = factorial(n) / (factorial(k) * factorial(n - k))
print(round(ans))
