l, r = int(input()), int(input())
s = 'Hello,world!'
if r > len(s):
    s = ((r // len(s)) + 1) * s
print(s)
print(s[l-1:r])
