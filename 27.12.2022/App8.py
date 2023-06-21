s = ''
n = int(input())
lst = []
for i in range(n+1):
    lst.append(int(input()))
lst = lst[::-1]
for k, i in enumerate(lst):
    print(k, i, s)
    if k == 0:
        if i == 0:
            continue
        elif i == 1:
            s = ' + 1' + s
        elif i == -1:
            s = ' - 1' + s
        elif i > 0:
            s = f' + {i}' + s
        elif i < 0:
            s = f' - {i}' + s
    elif k == 1:
        if i == 0:
            continue
        elif i == 1:
            s = f' + x' + s
        elif i == -1:
            s = f' - x' + s
        elif i > 0:
            s = f' + {i}x' + s
        elif i < 0:
            s = f' - {i}x' + s
    else:
        if i == 0:
            continue
        elif i == 1:
            s = f' + x^{k}' + s
        elif i == -1:
            s = f' - x^{k}' + s
        elif i > 0:
            s = f' + {i}x^{k}' + s
        elif i < 0:
            s = f' - {i}x^{k}' + s
if s[:3] == ' + ' or s[:3] == ' - ':
    s = s[3:]
print(s)

