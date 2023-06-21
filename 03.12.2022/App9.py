s = input()
s1 = list(map(str, s.split()))
a = '`!@#$%^&*()_+-=/\\[]{};:\'"?/<,>.|~'
for i in s1:
    for j in a:
        if j in i:
            i = i.replace(j, '')
            if len(i) % 2 == 0:
                print(i)
print(s)

