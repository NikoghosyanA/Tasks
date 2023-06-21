a, b, s = int(input('первая сторона')), int(input('вторая сторона двора')), int(input('S'))
print(0 if a * b <= s else a * b - s)
