h, w, n = map(int, input().split())
m = [['.' for _ in range(w)] for _ in range(h)]
alf = 'abcdefghijklmnopqrstuvwxyz'
lst = []
for _ in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    for k in alf:
        print(lst)
        if k not in lst:
            lst.append(k)
            for i in range(r1-1, r2):
                for j in range(c1-1, c2):
                    if i == r1 - 1:
                        m[i][j] = k
                    elif i == r2 - 1:
                        m[i][j] = k
                    elif j == c1 - 1:
                        m[i][j] = k
                    elif j == c2 - 1:
                        m[i][j] = k
            break
for i in m:
    print(*i)
