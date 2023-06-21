n = int(input())
lst = list(map(int, input().split()))
s = ''
c = 1
i, j = 0, 1
count = 0
while True:
    try:
        if lst[i] == lst[i+j]:
            c += 1
            j += 1
        else:
            if i == 0:
                s += f'[{lst[i]} {c}]'
                count += 1
            else:
                s += f'[{lst[i]} {c}]'
                count += 1
            i = i + j
            c = 1
            j = 1
    except IndexError:
        s += f'[{lst[i]} {c}]'
        count += 1
        break
    if i >= n-1:
        break
print(count)
print(s)
