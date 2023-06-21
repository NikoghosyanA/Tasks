import random
vs = int(input())
vmin, vmax = map(int, input().split())
while True:
    v = random.randint(vmin, vmax)
    if v != vs:
        print(v)
        break
    else:
        continue
