_, r, c, n, t = input(), input(), 0, -1, set()
while n and r not in t:
    t.add(r)
    n = r.count('><')
    r = r.replace('><', '<>')
    c += n
print(-1 if n else c)
