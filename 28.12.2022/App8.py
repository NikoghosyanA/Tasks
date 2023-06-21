def count_numbers(k, n, flag):
    if n == 1:
        if flag:
            return k - 1
        else:
            return 1
    if flag:
        return (k - 1) * (count_numbers(k, n - 1, 0) +
                          count_numbers(k, n - 1, 1))
    else:
        return count_numbers(k, n - 1, 1)


n, k = map(int, input().split())
print(count_numbers(k, n, True))
