print('y z w x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not ((x or not y) and (not z == w)) or (y and z)) == 0:
                    print(y, z, w, x)
