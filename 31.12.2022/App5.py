flag = 1
while True:
    line = input()
    if not line:
        break
    elif flag:
        flag = 0
        print('-'.join(filter(lambda x: not int(x) % 2, line.split())))
    else:
        flag = 1
        print('-'.join(filter(lambda x: int(x) % 2, line.split())))
