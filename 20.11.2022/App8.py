k = int(input())
s = input()
lt = ''
for i in s:
    c = 0
    for j in s:
        if i == j:
            c += 1
    if c == k:
        lt = i
s.replace(lt, '')
print(s[:10])
