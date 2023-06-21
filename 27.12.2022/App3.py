maxn = 1000
k1 = int(input())
m = int(input())
k2 = int(input())
p2 = int(input())
n2 = int(input())
vp = 0
vn = 0
p1 = -1
n1 = -1
for i in range(1, maxn + 1):
    inp = m * i
    tp = (((k2 - 1) // inp) + 1)
    tk = k2 - (tp - 1) * inp
    tn = (((tk - 1) // i) + 1)
    if tp == p2 and tn == n2:
        tp = (((k1 - 1) // inp) + 1)
        tk = k1 - (tp - 1) * inp
        tn = (((tk - 1) // i) + 1)
        if n1 == -1:
            n1 = tn
            vn = 1
        if p1 == -1:
            p1 = tp
            vp = 1
        if vp > 0 and tp != p1:
            vp += 1
        if vn > 0 and tn != n1:
            vn += 1
if vp == 0:
    x = -1
elif vp > 1:
    x = 0
elif vp == 1:
    x = p1
if vn == 0:
    y = -1
elif vn > 1:
    y = 0
elif vn == 1:
    y = n1
print(x, y)
