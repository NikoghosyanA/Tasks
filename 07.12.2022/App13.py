x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
a1, a2 = x2 - x1, y2 - y1
b1, b2 = x3 - x2, y3 - y2
c1, c2 = x4 - x3, y4 - y3
d1, d2 = x1 - x4, y1 - y4
if a1 * b1 + a2 * b2 == 0:
    if a1 * c1 + a2 * c2 == 0:
        print('Yes')
    elif a1 * d1 + a2 * d2 == 0:
        print('Yes')
    else:
        print('N')
elif a1 * c1 + a2 * c2 == 0:
    if a1 * d1 + a1 * d2 == 0:
        print('Yes')
    else:
        print('No')
elif b1 * c1 + b2 * c2 == 0:
    if b1 * d1 + b2 * d2 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
