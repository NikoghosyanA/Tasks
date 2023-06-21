text = input()
w = input()
t, i1 = False, -1
for i in range(len(text)):
    for j in range(len(text) + 1):
        if j - i == len(w):
            if text[i:j].lower() == w.lower():
                t = True
                i1 = i
    if t:
        print('YES', i1)
        break
else:
    print('NO')
