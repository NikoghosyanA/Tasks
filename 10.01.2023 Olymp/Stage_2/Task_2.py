r, c, q = map(int, input().split())
s = list(map(int, input().split()))
lst = [[0 for i in range(c)] for j in range(r)]
a = 1
for i in range(r+c-1):
    for j in range(r):
        if -1 < (i - j) < c:
            lst[j][i-j] += a
            a += 1
for i in lst:
    print(*i)
for v in s:
    for i in range(r):
        for j in range(c):
            if v == lst[i][j]:
                print(i + 1, j + 1)
