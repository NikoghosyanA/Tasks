n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(str, input().split(': '))))
s = input()
lst1 = []
for j in lst:
    lst2 = []
    for k in j:
        for i in s:
            if i in k and k not in lst2:
                lst2.append(k)
    lst1.append(lst2)
for i in lst1:
    try:
        print(max(i))
    except ValueError:
        print()
