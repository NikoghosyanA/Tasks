form = [0, 0, 0]
for i in range(10):
    x, y = map(int, input().split())
    if 0 <= x < 40 and 0 <= y <= 80:
        form[0] += 1
    elif 40 < x < 80 and 0 <= y <= 80:
        form[1] += 1
    elif 80 < x <= 120 and 0 <= y <= 80:
        form[2] += 1
k = 0
lst = []
for z in range(1, 6):
    for pz in range(1, 6):
        for n in range(4):
            if z + pz + n == 10 and abs(z - form[0]) <= 2 and abs(pz - form[1]) <= 2 and abs(n - form[2]) <= 2:
                k += 1
                lst.append((str(z), str(pz), str(n)))
print(k)
for i in lst:
    print('-'.join(i))
