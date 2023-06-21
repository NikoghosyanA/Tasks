a = int(input())
A = list(map(int, input().split()))
m = [[0, 0, 0]]
for i in range(a):
    if A[i] != 5:
        n = [i + 1]
        x = 0
        while A[i] != 5:
            x += 5 - A[i]
            i += 1
            if i == a:
                break
        n.append(i)
        n.append(x)
        if n[2] > m[0][2]:
            m = [[0, 0, 0]]
            m[0] = n
        elif n[2] == m[0][2]:
            m.append(n)
for row in m:
    print(*row)
