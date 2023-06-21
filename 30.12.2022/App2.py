lst = list(map(int, input().split()))
a, b = lst[0], lst[-1]
lst = lst[:-1]
chet, nechet = False, False
if b % 2 == 0:
    chet = True
else:
    nechet = True
if chet:
    for i in set(lst):
        if i < a and i % 2 == 0:
            print(i, end=' ')
elif nechet:
    for i in set(lst):
        if i < a and i % 2 != 0:
            print(i, end=' ')
