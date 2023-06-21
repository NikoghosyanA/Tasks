c = 0
mins = ''
ss = ''
while True:
    if c > 100:
        break
    s = input()
    c += len(s)
    ss += s
    if mins == '':
        mins = s
    else:
        if len(s) < len(mins):
            mins = s
print(ss.count('е'), ss.count('з'), mins)
