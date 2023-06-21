a, b = map(int, input().split())
if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1):
    print(int(((b - a) / 2) - 1))
elif (a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0):
    print(int(((b - a) / 2)))
