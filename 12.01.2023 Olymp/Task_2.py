n, k = map(int, input().split())
c = 0
for i in range(1, n+1):
    a = bin(i)[2:]
    if a.count('0') == k:
        c += 1
print(c)
