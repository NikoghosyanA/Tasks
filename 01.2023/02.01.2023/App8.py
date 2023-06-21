n = int(input())
c = 0
for i in range(n+1):
    for j in range(n + 1):
        print(i, j)
        c += 1
print(c//2, c)
