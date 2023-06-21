for z in range(102):
    x, y = -80 + ((9*z)/10), 180-((19*z)/10)
    if (int(x) == x and int(y) == y) and (x >= 0 and y >= 0):
        print(int(x), int(y), z)
        break
    elif z > 100:
        print(-1, -1, -1)
