# 1
n, c, d = map(int, input().split())
sm1 = 0
for i in range(1, n+1):
    if n % i == 0:
        if i % c == 0 and i % d == 0:
            sm1 += i
print(sm1)

# 2
n, c = map(int, input().split())
for i in range(1, n+1):
    if n % i == 0:
        if i % c == 0:
            print(i, end=' ')
