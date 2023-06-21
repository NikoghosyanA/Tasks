import random
n = int(input())
lst = []
for i in range(n):
    c = 0
    a = random.randint(1, n**2)
    for j in range(1, a):
        if a % j == 0:
            c += 1
    if c <= 1:
        lst.append(a)
print(*lst)
print(lst.index(max(lst)))
