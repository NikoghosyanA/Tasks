s = input()
for i in s:
    if i.isdigit():
        s = s.replace(i, '')
print(s)
