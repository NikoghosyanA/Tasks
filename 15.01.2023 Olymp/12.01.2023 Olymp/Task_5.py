from itertools import permutations
from copy import deepcopy

n, m = map(int, input().split())
lst = []
for i in range(n):
    a = list(map(int, input().split()))
    lst.append(a)
ans = []
allrows, allcolumns = [], []
for i in range(n):
    rows = []
    columns = []
    for j in range(m):
        rows.append((i, j))
    ans.append(rows)
    allrows.append(rows)
for i in range(m):
    rows = []
    columns = []
    for j in range(n):
        columns.append((j, i))
    ans.append(columns)
    allcolumns.append(columns)


def is_true(ii, arr):
    tlist = []
    for jj in range(len(ii)):
        for q in range(len(ii[jj])):
            x, y = ii[jj][q][0], ii[jj][q][1]
            arr[x][y] = -arr[x][y]
    for w in range(n):
        smr = 0
        for e in range(m):
            smr += arr[w][e]
        if smr >= 0:
            tlist.append(1)
        else:
            tlist.append(0)
    for w in range(m):
        smc = 0
        for e in range(n):
            smc += arr[e][w]
        if smc >= 0:
            tlist.append(1)
        else:
            tlist.append(0)
    if 0 in tlist:
        return False
    else:
        return True


ansc = ()
tt = False
for k in range(len(ans)):
    perm = permutations(ans, k)
    for i in list(perm):
        clst = deepcopy(lst)
        tt = is_true(i, clst)
        if tt:
            ansc = i
            break
    if tt:
        break
if ansc:
    print(len(ansc))
    for i in range(len(ansc)):
        if ansc[i] in allrows:
            print(f'R {ansc[i][0][0] + 1}')
        elif ansc[i] in allcolumns:
            print(f'C {ansc[i][0][1] + 1}')
else:
    print(-1)
