n, f = int(input()), int(input())
if n in [1, 2, 3] and f <= 100:
    print('Yes')
elif n in [4, 5, 6, 7] and f <= 50:
    print('Yes')
elif n >= 8 and f <= 2:
    print('Yes')
else:
    print('No')
