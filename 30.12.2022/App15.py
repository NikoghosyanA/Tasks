import random

lst1, lst2 = [], []
for i in range(20):
    lst1.append(round(random.uniform(5, 10), 2))
    lst2.append(round(random.uniform(5, 10), 2))
print(lst1)
print(lst2)
lst3 = []
for i in range(20):
    if lst1[i] > lst2[i]:
        lst3.append(lst1[i])
    else:
        lst3.append(lst2[i])
print(lst3)
