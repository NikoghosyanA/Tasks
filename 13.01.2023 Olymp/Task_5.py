m, n, k = map(int, input().split())
lst = []
for _ in range(k):
    a, b, c, d, e = map(int, input().split())
    lst.append([e, a, b, c, d])
lst = sorted(lst)
sm = 0
bz = []
for i in range(k):
    p, r, c, h, w = map(int, lst[i])
    xs, ys = [], []
    for y in range(r, r + h + 1):
        for x in range(c, c + w + 1):
            xs.append(x)
            ys.append(y)
    for j in range(k):
        xss, yss = [], []
        if j > i:
            p1, r1, c1, h1, w1 = map(int, lst[j])
            for y1 in range(r1, r1 + h1 + 1):
                for x1 in range(c1, c1 + w1 + 1):
                    if y1 in ys and x1 in xs:
                        yss.append(y1)
                        xss.append(x1)
        if bz:
            for q in range(len(bz)):
                if (max(yss) in range(bz[q][0][0], bz[q][0][1] + 1) and max(xss) in range(bz[q][1][0], bz[q][1][1] + 1)) \
                        and (min(yss) in range(bz[q][0][0], bz[q][0][1] + 1) and min(xss) in range(bz[q][1][0],
                                                                                                   bz[q][1][1] + 1)):
                    break
            else:
                p -= ((max(yss) - min(yss)) * (max(xss) - min(xss))) * ((h * w) / p)
                bz.append([(min(yss), max(yss)), (min(xss), max(xss))])
    sm += p
print(sm)
