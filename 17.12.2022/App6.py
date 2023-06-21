lst = list(map(int, input().split()))
if lst[-1] == 100 or lst[-2] == 100:
    print(0)
else:
    if sum(lst) < 250:
        print(250 - sum(lst))
    else:
        print(0)
