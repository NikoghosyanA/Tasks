lst = [[], [], []]
g = ['а', 'о', 'и', 'ы', 'у', 'э']
while True:
    s = input()
    if s == 'Стоп':
        break
    if len(s) <= 10:
        c = 0
        for i in s:
            if i in g:
                c += 1
        if c >= 5:
            lst[0].append(s)
        else:
            lst[2].append(s)
    elif len(s) > 10:
        if '  ' in s:
            lst[1].append(s)
        else:
            lst[2].append(s)
print(lst)
