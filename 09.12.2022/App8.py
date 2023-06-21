m, n = int(input()), int(input())
A = [[10, 11, 3],
     [7, 5, 6],
     [4, 8, 9],
     [1, 11, 12]]
B = []
for i in range(n):
    c = 0
    a, b = -1, -1
    for j in range(m):
        if j > 0:
            if A[j-1][i] > A[j][i]:
                c += 1
                print(c)
            else:
                a, b = j, i
                break
    if c == m-1:
        B.append(0)
    else:
        B.append((a, b))
print(B)
