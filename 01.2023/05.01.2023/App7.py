n = int(input())
sm = 0
for i in range(n):
    a = int(input())
    if a <= 10:
        continue
    elif 10 < a <= 18:
        sm += 50
    else:
        sm += 100
print(sm)
