s = input('Введите любимые блюда ресторана "Подсолнух":')
s1 = list(map(str, s.split(', ')))
lst = ['шоколадный торт', 'шашлык']
for i in lst:
    if i in s1:
        print(i, s.index(i[0]))
    else:
        print(i, -1)
