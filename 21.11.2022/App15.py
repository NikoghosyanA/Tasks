a, b = map(int, input().split())
if (a < 0 and b <= 0) or (a == 0 and b <= 0):
    print('no such x')
elif (a == 0 and b > 0) or (a > 0 and b > 0):
    print('any x')
elif a > 0 >= b:
    print(f'x < {-b/a} or x > {b/a}')
elif a < 0 < b:
    print(f'{-b/a} < x < {b/a}')
