n = int(input())
m = [[i * j for i in range(1, n+1)] for j in range(1, n+1)]
for line in m:
    print(line)
summ = 0
for i in range(n):
    for j in range(n):
        if i == j:
            summ += m[i][j]
print(summ)
