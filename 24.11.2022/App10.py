n, k = map(int, input().split())
s = input()
lst = []
for i in range(len(s)+1):
    for j in range(len(s)+1):
        if j - i == k:
            lst.append(s[i:j])
if len(lst) == len(set(lst)):
    print('NO')
else:
    print('YES')
