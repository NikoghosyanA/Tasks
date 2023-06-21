a, b = list(map(str, input().split('.'))), list(map(str, input().split('.')))
if a[1] > b[1]:
    print('.'.join(a[:2]))
elif b[1] > a[1]:
    print('.'.join(b[:2]))
elif a[1] == b[1]:
    if a[0] > b[0]:
        print('.'.join(a[:2]))
    elif b[0] > a[0]:
        print('.'.join(b[:2]))
