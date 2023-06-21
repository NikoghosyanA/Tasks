n, m = map(int, input().split())
lst = []
for i in range(m):
    a, b = map(int, input().split())
    lst.append(sorted((a, b)))
lst = sorted(lst)
t = False
for i in lst:
    for j in lst:
        if i != j:
            for i1 in range(2):
                for j1 in range(2):
                    if i[i1] != j[j1]:
                        c = [i[i1], j[j1]]
                        if c != i and c != i[::-1] and c != j and c != j[::-1]:
                            if c in lst or c[::-1] in lst:
                                t = True
                                break
                if t:
                    break
        if t:
            break
    if t:
        print(-1)
        break
r = []
ans = []
lst1 = [i + 1 for i in range(n)]
if not t:
    for i in range(1, n+1):
        for j in lst:
            if i == j[0] and (i not in r or j[1] not in r):
                if i not in r:
                    r.append(i)
                if j[1] not in r:
                    r.append(j[1])
                if i not in ans:
                    ans.append(i)
                if i in lst1:
                    lst1.remove(i)
                if j[1] in lst1:
                    lst1.remove(j[1])
            elif i in lst1 and i not in r:
                r.append(i)
                ans.append(i)
    print(len(ans))
    print(*ans, sep=' ')
