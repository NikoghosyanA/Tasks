n, b, f = map(int, input().split())
q = list(map(int, input().split()))
x = 0
while q != []:
    q.sort()
    x = q.pop(0)
    for i in range(len(q)):
        if q[i] < x + b:
            q[i] += f
print(x + b)
