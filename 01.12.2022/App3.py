while True:
    n = int(input())
    i = n // 2
    while True:
        if n % i == 0:
            print(i)
            break
        else:
            i -= 1
