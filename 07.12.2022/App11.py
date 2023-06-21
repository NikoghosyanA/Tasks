f = open('input.txt', 'r')
for i in f:
    lst = list(i)
    if lst[1] == '+':
        if lst[0] == 'x':
            print(int(lst[4]) - int(lst[2]))
        elif lst[2] == 'x':
            print(int(lst[4]) - int(lst[0]))
    elif lst[1] == '-':
        if lst[0] == 'x':
            print(int(lst[4]) + int(lst[2]))
        elif lst[2] == 'x':
            print(-int(lst[4]) + int(lst[0]))
