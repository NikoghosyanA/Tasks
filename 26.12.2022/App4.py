c = 0
for i in range(101, 1000):
    if i % 13 == 0 and i % 15 == 0:
        c += 1
print(c)
