s = input()[::-1]
ss = input()[::-1]
ans = 0
lst = []
for i in range(len(s)):
    if s[i] == ss[0]:
        for j in range(2, len(s)-i+1):
            if s[i:i+j] == ss[0:0+j] and i + j == len(s):
                lst.append(len(s[i:i+j]))
                break
if lst:
    ans = len(s) - max(lst)
else:
    ans = len(s)
print(ans)

