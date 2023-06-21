n = int(input())
s1, s2 = input(), input()
s = ''
for i in range(n):
    if s1[i] == '0' and s2[i] == '1':
        s += '1'
    else:
        s += '0'
print(s)
