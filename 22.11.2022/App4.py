lst = [9, 19, -20, 15, -14, 2, -3, -14]
#1
osum = 0
for i in lst:
    if i < 0:
        osum += i
print(osum)
#2
sum_nechet = 0
for i in range(len(lst)):
    if i % 2 == 1:
        sum_nechet += lst[i]
print(sum_nechet)
#3
prod_chet = 1
for i in range(len(lst)):
    if i % 2 == 0:
        prod_chet *= lst[i]
print(prod_chet)
#4
A = [-13, 5, 12, 4, 17, 20, -10, 16]
c, psum = 0, 0
for i in A:
    if i > 0:
        psum += i
        c += 1
print(psum, c)
#5
mx = max(lst)
mcount = 0
for i in lst:
    if abs(i) > mx:
        mcount += 1
print(mcount)
#6
mas = list(map(int, input('Введите числа через пробел: ').split()))
c_chet = 0
for i in mas:
    if i % 2 == 0:
        c_chet += 1
if c_chet > 5:
    print('Кол-во четных не может быть больше 10')
else:
    i = 0
    for j in range(10):
        if mas[j] % 2 == 1:
            mas[j] = mas[j] * 2
            i += 1
        if i == c_chet:
            break
print(mas)
#7
minn, maxx = int(input()), int(input())
for i in range(len(lst)):
    if minn <= lst[i] <= maxx:
        print('index', i)
#8
N = int(input())
AA = list(map(int, input().split()))
sr = sum(AA) / len(AA)
count = 0
for i in AA:
    if i > sr:
        count += 1
print(count)
