n1 = int(input())
n2 = int(input())
if (n1 + n2 * 2) % 2 == 1:
    print("No")
else:
    print("Yes")
    if ((n1 + n2 * 2) // 2) % 2 == 0:
        if n2 * 2 < n1:
            print((n1 + n2 * 2) // 2 - n2 * 2, n2)
        elif n2 * 2 > n1:
            print(n1, ((n1 + n2 * 2) // 2 - n1) // 2)
        else:
            print(n1, 0)
    else:
        if n2 * 2 < n1:
            print((n1 + n2 * 2) // 2 - n2 * 2, n2)
        elif n2 * 2 > n1:
            print(n1 - 1, ((n1 + n2 * 2) // 2 - n1 + 1) // 2)
        else:
            print(n1, 0)
