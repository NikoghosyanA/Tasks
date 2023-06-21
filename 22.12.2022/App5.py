def per(s):
    k = []
    for i in range(1, len(s) + 1):
        if (i == len(s) and s[i - 1] == s[0]):
            k.append(i)
        for j in range(i, len(s)):
            if (s[j] != s[j - i]):
                break
            elif (s[j] == s[j - i] and j == len(s) - 1):
                k.append(i)
    return k


a = []
b = int(input())
k = input()
w = len(k)
for i in range(len(k)):
    a = per(k[:w - i])
    if a != []:
        f = min(a)
        if f <= b:
            print(i)
            break
    else:
        f = 1
        if f <= b and len(k[:w - i]) <= b:
            print(i)
            break
