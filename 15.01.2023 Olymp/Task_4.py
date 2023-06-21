n = int(input())
k = 0
lst = []
while n > 0:
    k += 1
    if n % 2 == 1:
        print((-n % 4))
        lst.append(-(n % 4))
    elif n % 2 == 0:
        lst.append(0)
    n = (n - lst[-1]) // 2
print(lst)
