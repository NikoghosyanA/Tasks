for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not w or y) and (not not x or y)) ^ ((z is w) or (y and not x)):
                    pass
                else:
                    print(x, y, z, w, 222)
