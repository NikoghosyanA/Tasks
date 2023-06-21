n, k, a, b = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst, reverse=True)
lst1 = []
while len(lst1) < a:
    lst1.append(lst[0])
    lst.pop(0)
print(max(lst1) - min(lst1))

