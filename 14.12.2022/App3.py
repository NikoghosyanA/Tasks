a, b, c = int(input()), int(input()), int(input())
d = (b ** 2) - (4 * a * c)
if d > 0:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print(x2, x1)
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    pass
