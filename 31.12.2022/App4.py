N = int(input("N-"))
a = [0] * N
b = [0] * N
for i in range(N):
    a[i] = int(input())
for j in range(5, 2, -1):
    for i in range(N):
        if i < N - 1:
            if (a[i] < j) and (a[i + 1] == j) and (b[i + 1] == 0):
                a[i] = j
                b[i] = 1
        if i > 0:
            if (a[i] < j) and (a[i - 1] == j) and (b[i - 1] == 0):
                a[i] = j
                b[i] = 1
print("\n".join([str(i) for i in a]))
