n = input()
s = input()
lst = list(map(str, s.split()))
lst1 = list(set(lst))
c = 0
for i in lst1:
    if s.count(i) >= 10:
        c += 1
print(c)
