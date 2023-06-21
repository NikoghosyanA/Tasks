a, h, m = map(int, input().split())
print((a - (h * 60 + m) * 5.5) % 360)
