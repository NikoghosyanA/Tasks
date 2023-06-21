s1, s2 = input(), input()
t = False
for i in range(len(s2)):
    for j in range(len(s2)):
        c = 0
        if j - i == len(s1):
            for k in range(len(s1)):
                if s1[k] == '?' or s1[k] == s2[i:j][k]:
                    c += 1
            if c == len(s1):
                t = True
                break
    if t:
        print(i+1)
        break
