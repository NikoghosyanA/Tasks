n = int(input())
lst = []
for i in range(n):
    lst.append(input())
dt, add = input('Delete symbol: '), input('Add symbol')
for i in range(len(lst)):
    if dt in lst[i]:
        for j in range(len(lst[i])):
            if lst[i][j] == dt:
                ni = lst[i][:j] + add + lst[i][j + 1:]
                lst[i] = ni
                print(lst[i])
