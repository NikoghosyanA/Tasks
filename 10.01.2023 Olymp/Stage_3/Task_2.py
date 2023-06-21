n, p, q = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, n+1):
        t = False
        if j >= i:
            for k in range(2, j):
                if i % k == 0 and j % k == 0:
                    t = True
                    break
        elif i > j:
            for k in range(2, i):
                if i % k == 0 and j % k == 0:
                    t = True
                    break
        if t:
            continue
        else:
            if 1/p < i/j < 1/q:
                print(f'{i}/{j}')
