arr = input()
d = ""
c = ""
s = []
for j in range(len(arr)):
    i = arr[j]
    m = 0
    if i == ">" and "<" in c:
        s.append(c[:-1])
        c = c[-1]
        c += i
        m = 1
    if j == len(arr) - 1:
        c += i
        s.append(c)
    if d == ">" and i == "<":
        d = i
        s.append(c)
        c = i
    elif  d == "-" and i == "<":
        d = i
        s.append(c)
        c = i
    elif d == ">" and i == "-":
        d = i
        s.append(c)
        c = i
    else:
        if m == 0:
            d = str(i)
            c += str(i)
for i in s:
    print(i)
