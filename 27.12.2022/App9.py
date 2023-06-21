from math import factorial

sm = 0
n = 1
x = int(input())
e = 0.00001
while True:
    sn = (((0.3 * x) + 5) ** ((2 * n) - 1)) / factorial((2 * n) + 3)
    if abs(sn) < e:
        break
    sm += sn
    n += 1
print(sm)
