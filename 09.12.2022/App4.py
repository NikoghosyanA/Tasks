f = open('17.txt', 'r')
lst = []
for line in f:
    lst = list(map(int, line.split()))
lst1 = []
for i in lst:
    if i % 2 == 0:
        lst1.append(i)
sr = sum(lst1) / len(lst1)
c = 0
mx = 0
for i in range(len(lst)):
    if i >= 2:
        a, b, c = lst[i-2], lst[i-1], lst[i]
        if ((a > sr and b > sr) or (a > sr and c > sr) or (b > sr and c > sr)) and (a % 5 == 0 or b % 5 == 0 or c % 5 == 0):
            c += 1
            if a + b + c > mx:
                mx = a + b + c
print(c, mx)
