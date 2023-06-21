from math import *

eps = float(input('Введите eps = '))
x = float(input('Введите x = '))
summ = 0
n = 0

while True:
    an = ((-1**n) * factorial(2*n) * (x**(2 * n + 1))) / ((2**(2*n)) * (factorial(n)**2) * (2*n + 1))
    if abs(an) < eps:
        break
    n += 1
    summ += an
print(summ)
