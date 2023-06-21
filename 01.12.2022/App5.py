s = input()
i, j = 0, 1
while True:
    if s[i] == s[j]:
        s = s[:j] + s[j+1:]
    else:
        j += 1
    if j == len(s):
        i += 1
        j = i + 1
    if i == len(s)-1:
        break
print(s)
