s = input()
c = 0
for i in s:
    if i == i.capitalize():
        print(i)
        c += 1
if c == 0:
    print(-1)
