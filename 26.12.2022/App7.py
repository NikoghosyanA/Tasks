def sqc(xa, ya, xb, yb, xc, yc):
    return ((xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)) / 2


xa, ya, xb, yb = map(float, input().split())
n, m = map(int, input().split())
astra = []
sc = []
res, smax = 0, 0
for i in range(n):
    xc, yc = map(float, input().split())
    astra.append((xc, yc))
    sctmp = sqc(xa, ya, xb, yb, xc, yc)
    if smax < abs(sctmp):
        smax = abs(sctmp)
    # print(sctmp)
    sc.append(sctmp)
for i in range(m):
    xc, yc = map(float, input().split())
    sp = sqc(xa, ya, xb, yb, xc, yc)
    if smax < abs(sp):
        smax = abs(sp)
    # print(sp)
    for j in range(n):
        xd, yd = astra[j][0], astra[j][1]
        if sp * sc[j] < 0:
            if smax < abs(sp * sc[j]):
                smax = abs(sp * sc[j])
print('{:.2f}'.format(smax))
