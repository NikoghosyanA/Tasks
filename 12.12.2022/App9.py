n = int(input())
a, b = map(int, input().split())
if a + b > n:
    print((a + b) - n, min(a, b))
else:
    print(0, min(a, b))
