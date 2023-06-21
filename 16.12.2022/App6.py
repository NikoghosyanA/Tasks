a = int(input())
if a in [i for i in range(5, 21)] or a % 10 in [i for i in range(5, 10)] or a % 10 == 0:
    print(a, 'лет')
elif a % 10 == 1:
    print(a, 'год')
elif a % 10 in [2, 3, 4]:
    print(a, 'года')
