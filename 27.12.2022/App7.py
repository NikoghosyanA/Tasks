paths = []
while True:
    s = input()
    if s == '':
        break
    paths.append(s)
n = int(input())
speed = []
for i in range(n):
    speed.append(float(input()))
dct = {}
for i in paths:
    mx = -1
    for j in speed:
        if int(max(str(j))) <= len(i):
            if j > mx:
                mx = j
    if mx != -1:
        dct[i.upper()] = mx


