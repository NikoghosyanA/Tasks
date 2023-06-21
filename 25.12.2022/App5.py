a, b = map(int, input().split())
for i in range(a, b+1):
    if (int(str(i)[0]) ** 3) + (int(str(i)[1]) ** 3) + (int(str(i)[2]) ** 3) == i:
        print(i)
