import tabulate

f = open('input.txt', 'r')
dct = {}
for line in f:
    lst = list(map(str, line.split()))
    if lst[0] not in dct.keys():
        dct[lst[0]] = int(lst[3])
    else:
        dct[lst[0]] += int(lst[3])
    if lst[1] not in dct.keys():
        dct[lst[1]] = int(lst[2])
    else:
        dct[lst[1]] += int(lst[2])
team = input('Введите название футбольной команды: ')
if team in dct.keys():
    goals = dct[team]
    print(f'Кол-во пропущенных мячей: {goals}')
    for i, v in dct.items():
        if v == goals:
            print('У команды', i)
else:
    print('В списке нет такой команды')
h = ['Футбольная команда', 'Пропущенные мячи']
print(tabulate.tabulate(sorted(dct.items()), headers=h))
