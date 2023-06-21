n, m = int(input()), int(input())
xn = []
xm = []
for i in range(n):
    xn.append(int(input()))
for i in range(m):
    xm.append(int(input()))
p = sum(xn) + sum(xm)
t = 0
while True:
    pp = p - n + m
    if abs(pp) > abs(p):
        break
    else:
        p = pp
        t += 1
print(t)
