while True:
    n = input('Введите число: ')
    if n == '0':
        print('Программа завершена!')
        break
    else:
        print('Число наоборот:', int(n[::-1]))
