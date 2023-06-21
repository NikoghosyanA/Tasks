def f(x, y, a, b, c, d):
    if x > 3 and x * y < 2:
        return max((3**(x + a)), c + d, min(x, a))
    elif x > 3 and x * y > 2:
        return min(x, a, c, y, d)
    else:
        3 * c + d * x
