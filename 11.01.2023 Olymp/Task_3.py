h, w, k = 0, 0, 0
lst = []
allsh = 0
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        if i == 0:
            h, w, k = map(int, line.split())
        else:
            lst1 = []
            for j in line:
                if j == '.':
                    lst1.append(0)
                else:
                    allsh += 1
                    lst1.append(1)
            lst.append(lst1)

listed = []
lst_ans = []
ans = 0
goals = []
exp = []
lsst = []
ii, jj = 0, 0
start, start1 = True, False
c = [-10, -3, -2, -1]
while True:
    if ii == h - 1 and jj == w - 1:
        break
    if c[-1] == c[-2]:
        lst_ans.append(c[-1])
        listed.append(goals)
        goals.clear()
        start1 = False
        start = True
    while start:
        while True:
            if ii in range(h) and jj in range(w):
                if lst[ii][jj] == 1 and (ii, jj) not in exp:
                    goals.append((ii, jj))
                    exp.append((ii, jj))
                    lsst = []
                    start = False
                    break
            if ii == h - 1 and jj == w - 1:
                start = False
                break
            jj += 1
            if jj == w:
                ii += 1
                jj = 0
    if goals:
        start1 = True
    elif c[-1] == c[-2]:
        c = [10, -3, -2, -1]
        goals.clear()
        start1 = False
        start = True
    while start1:
        t = False
        for i in range(len(goals)):
            for i1 in range(-1, 2):
                for j1 in range(-1, 2):
                    if goals[i][0] + i1 == goals[i][0] and goals[i][1] + j1 != goals[i][1]:
                        if goals[i][0] + i1 in range(h) and goals[i][1] + j1 in range(w):
                            if lst[goals[i][0] + i1][goals[i][1] + j1] == 1 and (
                                    goals[i][0] + i1, goals[i][1] + j1) not in goals and (
                                    goals[i][0] + i1, goals[i][1] + j1) not in exp \
                                    and (goals[i][0] + i1, goals[i][1] + j1) not in lsst:
                                goals.append((goals[i][0] + i1, goals[i][1] + j1))
                                if len(goals) == k:
                                    lsst.append((goals[i][0] + i1, goals[i][1] + j1))
                                    ans += 1
                                    goals.pop(-1)
                                    t = True
                                    break
                    elif goals[i][0] + i1 != goals[i][0] and goals[i][1] + j1 == goals[i][1]:
                        if goals[i][0] + i1 in range(h) and goals[i][1] + j1 in range(w):
                            if lst[goals[i][0] + i1][goals[i][1] + j1] == 1 and (
                                    goals[i][0] + i1, goals[i][1] + j1) not in goals and (
                                    goals[i][0] + i1, goals[i][1] + j1) not in exp and \
                                    (goals[i][0] + i1, goals[i][1] + j1) not in lsst:
                                goals.append((goals[i][0] + i1, goals[i][1] + j1))
                                if len(goals) == k:
                                    lsst.append((goals[i][0] + i1, goals[i][1] + j1))
                                    ans += 1
                                    goals.pop(-1)
                                    t = True
                                    break
                if t:
                    break
            if t:
                break
        c.append(len(goals))
        if not t:
            break
print(ans)
