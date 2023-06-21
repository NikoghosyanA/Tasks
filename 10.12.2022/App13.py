from numpy import std
arr = []
f = open('input.csv', 'r')
for line in f:
    arr.append(list(map(int, line.split(','))))
c1, c2 = 0, 0
for i in arr:
    if 0 <= std(i) <= 1:
        c1 += 1
    else:
        c2 += 1
if c1 > c2:
    print(1)
else:
    print(2)
