n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split(';'))))
k = int(input())
for i in range(n):
    mx = 0
    for j in lst[i]:
        if j % k == 0:
            if len(set(str(j)).intersection(set(str(k)))) == 0:
                if j > mx:
                    mx = j
    if mx == 0:
        print('')
    else:
        print(mx)
