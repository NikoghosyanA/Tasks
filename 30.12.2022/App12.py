a = 'abcdefghijklmnopqrstuvwxyz'
lst = []
with open('input.txt', 'r') as f:
    for line in f:
        for i in line.split():
            lst.append(i)
with open('output.txt', 'a') as f:
    dct = {}
    for i in a:
        c = 0
        for j in lst:
            if j[0] == i:
                c += 1
        if c != 0:
            dct[i] = c
    lst1 = []
    for i in sorted(dct.values(), reverse=True):
        for k, v in dct.items():
            if v == i and k not in lst1:
                f.write(f'{v} {k}\n')
                lst1.append(k)
                break
