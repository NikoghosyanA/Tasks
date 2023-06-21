def func(arr):
    c = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < 0:
                c += 1
    return c
