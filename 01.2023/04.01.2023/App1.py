from math import cos, radians, pi

print(cos(radians(float(input()))))

e = 8.85 * 10**(-12)
k = 1 / (4 * pi * e)
ro = 10 * 10**(-6)
r, R = 0.1, 0.01
E = (4 * k * pi * ro * (R ** 2)) / (r ** 2)
print('a)', E)
r, R = float(input('r: ')), float(input('R: '))
E = (4 * k * pi * ro * (R ** 2)) / (r ** 2)
print('b)', E)
