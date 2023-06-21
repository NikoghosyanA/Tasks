def in_target(x, y, xc, yc, r=10):
    return ((xc - x) ** 2 + (yc - y) ** 2) ** 0.5 <= r


targets = [(0, 0),
           (25, 0),
           (50, 0),
           (75, 0),
           (100, 0)
           ]

for _ in range(5):
    x, y = map(int, input().split())
    i = 0
    while i < len(targets):
        if in_target(x, y, *targets[i]):
            del targets[i]
        else:
            i += 1

print(5 - len(targets))
