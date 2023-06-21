n, k = map(int, input().split())
dnk = input()
lst = []
lsst = []
for i in range(n):
    for j in range(n + 1):
        if j - i == k:
            a = dnk[i:j]
            lsst.append(a)
            lst.append([a.count('A'), a.count('C'), a.count('T'), a.count('G')])
c = 0
while c < n:
    c += 1
    for i in range(len(lst)):
        t = False
        for j in range(len(lst)):
            if i != j:
                if lst[i] != lst[j]:
                    t = True
                else:
                    lst.remove(lst[i])
                    t = False
                    break
        if not t:
            break
print(len(lst))
