from math import sin, cos, log2, pi

k = 1
a = float(input())
while True:
    y = ((sin(pi) / cos(pi)) / sin(pi/4)) + ((log2(k**4) + (2*(k**2)) - (3+k) + 9) / (k**0.5))
    if y < a:
        print(k)
        break
    else:
        k += 1
