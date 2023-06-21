def func(lst):
    sm = 0
    for i in lst:
        if i > lst[-1]:
            sm += i
    return sm
