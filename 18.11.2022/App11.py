def func1(num):
    l, r = str(num)[:3], str(num)[3:]
    if int(r[0]) + int(r[1]) + int(r[2]) == int(l[0]) + int(l[1]) + int(l[2]):
        return 'Счастливый!'
    else:
        return 'Не повезло:('


def func2(a, b, c, d, e, f):
    if a + b + c == d + e + f:
        return 'Счастливый!'
    else:
        return 'Не повезло:('


def func3(left, right):
    if int(str(left)[0]) + int(str(left)[1]) + int(str(left)[2]) == int(str(right)[0]) + int(str(right)[1]) + int(str(right)[2]):
        return 'Счастливый!'
    else:
        return 'Не повезло:('