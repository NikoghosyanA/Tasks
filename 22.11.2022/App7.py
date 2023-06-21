input()
lst = list(map(int, input().split()))
m = max(lst)
for i in lst:
    if str(i)[-1] == '7' and i < m:
        m = i
print(m)

