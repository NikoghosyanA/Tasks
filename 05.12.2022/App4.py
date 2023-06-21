a, b = input(), input()
try:
    a, b = int(a), int(b)
except ValueError:
    a, b = float(a), float(b)
x = b / (a * a - 1)
print(x)
