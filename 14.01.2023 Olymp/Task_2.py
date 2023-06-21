from copy import deepcopy

n, m = map(int, input().split())


def arg_min(T, S):
    amin = -1
    mx = 1000000
    for i, t in enumerate(T):
        if t < mx and i not in S:
            mx = t
            amin = i
    return amin


D = [[1000000 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, l = map(int, input().split())
    D[a-1][b-1] = l
T = [1000000]*n
v = 0
S = {v}
T[v] = 0
M = [0]*n

while v != -1:
    for j, dw in enumerate(D[v]):
        if j not in S:
            w = T[v] + dw
            if w < T[j]:
                T[j] = w
                M[j] = v
    v = arg_min(T, S)
    if v >= 0:
        S.add(v)
start = 0
end = n-1
P = [end]
while end != start:
    end = M[P[-1]]
    P.append(end)
P = sorted(P)
mx = 0
nD = deepcopy(D)
x, y = 0, 0
for i in range(len(P)):
    for j in range(i+1, len(P)):
        if j-i == 1 and j > i:
            if D[P[i]][P[j]] > mx:
                mx = D[P[i]][P[j]]
                x, y = P[i], P[j]
nD[x][y] *= 2

T1 = [1000000]*n
v1 = 0
S1 = {v1}
T1[v1] = 0
M1 = [0]*n

while v1 != -1:
    for j, dw in enumerate(nD[v1]):
        if j not in S1:
            w = T1[v1] + dw
            if w < T1[j]:
                T1[j] = w
                M1[j] = v
    v1 = arg_min(T1, S1)
    if v1 >= 0:
        S1.add(v1)
print(T1[n-1] - T[n-1])
