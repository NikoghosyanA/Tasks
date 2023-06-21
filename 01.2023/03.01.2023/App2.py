mx = 8800
c = 0
for i in range(8800, 55536):
    prod = 1
    t = False
    for j in list(str(i)):
        if j == '7':
            t = True
        prod *= int(j)
    if t and prod > 35:
        c += 1
        if i > mx:
            mx = i
print(c, mx)
