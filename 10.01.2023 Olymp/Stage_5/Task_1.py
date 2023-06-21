a, b = int(input()), int(input())
ans = 0
if b >= 0:
    ans += b * a
else:
    ans -= abs(b) * a
print(ans)
