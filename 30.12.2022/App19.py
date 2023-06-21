a, b = map(int, input().split())
sm = 0
for x in range(a, b + 1):
    sm += x + 4
print(sm)
