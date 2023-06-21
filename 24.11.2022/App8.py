s = input('string: ')
n = input('letter: ').lower()
lst = list(map(str, s.split()))
lst1 = []
ns = s
c = 0
for i in range(len(lst)):
    if lst[i][0] == n:
        lst1.append(lst[i])
for i in range(len(lst1)):
    for j in range(c, len(ns)):
        for k in range(len(ns)):
            if j < k:
                if ns[j:k] == lst1[i]:
                    ns = ns[:j] + (str(ns[j:k]) * 2) + ns[k:]
                    c += 1
        if c == 1:
            c = 0
            break
print(ns)
