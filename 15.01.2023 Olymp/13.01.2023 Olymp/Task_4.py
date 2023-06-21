from copy import deepcopy

s = input()
lst = [list(map(str, s[:(len(s) + 1) // 3].split())),
       list(map(str, s[((len(s) + 1) // 3):((len(s) + 1) // 3) * 2].split())),
       list(map(str, s[((len(s) + 1) // 3) * 2:].split()))]
lst1 = deepcopy(lst)
lst2 = [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]
c = 0
ans = ''
while lst[2][2] != '*':
    c += 1
    t = False
    for i in range(3):
        for j in range(3):
            if lst1[i][j] == '*':
                for i1 in range(-1, 2):
                    for j1 in range(-1, 2):
                        if i + i1 in range(3) and j + j1 in range(3):
                            lst1[i][j], lst1[i+i1][j+j1] = lst1[i+i1][j+j1], lst1[i][j]
                            if lst1[i][j] == lst2[i][j]:
                                lst[i][j], lst[i+i1][j+j1] = lst[i+i1][j+j1], lst[i][j]
                                if i == i + i1 and j + j1 > j:
                                    ans += 'R'
                                elif i == i + i1 and j + j1 < j:
                                    ans += 'L'
                                elif j == j + j1 and i + i1 > i:
                                    ans += 'D'
                                elif j == j + j1 and i + i1 < i:
                                    ans += 'U'
                                lst1 = deepcopy(lst)
                                t = True
                            else:
                                lst1 = deepcopy(lst)
                            if t:
                                lst1 = deepcopy(lst)
                                break
                    if t:
                        break
            if t:
                break
        if t:
            break
print(ans)
