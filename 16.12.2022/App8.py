from itertools import combinations_with_replacement

comb = combinations_with_replacement(list('0123456789'), 6)
c = 0
for i in list(comb):
    if i.count('3') < 3:
        c += 1
print(c)
