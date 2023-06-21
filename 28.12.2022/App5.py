def is_simple(n):
    c = 0
    for i in range(2, n):
        if n % i == 0:
            c += 1
    if c >= 1:
        return True
    else:
        return False


n = int(input())
count = 0
if not is_simple(n):
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
print(count)
