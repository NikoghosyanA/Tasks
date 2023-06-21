import random

n = int(input())
lst = []
for i in range(n):
    lst.append(random.randint(1500, 2500))
summa = 0
for i in lst:
    sm = 0
    for j in str(i):
        sm += int(j)
    if sm % 2 == 1:
        summa += i
print(summa)
mx = 0
for i in lst:
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
    if c == 1:
        if i > mx:
            mx = i
print(mx)
