n = int(input())
for i in range(1, n + 1):
    if i == int(str(i ** 2)[-len(str(i)):]):
        print(i, i**2)
