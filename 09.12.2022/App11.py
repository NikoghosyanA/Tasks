a, b, c, d = map(int, input().split())
x, y = map(int, input().split())
h = ((c**2) - (((a - b)**2) / 4))
if a <= x and h <= y:
    print('Yes')
else:
    print('No')
