lst = list(map(int, input().split()))
lst1 = sorted(lst)
for i in range(len(lst)):
    if lst[i] == lst1[i]:
        continue
    else:
        lst.pop(i)
        break
if lst == sorted(lst):
    print('true')
else:
    print('false')
