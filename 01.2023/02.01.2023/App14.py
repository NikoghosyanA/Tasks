a = [list(range(i, i + 8) if i % 16 else reversed(range(i, i + 8))) for i in range(0, 63, 8)]
b = zip(*[list(reversed(i)) for i in a])
[print(*i) for i in b]
print()
[print(*i) for i in a]
