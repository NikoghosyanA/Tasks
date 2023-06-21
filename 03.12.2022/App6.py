l, v, r, s = input(), int(input()), input(), int(input())
if v <= s:
    l1 = l[:v+1] + r + l[v+1:s+1] + '78' + l[s+1:]
else:
    l1 = l[:s + 1] + '78' + l[s + 1:v + 1] + r + l[v + 1:]
print(l, l1)
