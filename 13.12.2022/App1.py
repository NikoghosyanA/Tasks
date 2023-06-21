sm = 0


def f(n):
    global sm
    if n < 3:
        return 1
    elif n > 2 and n % 2 == 1:
        return f(n - 1) - f(n - 2)
    elif n > 2 and n % 2 == 0:
        for i in range(1, n):
            sm += f(i)
        return sm


print(f(39))
