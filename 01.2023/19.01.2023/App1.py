s = input()
ns = ''
i = 0
j = 0
while j < len(s):
    c = 0
    while j < len(s):
        if s[i] == s[j]:
            c += 1
            j += 1
        else:
            i = j
            break
    if j == len(s):
        ns += s[i] + str(c)
    else:
        ns += s[i-1] + str(c)
print(ns)
