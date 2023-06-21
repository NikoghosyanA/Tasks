s1, s2 = input(), input()
c = 0
if len(s1) >= len(s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            print('Индекс', i, 'Позиция', i+1)
            c += 1
else:
    for i in range(len(s2)):
        if s1[i] == s2[i]:
            print('Индекс', i, 'Позиция', i+1)
            c += 1
if c == 0:
    print('Совпадений нет')
