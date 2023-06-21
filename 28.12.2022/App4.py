n = input()
while True:
    if len(n) == 1:
        print(n)
        break
    lst = list(map(int, list(n)))
    n = str(sum(lst))

