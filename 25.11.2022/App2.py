n = int(input())
lst1, lst2 = [], []
for i in range(n):
    x, y = map(int, input().split())
    lst1.append(x)
    lst2.append(y)
c = 0
for i in range(len(lst1)):
    for j in range(len(lst1)):
        for k in range(len(lst1)):
            if k > j > i:
                x1, y1, x2, y2, x3, y3 = lst1[i], lst2[i], lst1[j], lst2[j], lst1[k], lst2[k]
                if not ((x3 - x1) * (y2 - y1) == (y3 - y1) * (x2 - x1)):
                    print('Yes')
                    print(i+1, j+1, k+1)
                    c = 1
            if c == 1:
                break
        if c == 1:
            break
    if c == 1:
        break
