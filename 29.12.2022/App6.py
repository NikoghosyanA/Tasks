sm = 0
lst = [[], [], []]
while True:
    if sm > 10000:
        break
    a = int(input())
    sm += a
    if sum(list(map(int, list(str(a))))) > 10:
        lst[0].append(a)
    elif a not in lst[0] and bin(a).count('1') >= 4:
        lst[1].append(a)
    else:
        lst[2].append(a)
print(lst)
