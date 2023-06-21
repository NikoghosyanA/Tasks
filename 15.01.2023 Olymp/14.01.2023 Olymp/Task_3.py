from itertools import permutations

k, m, A, n, B = int(input()), int(input()), list(map(int, input().split())), int(input()), list(
    map(int, input().split()))
lst = []
if len(A) > len(B):
    for i in range(1, k + 1):
        for _ in range(len(A)):
            lst.append(i)
else:
    for i in range(1, k + 1):
        for _ in range(len(B)):
            lst.append(i)
prm = []
for k in range(2, len(A) + 1):
    c = permutations(lst, k)
    for p in c:
        if p not in prm:
            prm.append(p)
for cmb in prm:
    lsta, lstb = [-1], [-1]
    for i in cmb:
        for j1 in range(len(A)):
            if i == A[j1] and j1 > lsta[-1]:
                lsta.append(j1)
                break
        for j2 in range(len(B)):
            if i == B[j2] and j2 > lstb[-1]:
                lstb.append(j2)
                break
    if len(lsta) - 1 != len(cmb) and len(lstb) - 1 != len(cmb):
        print(len(cmb))
        print(*cmb)
        break
