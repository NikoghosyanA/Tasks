from math import log, sqrt

a, b, h = float(input('a: ')), float(input('b: ')), float(input('h: '))
x = a
while True:
    if x > b:
        break
    y = log(sqrt(1/x))
    print(y)
    x += h
