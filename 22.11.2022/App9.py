n, m = map(int, input().split())
s = input()
lst = []
for i in range(len(s)):
    for j in range(len(s) + 1):
        if i < j:
            if s[i:j][0] == '0' and s[i:j][-1] == '0' and len(s[i:j]) >= 3:
                lst.append(len(s[i:j]))
lst.remove(max(lst))
for i in range(m):
    k = int(input())
    if max(lst) - 1 == k:
        print('YES')
    else:
        print('NO')
