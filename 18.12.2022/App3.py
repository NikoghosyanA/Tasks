X, Y = int(input()), int(input())

if X == 1:
    print(1)
else:
    if Y == X:
        print(-1)
    else:
        if Y - X == 1:
            print(X * (X - 1))
        else:
            if (Y - X) > 1 and Y < 2 * X - 1:
                print(2 * X)
            else:
                if Y >= 2 * X - 1:
                    print(X)
                else:
                    print(-1)
