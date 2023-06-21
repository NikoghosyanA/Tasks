import operator

n, m = int(input()), int(input())
lst = []
for i in range(n):
    lst.append(list(map(float, input().split())))
for i in range(n):
    a = lst[i]
    s = sum(a) / len(a)
    b = [abs(x - s) for x in a]
    min_index, min_value = min(enumerate(b), key=operator.itemgetter(1))
    max_index, max_value = max(enumerate(b), key=operator.itemgetter(1))
    print(s, min_index, a[min_index], max_index, a[max_index])
