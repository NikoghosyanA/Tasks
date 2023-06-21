n = int(input())
lstx, lsty = [], []
for i in range(n):
    x, y = map(int, input().split())
    lstx.append(x)
    lsty.append(y)
t = False
for i in range(n):
    for j in range(n):
        for k in range(n):
            if k > j > i:
                x1, y1, x2, y2, x3, y3 = lstx[i], lsty[i], lstx[j], lsty[j], lstx[k], lsty[k],
                if (x3 - x1) / (x2 - x1) == (y3 - y1) / (y2 - y1):
                    continue
                else:
                    t = True
                    print('Yes')
                    print(i+1, j+1, k+1)
                    break
        if t:
            break
    if t:
        break
else:
    print('No')

