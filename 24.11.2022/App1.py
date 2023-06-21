lst = list(map(str, input().split()))
n = int(input())
for i in lst:
    if len(i) < n:
        print(i)
