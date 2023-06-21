input()
s = input()
A = list(map(int, s.split()))
print(min([A.count(a) for a in (1, 2)]))
