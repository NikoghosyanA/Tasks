sm = 0
mx = 0
c = 0
while True:
    a = int(input())
    sm += a
    if str(a)[-1] == '5' or str(a)[-1] == '7':
        c += 1
    if sm > 10000:
        print((c / 4) / 2)
        print(mx ** 2)
        break
