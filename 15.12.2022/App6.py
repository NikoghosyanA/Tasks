x, y = float(input()), float(input())
if (-200 <= x <= -100 and -x >= y >= 0 and (x ** 2) + (y ** 2) <= 40000) or (-200 <= y <= 0 and 0 <= x <= 200 and (x ** 2) + (y ** 2) <= 40000):
    print('Yes')
else:
    print('No')
