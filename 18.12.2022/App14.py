lst = []
with open('input.csv', 'r') as f:
    for i in f:
        lst = list(map(int, i.split()))
sr = sum(lst) / len(lst)
lst1 = []
for i in lst:
    if i > sr:
        lst1.append(i)
with open('output.txt', 'w') as f:
    f.write(' '.join(lst[::-1]))
