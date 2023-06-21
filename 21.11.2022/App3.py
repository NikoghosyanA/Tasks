lst = []
n = int(input('Кол-во видеокарт: '))
for i in range(n):
    lst.append(int(input(f'{i + 1} Видеокарта: ')))
m = max(lst)
lst1 = [i for i in lst if i != m]
print('Старый список видеокарт:', lst)
print('Новый список видеокарт:', lst1)
