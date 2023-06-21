k = 1
s = 10
s1 = s
p = float(input())
while True:
    if s > 200:
        print(k)
        print(s)
        break
    s1 = s1 + (s1 * (p/100))
    k += 1
    s += s1
