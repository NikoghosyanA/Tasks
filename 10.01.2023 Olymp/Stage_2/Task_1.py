n = int(input())
n1 = str(n)
k = 0
for i in range(1, len(n1)+1):
    if n1[-i] == '0':
        k -= 1
    else:
        break
for i in range(len(n1)):
    if n1[i] == '0':
        k += 1
print(k)
