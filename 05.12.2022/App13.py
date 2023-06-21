from math import log, ceil

n = int(input())
n2 = ceil(log(n) / log(2))
n2 += pow(2, n2) == n
n3 = ceil(log(n) / log(3))
n3 += pow(3, n3) == n
n5 = ceil(log(n) / log(5))
n5 += pow(5, n5) == n
res = [i * j * k for i in [pow(2, k2) for k2 in range(n2)]
       for j in [pow(3, k3) for k3 in range(n3)]
       for k in [pow(5, k5) for k5 in range(n5)] if i * j * k <= n]
print(max(res))
