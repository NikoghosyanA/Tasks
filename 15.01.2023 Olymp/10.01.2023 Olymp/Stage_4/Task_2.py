def count(n, k):
    if n == 0:
        global c
        c += 1
    for i in range(k, n + 1):
        if i % 2 != 0:
            a.append(i)
            count(n - i, i)
            a.pop(len(a) - 1)


a = []
c = 0
n = int(input())
count(n, 1)
print(c)
