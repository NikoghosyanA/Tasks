a, b, c, d = map(int, input().split())
count = 0
for x in range(1, 101):
    if a * x ** 3 + b * x ** 2 + c * x + d > 0:
        count += 1
print(count)
