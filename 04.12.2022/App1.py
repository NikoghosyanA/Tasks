def intersection(a, b):
    return [x for x in a if x in b]


print(intersection(list(map(int, input().split())), list(map(int, input().split()))))
