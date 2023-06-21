from itertools import combinations_with_replacement

s = int(input())
q = [1, 2, 3]
weight = [1, 1, 2]
m = [[0, 5, 15, 18],
     [0, 3, 6, 14],
     [0, 6, 10, 22]]
ans1, ans2 = 0, ()
for k in range(s):
    c1 = combinations_with_replacement(weight, k)
    c2 = combinations_with_replacement(q, k)
    c1, c2 = list(c1), list(c2)
    for i in range(len(list(c1))):
        if sum(c1[i]) == s:
            sm = 0
            for j in set(c2[i]):
                sm += m[j-1][c2[i].count(j)]
            if sm > ans1:
                ans1 = sm
                ans2 = c2[i]
print(f'1 тип контейнера - {ans2.count(1)}\n'
      f'2 тип контейнера - {ans2.count(2)}\n'
      f'3 тип контейнера - {ans2.count(3)}\n'
      f'Суммарная ценность = {ans1}')
