from random import randint
number = randint(1, 10)
c = 5
while True:
    n = int(input())
    if n == number:
        print('Вы угадали!')
        break
    else:
        print('Попробуйте еще раз!')

# punkt 2
while True:
    n = int(input())
    if n == number:
        print('Вы угадали!')
        break
    else:
        c -= 1
    if c == 0:
        print('Попытки закончились!')
        break
