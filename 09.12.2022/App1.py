lst = list(map(int, input().split()))
mn = 1000
sr2 = 0
c2 = 0
for i in lst:
    if len(str(i)) == 3:
        if i < mn:
            mn = i
    if len(str(i)) == 2:
        c2 += 1
        sr2 += i
sr2 = sr2 / c2
c = 0
for i in lst:
    if i < sr2:
        c += 1
count = 0
for i in range(len(lst)-1):
    if lst[i] + 1 == lst[i+1] or lst[i] - 1 == lst[i+1]:
        count += 1
print(f'a) {mn}\nb) {c}\nc) {count}')
