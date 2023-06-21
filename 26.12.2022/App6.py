def f(n, s=''):
    if n == 0:
        return s
    elif n % 3 == 0 or (n - 1) % 3 == 0 and n - 1 != 0:
        if n % 3 == 0:
            return f(n // 3, s+'3')
        elif (n - 1) % 3 == 0:
            return f((n - 1) // 3, s+'13')
    elif n % 2 == 0 or (n - 1) % 2 == 0 and n - 1 != 0:
        if n % 2 == 0:
            return f(n // 2, s+'2')
        elif (n - 1) % 2 == 0:
            return f((n - 1) // 2, s+'12')
    else:
        return f(n-1, s+'1')


ln = [10, 15, 30, 49, 77, 95, 137, 286, 579, 995]
for n in ln:
    print(n, ':', f(n, ''))
