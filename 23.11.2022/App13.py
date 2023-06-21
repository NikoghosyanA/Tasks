lst = list(map(int, input().split()))
mn = sorted(lst)[-1]
for i in lst:
    if i % 2 == 1 and i < mn:
        mn = i
if mn <= sorted(lst)[-1] and mn % 2 == 1:
    print(mn)
else:
    print('NO')
