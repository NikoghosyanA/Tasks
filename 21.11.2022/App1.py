import numpy as np

n = 8
lst = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    s = 8 * i
    for j in range(n):
        if i % 2 == 0:
            lst[j][i] = s + j
        else:
            lst[-j-1][i] = s + j

for line in lst:  # 1 variant
    print(line)
lst1 = np.rot90(lst, k=3)
print()
for line in lst1:  # 2 variant
    print(line)
