a = int('1110', base=2)
b = int('122', base=3)
c = a / 2
d = int('30', base=4)
ans = c + (b - d)
digits = []
while ans:
    digits.append(str(int(ans % 5)))
    ans //= 5
print(''.join(digits[::-1]))
