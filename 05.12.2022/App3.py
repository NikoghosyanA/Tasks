a, b = input(), input()
try:
    a1, b1 = int(a), int(b)
    for i in range(a1, b1 + 1):
        print(i)
except ValueError:
    a1, b1 = int(round(float(a))), int(round(float(b)))
if a1 < b1:
    for i in range(a1, b1 + 1):
        print(i)
else:
    for i in range(b1, a1 + 1):
        print(i)
