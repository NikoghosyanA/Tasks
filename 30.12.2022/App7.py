a = set(map(str, input().split()))
b = set(map(str, input().split()))
c = set(map(str, input().split()))
ans1 = a.intersection(b, c)
ans2 = a.union(b, c)
print(ans1)
print(ans2)