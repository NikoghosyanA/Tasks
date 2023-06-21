s = input()
ans = []
for k in range(1, len(s)):
    lst = []
    for i in range(len(s)):
        for j in range(len(s)+1):
            if j - i == k:
                if s[i:j] not in lst:
                    lst.append(s[i:j])
    for q in lst:
        c = 0
        for i1 in range(len(s)):
            for j1 in range(len(s)+1):
                if q == s[i1:j1]:
                    c += 1
        if c >= 2:
            ans.append(q)
if ans:
    print(len(ans[-1]))
else:
    print(0)
