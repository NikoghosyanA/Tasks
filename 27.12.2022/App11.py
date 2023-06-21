import math
a = int(input())
ar = []
d = 0
for i in range(a):
    ar.append(input().split())
for i in range(len(ar)):
    for j in range(len(ar)):
        b = round(math.sqrt(((int(ar[j][0]) - int(ar[i][0]))**2) + ((int(ar[j][1]) - int(ar[i][1]))**2)), 15)
        if b > d:
            d = b
print(d)
