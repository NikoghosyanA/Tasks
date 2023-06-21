from math import log, sin


def s(x, y):
    if x / y > 0:
        return '(x + ln(|y|))^3', (x + log(abs(y))) ** 3
    elif x / y < 0:
        return '2/3 + ln(|sin(y)|)', 2/3 + log(abs(sin(y)))
    else:
        return 'x^2/3 + y', (x ** (2/3)) + y


print(s(float(input('x: ')), float(input('y: '))))
