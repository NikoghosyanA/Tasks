n, s, x, y = map(int, input().split())
lst = [i for i in range(1, n+1)]
c = 0
lst1, lst2 = [], []
for i in range(0, n, s):
    for j in range(n+1):
        if j - i == s:
            if c % 2 == 0:
                for q in lst[i:j]:
                    lst1.append(q)
                c += 1
                break
            elif c % 2 == 1:
                for q in lst[i:j]:
                    lst2.append(q)
                c += 1
                break
        elif n - i < s:
            if c % 2 == 0:
                for q in lst[i:]:
                    lst1.append(q)
                c += 1
                break
            elif c % 2 == 1:
                for q in lst[i:]:
                    lst2.append(q)
                c += 1
                break
if x in lst1 and y in lst1:
    print('YES')
elif x in lst2 and y in lst2:
    print('YES')
else:
    print('NO')
