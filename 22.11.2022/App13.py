n = int(input())
summ = 0
for i in range(n):
    if n % i == 0:
        summ += i
if summ == n:
    print('Число совершенное')
else:
    print('Число несовершенное')
