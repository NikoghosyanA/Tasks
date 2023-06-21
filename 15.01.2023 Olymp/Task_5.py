n = int(input())
n = n // 2 + 1
lst = list(map(int, input().split()))
s = set(lst)
for i in s:
    if lst.count(i) >= n:
        print(i)
