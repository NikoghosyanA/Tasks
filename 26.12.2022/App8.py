x, y = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if (x1 == x or y1 == y) and (x2 == x or y2 == y):
    print('double')
else:
    print('no')
