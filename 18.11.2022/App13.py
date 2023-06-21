s = ''
k = int(input())
for i in range(10, 100):
    s += str(i)
    if len(s) >= k:
        break
print(s[k-1])
