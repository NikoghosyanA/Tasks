n = int(input())
lst = []
for i in range(n):
    lst.append(input())
ans = []
for s in lst:
    ns = s
    for j in range(len(s)):
        if s[j] == 's' and j != 0:
            if j + 1 == len(s):
                ns = s[:j] + 'th'
            elif s[j + 1] != 'h':
                ns = s[:j] + 'th' + s[j+1:]
        if j == 0 and s[j].lower() == 'e':
            if s[j] == 'E':
                ns = 'Ae' + s[j+1:]
            else:
                ns = 'ae' + s[j+1:]
        if 'oo' in s:
            ns = s.replace('oo', 'ou')
        if 'Oo' in s:
            ns = s.replace('Oo', 'Ou')
    ans.append(ns)
print(*ans, sep='\n')
