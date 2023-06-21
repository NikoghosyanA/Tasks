a, b, n = map(int, input().split())
step = (b - a) / n
i = 0
lstx, lsty = [], []
while True:
    if i == 0:
        lstx.append(f"{a:.{3}f}")
        y = ((2*a) - 1) / ((a**2) + 1)
        lsty.append(f"{y:.{6}f}")
    else:
        a += step
        lstx.append(f"{a:.{3}f}")
        y = ((2 * a) - 1) / ((a ** 2) + 1)
        lsty.append(f"{y:.{6}f}")
    if a == b:
        break
    i += 1
with open('output.txt', 'a') as f:
    for i in range(len(lstx)):
        f.write(lstx[i] + '\t' + lsty[i] + '\n')
