n, k = int(input()), int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lstc = []
for i in lst:
    lstc.append(lst.count(i))
print(k - max(lstc))
