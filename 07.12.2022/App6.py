n = int(input())
lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)
if len(lst) <= 2:
    print(*lst)
    print('ПРОСТОЕ')
else:
    print(*lst)
    print('НЕТ')
