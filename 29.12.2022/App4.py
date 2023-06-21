c = 0
sm = 0
for i in range(20000, 25000):
    if i % 6 == 0 and i % 8 == 0 and str(i)[-1] != '2':
        c += 1
    if i % 3 == 0 and int(str(i // 3)[-1]) % 2 == 0:
        sm += i
print(c, sm)
