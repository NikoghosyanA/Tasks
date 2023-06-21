n = int(input())
lst = []
for i in range(n):
    lst.append(float(input()))
if n % 2 == 0:
    lst.pop(n // 2)
    lst.pop(n // 2 - 1)
else:
    lst.pop(n // 2)
print(*lst[::-1])
