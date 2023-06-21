n = int(input())
for i in range(n + 1):
    if i ** 2 > n:
        print(i - 1)
        break
    elif i ** 2 == n:
        print(i)
        break
