n = int(input())
c = 0
for i in range(n):
    a, b = map(str, input().split())
    if a[4:] == '01' and (b == 'белый' or b == 'white'):
        c += 1
print(c)
