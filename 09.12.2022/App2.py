f = open('17.txt', 'r')
lst = []
for line in f:
    lst = list(map(int, line.split()))
c = 0
mxprod = 0
for i in range(len(lst)):
    if i >= 1:
        if lst[i] < lst[i-1]:
            c += 1
            pr = lst[i] * lst[i-1]
            if pr > mxprod:
                mxprod = pr
print(c, mxprod)
