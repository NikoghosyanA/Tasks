for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            if x + y + z == 100 and x * 10000 + y * 5000 + z * 500 == 100000:
                print(x, y, z)
