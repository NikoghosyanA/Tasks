n = int(input())
ans = n
while True:
    c = 0
    for i in range(1, ans+1):
        if ans % i == 0:
            c += 1
    if c == n:
        print(ans)
        break
    ans += 1
