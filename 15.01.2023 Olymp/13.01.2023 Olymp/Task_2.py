n = int(input())
rule = []
for i in range(n):
    rule.append(list(map(str, input().split())))
q = int(input())
loops, complexes = [], []
keyw = []
ans = []
for i in range(q):
    req = input()
    if req[0] == '+':
        rule.append(list(map(str, req[2:].split())))
        for i1 in range(len(rule)):
            for j in range(len(rule)):
                if j > i1:
                    if rule[i1] == rule[j][::-1]:
                        if rule[i1][0] not in loops:
                            loops.append(rule[i1][0])
                        if rule[i1][2] not in loops:
                            loops.append(rule[i1][2])
                    if rule[i1][0] not in keyw:
                        keyw.append(rule[i1][0])
                    if rule[i1][2] not in keyw:
                        keyw.append(rule[i1][2])
        for i2 in range(len(rule)):
            for j in range(len(rule)):
                if j > i2:
                    if rule[i2][0] == rule[j][0] and rule[i2][2] != rule[j][2]:
                        if rule[i2][0] not in complexes:
                            complexes.append(rule[i2][0])
                    if rule[i2][0] not in keyw:
                        keyw.append(rule[i2][0])
                    if rule[i2][2] not in keyw:
                        keyw.append(rule[i2][2])
    elif req[0] == '?':
        if req[2:] not in loops and req[2:] not in complexes:
            for k in rule:
                if req[2:] == k[0]:
                    ans.append(k[2])
                    break
        elif req[2:] in loops and req[2:] not in complexes:
            ans.append('INFINITE LOOP')
        elif req[2:] in complexes:
            ans.append('TOO COMPLEX')
        if req[2:] not in keyw:
            ans.append(req[2:])
for w in ans:
    print(w)
