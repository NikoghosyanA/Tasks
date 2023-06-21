import math


def getdis1(cx, cy, ax, ay, bx, by):  # Расстояние от точки до прямой
    a = by - ay
    b = ax - bx
    c = bx * ay - ax * by
    dis = (math.fabs(a * cx + b * cy + c)) / (math.pow(a * a + b * b, 0.5))
    return dis


def getdis3(cx, cy, ax, ay, bx, by):  # Расстояние от точки до отрезка
    if cy > ay:
        cy, ay = ay, cy
    dist = abs(bx - cx) ** 2
    if by > ay:
        dist += (by - ay) ** 2
    elif by < cy:
        dist += (by - cy) ** 2
    print(dist ** 0.5)


