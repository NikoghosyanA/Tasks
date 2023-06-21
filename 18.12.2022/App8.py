from random import randint, seed
from time import time

minn = 100000000
maxx = 0
summ = 0

seed(time())
for _ in range(10):
    attempts = ''
    while 1:
        attempts += ('P', 'O')[randint(0, 1)]
        if len(attempts) > 2:
            if attempts[len(attempts) - 3:] in ('OOO', 'PPP'):
                break
    for c in attempts:
        print(c, end=' ')
    print('(popitok: %d)\n' % len(attempts))

    if len(attempts) < minn:
        minn = len(attempts)
    if len(attempts) > maxx:
        maxx = len(attempts)
    summ += len(attempts)

print('max: ', maxx)
print('min: ', minn)
print('avg: ', summ / 10)
