obj = []
while True:
    s = input()
    if s == '':
        break
    obj.append(s)

n = int(input())
be = []
for i in range(n):
    be.append(input())
dct = {}
for i in obj:
    s = ''
    for j in be:
        if len(set(i.lower()).intersection(set(j.lower()))) >= 3:
            if j > s:
                s = j
    dct[i.capitalize()] = s
print(dct)
