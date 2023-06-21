from math import sin

p = 1
while True:
    x = float(input())
    if abs(x) < 5:
        break
    p *= sin(x)
print(p)
