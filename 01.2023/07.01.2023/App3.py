from math import factorial

x = 0.2
n = 1
sm = 0
e = 10 ** -5
while True:
    ans = (-1**n) * (((2 * x) ** (2 * n)) / factorial(2 * n))
    if abs(ans) < e:
        break
    sm += ans
    n += 1
    print(sm)
print(sm)
