import random

n = int(input())
lst = []
for i in range(n):
    lst.append(random.randint(-10, 10))
print(*lst)


def f1(c, arr):
    count = 0
    for v in arr:
        if v == 0:
            count += 1
    return count


def f2(c, arr):
    if arr == sorted(arr):
        return True
    else:
        return False


def f3(c, arr):
    mx, mn = -1, -1
    for v in range(c):
        if mx == -1 and arr[v] == max(arr):
            mx = v
        if mn == -1 and arr[v] == min(arr):
            mn = v
    arr[mn], arr[mx] = arr[mx], arr[mn]
    return arr


print(f1(len(lst), lst))
print(f2(len(lst), lst))
print(f3(len(lst), lst))
