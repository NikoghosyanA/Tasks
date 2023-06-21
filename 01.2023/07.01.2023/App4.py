mn = 30000
n = int(input())
for i in range(n):
    a = int(input())
    if str(a)[-1] == '7':
        if a < mn:
            mn = a
print(mn)
