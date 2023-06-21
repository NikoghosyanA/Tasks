t = int(input())
ans = []
for _ in range(t):
    kings = []
    m, n = map(int, input().split())
    for _ in range(n):
        kings.append(tuple(map(int, input().split())))
    board1 = [[0 for _ in range(m)] for _ in range(m)]
    for i in kings:
        x, y = i[1]-1, i[0]-1
        for i1 in range(-1, 2):
            for j1 in range(-1, 2):
                x1, y1 = x + i1, y + j1
                if x1 in range(m) and y1 in range(m):
                    if i1 == 0 and j1 == 0:
                        board1[x1][y1] = -2
                    else:
                        board1[x1][y1] = -1
    queens = []
    for i in range(m):
        for j in range(m):
            c = 0
            board2 = [[0 for _ in range(m)] for _ in range(m)]
            for i1 in range(m):
                for j1 in range(m):
                    if board2[i1][j1] == 0:
                        if i1 == i and j1 == j:
                            board2[i1][j1] = -4
                        elif i1 != i and j1 == j:
                            board2[i1][j1] = -3
                        elif i1 == i and j1 != j:
                            board2[i1][j1] = -3
                        elif abs(i1 - i) == abs(j1 - j):
                            board2[i1][j1] = -3
            for i2 in range(m):
                for j2 in range(m):
                    if board1[i2][j2] == -2 and board2[i2][j2] == -3 and board1[i2][j2] != -1:
                        c += 1
            if c == n:
                if board1[i][j] != -1:
                    board1[i][j] = n
                    queens.append((i, j))
    ans.append(len(queens))
for i in ans:
    print(i)
