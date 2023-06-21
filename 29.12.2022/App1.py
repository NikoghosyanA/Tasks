lst = list(map(int, input().split()))
sm = 0
c = 0
sm2 = 0
for i in lst:
    if i % 2 == 0:
        sm += i
        c += 1
    if i % 3 == 0 and i % 6 == 0:
        sm2 += i
sr = sm / c
print((sr / 2) / 3)
print((sm2 / 4) ** 2)
