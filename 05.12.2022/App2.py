from tabulate import tabulate

f = open('input.txt', 'r')
dct = {}
for line in f:
    lst = list(map(str, line.split()))
    lst1 = [int(i) for i in lst[2:]]
    if lst[1] not in dct.keys():
        dct[lst[1]] = {lst[0]: (sum(lst1) - max(lst1) - min(lst1)) / (len(lst1) - 2)}
    else:
        dct[lst[1]][lst[0]] = (sum(lst1) - max(lst1) - min(lst1)) / (len(lst1) - 2)
mx = 0
for i in dct.keys():
    mx = max(dct[i].values())
    for j, v in dct[i].items():
        if v == mx:
            print(i, j)
print(tabulate(sorted(dct.items())))
