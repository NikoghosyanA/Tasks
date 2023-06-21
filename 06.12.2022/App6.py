t = int(input())
for _ in range(t):
    k = int(input())
    n = input()
    if len(n) >= 2:
        r = 1
    else:
        r = 1
    c = 0
    a = False
    for q in range(len(n)):
        for i in range(len(n)):
            for j in range(len(n) + 1):
                if j - i == r:
                    s1 = n[:i] + n[j:]
                    if len(s1) == 0:
                        a = True
                        print(-1)
                        print(-1)
                        break
                    n1 = int(s1)
                    for d in range(2, n1):
                        if n1 % d == 0:
                            c += 1
                    if c >= 1:
                        print(len(s1))
                        print(int(s1))
                        a = True
                        break
                if a:
                    break
            if a:
                break
        if a:
            c = 0
            break
        r += 1
