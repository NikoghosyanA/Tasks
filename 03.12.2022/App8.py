a = input()
c = 0
for i in a:
    if i == ',':
        c += 1
a1 = a.replace(',', '')
print(a, a1, c)
