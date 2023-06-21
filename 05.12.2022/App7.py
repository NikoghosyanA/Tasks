from math import ceil
n, k = map(int, input().split())
a, b, c = ceil((n*2) / k), ceil((n*5) / k), ceil((n*8) / k)
print(a + b + c)
