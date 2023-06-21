h, w, k = 0, 0, 0
lst = []
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
                    lst1.append(1)
            lst.append(lst1)


ans = 0
goals = []
exp = []
ii, jj = 0, 0
start, start1 = True, False
c1 = 0
c = [10, -3, -2, -1]
while True:
    if c[-1] == c[-2]:
        if ii == h-1 and jj == w-1:
            break
        if len(goals) >= k:
            ans += 1
            ans += len(goals) - k
        goals.clear()
        start1 = False
        start = True
    while start:
        while True:
            if ii in range(h) and jj in range(w):
                if lst[ii][jj] == 1 and (ii, jj) not in exp:
                    goals.append((ii, jj))
                    exp.append((ii, jj))
                    c1 += 1
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
        for i in range(len(goals)):
            for i1 in range(-1, 2):
                for j1 in range(-1, 2):
                    if goals[i][0] + i1 == goals[i][0] and goals[i][1] + j1 != goals[i][1]:
                        if goals[i][0] + i1 in range(h) and goals[i][1] + j1 in range(w):
                            if lst[goals[i][0] + i1][goals[i][1] + j1] == 1 and (goals[i][0] + i1, goals[i][1] + j1) not in goals and (goals[i][0] + i1, goals[i][1] + j1) not in exp:
                                goals.append((goals[i][0] + i1, goals[i][1] + j1))
                    elif goals[i][0] + i1 != goals[i][0] and goals[i][1] + j1 == goals[i][1]:
                        if goals[i][0] + i1 in range(h) and goals[i][1] + j1 in range(w):
                            if lst[goals[i][0] + i1][goals[i][1] + j1] == 1 and (goals[i][0] + i1, goals[i][1] + j1) not in goals and (goals[i][0] + i1, goals[i][1] + j1) not in exp:
                                goals.append((goals[i][0] + i1, goals[i][1] + j1))
        c.append(len(goals))
        print(c, 11111)
        break
    print(goals, 777777)
print(ans)
