n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.remove(max(lst))
print(max(lst))
