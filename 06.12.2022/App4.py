ccol = int(input())
s = input()
columns = list(map(int, s.split()))
res = 0
for i in range(0, ccol):
    res |= 2**(columns[i]-1)
print(res)
