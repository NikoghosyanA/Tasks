s1 = int(input())
k = int(input())
s4 = 0
s16 = 0
if s1 >= 3:
    s4 = s1 // 3
    s1 = s1 - s4 * 3
    if s4 >= 3:
        s16 = s4 // 3
        s4 = s4 - s16 * 3
s = 0
while True:
    if s16 > 0:
        s16 -= 1
        s += 16
    elif s4 > 0:
        s4 -= 1
        s += 4
    elif s1 > 0:
        s1 -= 1
        s += 1
    k -= 1
    if k == 0:
        print(s)
        break
