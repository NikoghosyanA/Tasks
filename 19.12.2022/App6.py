n = int(input())
m = [list(map(int, input().split())) for i in range(n)]
col = [[m[k][i] for k in range(len(m))] for i in range(len(m[0]))]
d1 = [m[i][i] for i in range(len(m))]
m2 = [m[i][::-1] for i in range(len(m))]
d2 = [m2[i][i] for i in range(len(m2))]
res = []
for i in m: res += [sum(i)]
for i in col: res += [sum(i)]
res += [sum(d1)]
res += [sum(d2)]
print('YES'if len(set(res)) == 1 else 'NO')
