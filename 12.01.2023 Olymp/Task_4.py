n = int(input())
lstx, lstv = [], []
for i in range(n):
    x, v = map(int, input().split())
    lstx.append(x), lstv.append(v)
for i in range(len(lstx) - 1):
    for j in range(len(lstx) - i - 1):
        if lstx[j] > lstx[j + 1]:
            lstx[j], lstx[j + 1] = lstx[j + 1], lstx[j]
            lstv[j], lstv[j + 1] = lstv[j + 1], lstv[j]
t = 0
ch = False
while True:
    for i in range(len(lstx)):
        lstx[i] += lstv[i]
    t += 1
    for i in range(len(lstx)):
        for j in range(len(lstx)):
            if j > i:
                if lstx[i] >= lstx[j]:
                    ch = True
                    break
        if ch:
            break
    if ch:
        print(f'{t:.5f}')
        break




