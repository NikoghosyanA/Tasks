import random

lst = []
while True:
    n = input('Название фильма: ')
    if n == 'stop':
        break
    if n not in lst:
        lst.append(n)
while True:
    n = int(input('1.Вывести список фильмов\n'
                  '2.Добавить фильм\n'
                  '3.Удалить фильм по названию\n'
                  '4.Удалить фильм по номеру\n'
                  '5.Показать фильм по названию\n'
                  '6.Показать случайный фильм в случайном зале\n'
                  '0.Выход\n'
                  'Введите 1/2/3/4/5/6/0: '))
    if n == 1:
        print(*lst)
    elif n == 2:
        a = input('Название фильма: ')
        if a not in lst:
            lst.append(a)
            print('Добавлено.')
        else:
            print('Данный фильм присутствует в списке.')
    elif n == 3:
        a = input('Название фильма: ')
        if a in lst:
            lst.remove(a)
            print('Удалено.')
        else:
            print('Данный фильм отсутствует в списке.')
    elif n == 4:
        a = int(input('Номер фильма: '))
        if a in range(len(lst) + 1):
            lst.pop(a - 1)
            print('Удалено.')
        else:
            print('Данный номер не соответствует количеству фильмов.')
    elif n == 5:
        a = input('Название фильма: ')
        if a in lst:
            print(f'В зале {random.randint(1, 10)} показывают фильм {a}')
        else:
            print('Данный фильм отсутствует в списке.')
    elif n == 6:
        a = random.choice(lst)
        print(f'В зале {random.randint(1, 10)} показывают фильм {a}')
    elif n == 0:
        break
