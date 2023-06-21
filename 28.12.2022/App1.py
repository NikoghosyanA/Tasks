c1, c2, mn1, mn2 = 0, 0, 11110, 11110
for i in range(10101, 11111):
    if i % int('100', base=2) == 0 and i % int('100', base=8) == 0 and i % int('100', base=16) == 0:
        c1 += 1
        if i < mn1:
            mn1 = i
    if i % int('110', base=2) != 0 and i % int('12', base=8) != 0 and i % int('3A', base=16) != 0:
        c2 += 1
        if i < mn2:
            mn2 = i
print(c1, mn1)
print(c2, mn2)
