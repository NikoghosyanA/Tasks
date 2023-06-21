a = int(input())
if a % 3 == 0:
    print(a * ((a // 3) * 4))
elif a % 5 == 0:
    print(a * ((a // 5) * 12))
