s = input()
lst = []
for i in range(len(s)):
    for j in range(len(s)+1):
        if j > i:
            if s[i:j] not in lst:
                lst.append(s[i:j])
print(len(lst))
