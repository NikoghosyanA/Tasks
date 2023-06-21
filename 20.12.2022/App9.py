n = input()
i, j = 0, 2
mn = '0'
while True:
    a, b = int(n[i:j]), int(n[i:j][::-1])
    if a % 16 == b % 16:
        if a < b and a < int(mn):
            mn = str(a)
        elif b < a and b < int(mn):
            mn = str(b)
    if j == len(n):
        break
    i += 1
    j += 1
c, d = 0, 0
if mn != '0':
    c, d = int(mn[0]), int(mn[1])
    if c <= d:
        print(2)
    else:
        print(1)
else:
    print(0)
