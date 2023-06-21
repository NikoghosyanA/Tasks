from math import cos, factorial
sm = 0
n = int(input())
x = float(input())
for i in range(n):
    sm += (((-1)**i) * ((x**(2*i)) / factorial(2 * i)))
print(cos(x))
print(sm)
