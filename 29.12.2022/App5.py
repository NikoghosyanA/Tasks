maxs = ''
ss = ''
lst = []
while True:
    s = input()
    if s == 'Стоп':
        break
    ss += s
    if len(s) > len(maxs):
        maxs = s
    if 'ь' in s:
        lst.append(s)
print(maxs, ss.count('ь'))
print(lst)
