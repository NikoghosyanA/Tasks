while True:
    a = int(input('0 для выхода: '))
    if a == 0:
        break
    i = (a // 2 + 1)
    while True:
        if a > 2:
            if a % i == 0:
                print(i)
                break
            else:
                i -= 1
        elif a == 2:
            print(1)
            break
        else:
            print('error')
            break
