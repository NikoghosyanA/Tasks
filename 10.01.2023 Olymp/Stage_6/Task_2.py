n = int(input())
lst = []
for i in range(n):
    for j in range(i+1, n):
        if j > i:
            lst.append(f'if (ar[{i}] < ar[{j}])\n\tswap(ar[{i}], ar[{j}]);')
for i in lst:
    print(i)
