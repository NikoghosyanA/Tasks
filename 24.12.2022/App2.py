def iscomplex(n):
    c = 0
    for i in range(2, n):
        if n % i == 0:
            c += 1
    if c >= 1:
        return True


def list_complex(n):
    return [i for i in range(2, n + 1) if iscomplex(i)]


n = int(input())
lst = list_complex(n)
for num in lst:
    x = n - num
    print(x, lst)
    if x in lst:
        print(f'{num} + {x}')
