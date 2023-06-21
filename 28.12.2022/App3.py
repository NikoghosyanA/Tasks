abc, k = input(), int(input())
q = len(abc)
for n in range(q ** (k - 1)):
    print(abc[n // (q ** (k - 2))] + abc[0], end='')
    for i in range(k - 3, -1, -1):
        print(abc[n // (q ** i) % q], end='')
    print()
print(q ** (k - 1))
