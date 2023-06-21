lst = []
with open('input.txt', 'r') as f:
    for line in f:
        lst = list(map(int, line.split()))
with open('output.txt', 'w') as f:
    c = 0
    lst1 = []
    for i in lst:
        c1 = 0
        for j in range(2, i):
            if i % j == 0:
                c1 += 1
        if c1 == 0 and i != 1:
            c += 1
        if c1 != 0 or i == 1:
            lst1.append(c)
            c = 0
        if i == lst[-1] and c != 0:
            lst1.append(c)
    f.write(str(max(lst1)))
