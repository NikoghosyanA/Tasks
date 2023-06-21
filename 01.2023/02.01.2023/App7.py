x = int(input())
for i in range(x, x+12):
    if i % 12 == 0:
        print(i - x)
        break
