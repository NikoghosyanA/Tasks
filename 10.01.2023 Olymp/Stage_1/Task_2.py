def f(n, p, lst, nn):
    if n:
        for i in range(n + 1, 0, -1):
            if i <= p:
                if len(lst) == 0:
                    f(n - i, i, lst + [i], nn)
                else:
                    if abs(i - lst[-1]) > 1:
                        f(n - i, i, lst + [i], nn)
    else:
        lst = list(map(str, lst))
        print(f'{nn}=' + '+'.join(sorted(lst)))


n = int(input())
f(n, n, [], n)
