def f(n):
    t = False
    for i in range(1, n):
        for j in range(1, n):
            if i ** 2 + j ** 2 == n:
                t = True
                break
        if t:
            break
    if t:
        return True
    else:
        return False


n = int(input())
for i in range(n):
    if f(i):
        print(i)
