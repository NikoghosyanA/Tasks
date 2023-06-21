d = 0
while True:
    v, p = map(int, input().split())
    if v == 0 and p == 0:
        break
    if v > p:
        d += 1
print(d)