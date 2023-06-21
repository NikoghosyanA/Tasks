s = input()
lst = list(map(str, s.split()))
ns = s
for i in range(len(s)):
    for j in range(len(s)):
        if i < j:
            if s[i:j] == lst[-1]:
                ns = ns[:i] + str(s[i:j])[::-1] + ns[j:]
print(ns)
