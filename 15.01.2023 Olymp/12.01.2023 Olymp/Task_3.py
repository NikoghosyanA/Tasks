n = int(input())
sm = 0
for i in range(n+1):
    for j in range(n+1):
        if j >= i:
            sm += i + j
print(sm)
