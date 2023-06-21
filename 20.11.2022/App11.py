def summa(lst):
    if len(lst) != 4:
        print('error')
        return
    res = all(type(x) == int for x in lst)
    if res is False:
        print('error')
        return
    print([lst[0] + lst[2], lst[1] + lst[3]])


def raznost(lst):
    if len(lst) != 4:
        print('error')
        return
    res = all(type(x) == int for x in lst)
    if res is False:
        print('error')
        return
    print([lst[0] - lst[2], lst[1] - lst[3]])


def multi(lst):
    if len(lst) != 4:
        print('error')
        return
    res = all(type(x) == int for x in lst)
    if res is False:
        print('error')
        return
    print([lst[0] * lst[2] - lst[1] * lst[3], lst[0] * lst[3] + lst[1] * lst[2]])


def divide(lst):
    if len(lst) != 4:
        print('error')
        return
    res1 = all(type(x) == int for x in lst)
    res2 = all(type(x) == float for x in lst)
    if res1 is False and res2 is False:
        print('error')
        return
    print([(lst[0] * lst[2] + lst[1] * lst[3]) / (lst[2] * lst[2] + lst[3] * lst[3]),
           (lst[1] * lst[2] - lst[0] * lst[3]) / (lst[2] * lst[2] + lst[3] * lst[3])])


summa([2, 1, 3, 5])
raznost([2, 1, 3, 5])
multi([2, 1, 3, 5])
divide([2, 1, 3, 5])
