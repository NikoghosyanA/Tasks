lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst1, lst2 = [], []
for i in set(lst):
    if i % 7 == 0:
        lst1.append(str(i))
    if (i + 1) % 7 == 0:
        lst2.append(str(i))
print(f'Густая темнота ({"; ".join(lst1)})')
print(f'Плотная темнота ({"; ".join(lst2)})')
