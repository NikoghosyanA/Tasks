a, b = int(input()), int(input())
c = 0
if b % 2 == 0:
    if a % 2 == 0:
        for i in range(b):
            a += 2
            c += 1
            if a == b:
                print(c)
                break
    if a % 2 == 1:
        a += 1
        for i in range(b):
            a += 2
            c += 1
            if a == b:
                print(c)
                break
elif b % 2 == 1:
    if a % 2 == 1:
        for i in range(b):
            a += 2
            c += 1
            if a == b:
                print(c)
                break
    if a % 2 == 0:
        a += 1
        for i in range(b):
            a += 2
            c += 1
            if a == b:
                print(c)
                break
