from random import randint

level = int(input('Выберите уровень сложности(1/2/3):\n1. Легко\n2. Средне\n3. Сложно\n'))
i = 0
grade = 0
if level == 1:
    while i < 5:
        a = randint(1, 5)
        b = randint(1, 5)
        ans = int(input(f'{a} * {b} = '))
        if ans == a * b:
            print('Правильно!')
            i += 1
            grade += 1
        else:
            print('Неправильно')
            i += 1
elif level == 2:
    while i < 10:
        a = randint(2, 10)
        b = randint(6, 10)
        ans = int(input(f'{a} * {b} = '))
        if ans == a * b:
            print('Правильно!')
            i += 1
            grade += 1
        else:
            print('Неправильно')
            i += 1
elif level == 3:
    while i < 20:
        a = randint(10, 20)
        b = randint(10, 20)
        ans = int(input(f'{a} * {b} = '))
        if ans == a * b:
            print('Правильно!')
            i += 1
            grade += 1
        else:
            print('Неправильно')
            i += 1
print(f'Вы набрали {grade} из {i}')
