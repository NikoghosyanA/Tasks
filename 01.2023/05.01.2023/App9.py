def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 7
    if n >= 3:
        return 3 * fib(n-1) + fib(n-2) - fib(n-3)


n = int(input())
print(fib(n))
