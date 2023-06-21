s = '  asd  sad   das ads  '  #s = input()
b = input().lower()
ns = ''
q = -1
for i in range(len(s)):
    if (s[i - 1] == ' ' or i == 0) and s[i].isalpha() and s[i] == b:
        for j in range(i, len(s)):
            if (s[j] == ' ' or j + 1 == len(s)) and i != 0:
                if j + 1 == len(s):
                    ns += s[i:j+1] * 2
                    q = j
                    break
                else:
                    ns += (s[i:j] * 2) + ' '
                    q = j
                    break
            elif s[j] == ' ' and i == 0:
                ns += (s[i:j] * 2) + ' '
                q = j
                break
    else:
        if i > q:
            ns += s[i]
print(ns)
