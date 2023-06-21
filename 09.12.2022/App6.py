import random
n = random.randint(6, 30)
s = ''
sm = 0
c = 0
for i in range(1, n):
    if n % i == 0:
        if c == 0:
            s += f'{i}'
            c += 1
        else:
            s += f'+{i}'
        sm += i
    if i == n-1:
        s += f'={sm}'
if sm == n:
    print(f'Число {n} является совершенным')
else:
    print(f'Число {n} не является совершенным')
print(s)
