a, b = int(input()), int(input())
a1 = a
d = 1
while True:
    a -= b
    a += a1
    b += 1
    d += 1
    if a < b:
        print(d)
        break
