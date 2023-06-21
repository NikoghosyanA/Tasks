k, a, n = int(input()), int(input()), int(input())
if n in range(a, (9*k) + 1):
    print(f'Kvartira nomer {n} nahodistya v dome')
    c = 1
    e = 1
    sm = 0
    for i in range(a, (9 * k) + 1):
        sm += i
        c += 1
        if c == k:
            e += 1
        if i == n:
            print('Etaj', e)
            break
    if sm % 2 == 0:
        print('Summa chetnaya')
    else:
        print('Summa nechetnaya')
else:
    print(f'Kvartira nomer {n} NE nahodistya v dome')
