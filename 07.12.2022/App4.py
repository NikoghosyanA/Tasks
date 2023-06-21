a, b = map(int, input('Введите дробные числа вида 1/2: ').split('/'))
c, d = map(int, input().split('/'))
print(str(a * d + b * c) + '/' + str(b * d))
