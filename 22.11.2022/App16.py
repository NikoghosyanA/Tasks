x = float(input('x: '))
lst = list(map(int, input().split()))
for i in range(len(lst)):
    if lst[i] == x:
        print(i)
    elif i == len(lst) - 1:
        print('null')
