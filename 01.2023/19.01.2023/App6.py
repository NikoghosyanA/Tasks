lst = list(map(int, input().split()))
lst1 = lst.copy()
for i in range(len(lst)):
    lst1.pop(i)
    if lst1 == sorted(lst1):
        print('true')
        break
    else:
        lst1 = lst.copy()
