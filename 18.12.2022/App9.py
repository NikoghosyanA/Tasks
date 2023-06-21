lst = list(map(str, input().split(' / ')))
s = input()
lst1 = []
for a in lst:
    c = 0
    nlst = []
    for i in a:
        for j in s:
            if i == j and j not in nlst:
                nlst.append(j)
                c += 1
    if c >= 5:
        lst1.append(a)
print(' (*) '.join(lst1))
