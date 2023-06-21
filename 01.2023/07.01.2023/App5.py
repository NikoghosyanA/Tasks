n = int(input())
d = int(input())
c = 0
while True:
    if d == 1:
        c += 1
        n -= 1
        d += 1
    elif d == 7 and n < 7:
        break
    elif d == 7 and n >= 7:
        c += 1
        n -= 1
        d = 1
    elif c != 0:
        c += 1
        d += 1
        n -= 1
    else:
        n -= 1
        d += 1
print(c)
