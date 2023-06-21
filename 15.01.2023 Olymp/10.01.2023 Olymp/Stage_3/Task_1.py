n = int(input())
lst = [['0' for i in range(n)] for j in range(n)]
alf = 'abcdefghijklmnopqrstuvwxyz'
q = 0
k = 0
t = 0
while k < n:
    if t == 0:
        if q == 0:
            for i in range(n):
                for j in range(n):
                    if i == j:
                        if lst[i][j] == '0':
                            lst[i][j] = alf[q]
                        if lst[i][-(j + 1)] == '0':
                            lst[i][-(j + 1)] = alf[q]
        else:
            for i in range(n):
                for j in range(n):
                    if lst[i][j] == alf[q-1]:
                        if i + 1 in range(n):
                            if lst[i+1][j] == '0':
                                lst[i+1][j] = alf[q]
                        if j + 1 in range(n):
                            if lst[i][j+1] == '0':
                                lst[i][j+1] = alf[q]
                        if i - 1 in range(n):
                            if lst[i-1][j] == '0':
                                lst[i-1][j] = alf[q]
                        if j - 1 in range(n):
                            if lst[i][j-1] == '0':
                                lst[i][j-1] = alf[q]
    else:
        for i in range(n):
            for j in range(n):
                if lst[i][j] == alf[q - 1]:
                    if i + 1 in range(n):
                        if lst[i + 1][j] == '0':
                            lst[i + 1][j] = alf[q]
                    if j + 1 in range(n):
                        if lst[i][j + 1] == '0':
                            lst[i][j + 1] = alf[q]
                    if i - 1 in range(n):
                        if lst[i - 1][j] == '0':
                            lst[i - 1][j] = alf[q]
                    if j - 1 in range(n):
                        if lst[i][j - 1] == '0':
                            lst[i][j - 1] = alf[q]
    q += 1
    k += 1
    if q == 26:
        q = 0
        t += 1
for i in lst:
    print(''.join(i))
