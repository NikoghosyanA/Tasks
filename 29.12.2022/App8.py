n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    mx = 0
    for x in range(n):
        if x**2 <= n and x > mx:
            mx = x
    print(mx)

