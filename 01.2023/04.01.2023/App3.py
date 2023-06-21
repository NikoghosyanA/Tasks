x, y, c = map(int, input().split())
t = False
for a in range(x+1):
    for b in range(y+1):
        if a + b == c:
            print(a, b)
            t = True
            break
    if t:
        break
else:
    print('Impossible')
