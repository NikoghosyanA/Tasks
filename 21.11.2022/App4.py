n = int(input("n: "))
a = [0] * n
b = [0] * n
for i in range(n):
    a[i] = int(input())
for j in range(5, 2, -1):
    for i in range(n):
        if i < n - 1:
            if (a[i] < j) and (a[i + 1] == j) and (b[i + 1] == 0):
                a[i] = j
                b[i] = 1
        if i > 0:
            if (a[i] < j) and (a[i - 1] == j) and (b[i - 1] == 0):
                a[i] = j
                b[i] = 1
print("\n".join([str(i) for i in a]))
