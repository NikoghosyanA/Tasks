n, k = int(input()), int(input())
if k / n > k // n:
    print(k // n + 1)
else:
    print(k // n)
