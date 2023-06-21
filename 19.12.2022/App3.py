def fun():
    n, m = map(int, input().split())
    amax, amin = set(), set()
    arr = [list(map(int, input().split())) for i in range(n)]
    arrt = list(map(list, zip(*arr)))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == min(arr[i]):
                amin.add((i + 1, j + 1))
            if arrt[j][i] == max(arrt[j]):
                amax.add((i + 1, j + 1))

    res = sorted(list(amin & amax))
    if res:
        for i in res:
            print(*i)
    else:
        print(0)


fun()
