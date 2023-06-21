lst = [1]
s = 1324
while lst[-1] < s:
    lst.append(lst[-1] * 2)
lst1 = []
for i in lst[::-1]:
    if i <= s:
        s -= i
        lst1.append(str(i))
print(' + '.join(lst1), '= 1324')
