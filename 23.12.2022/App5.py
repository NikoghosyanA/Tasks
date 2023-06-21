from math import log


def _rectangle_rule(func, a, b, nseg, frac):
    """Обобщённое правило прямоугольников."""
    dx = 1.0 * (b - a) / nseg
    sum = 0.0
    xstart = a + frac * dx # 0 <= frac <= 1 задаёт долю смещения точки,
                           # в которой вычисляется функция,
                           # от левого края отрезка dx
    for i in range(npoints):
        sum += func(xstart + i * dx)

    return sum * dx

def left_rectangle_rule(func, a, b, nseg):
    """Правило левых прямоугольников"""
    return _rectangle_rule(func, a, b, nseg, 0.0)

def right_rectangle_rule(func, a, b, nseg):
    """Правило правых прямоугольников"""
    return _rectangle_rule(func, a, b, npoints, 1.0)

def midpoint_rectangle_rule(func, a, b, nseg):
    """Правило прямоугольников со средней точкой"""
    return _rectangle_rule(func, a, b, nseg, 0.5)

def fn(x):
    return (log(x) ** 2) / x
