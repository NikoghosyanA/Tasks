M1, Y1, M2, Y2 = map(int, input('Введите M1,Y1,M2,Y2 через пробел: ').split())
if Y1 < 1:
    Y1 += 1
if Y2 < 1:
    Y2 += 1
print(12 * (Y2 - Y1) + M2 - M1 + 1)
