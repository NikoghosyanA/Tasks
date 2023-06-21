f = open('17.txt', 'r')
lst = []
for line in f:
    lst = list(map(int, line.split()))


def numbertobase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


lst1 = []
for i in lst:
    if numbertobase(i, 5)[-1] == numbertobase(i, 9)[-1] and (i % 5 == 0 or i % 9 == 0):
        lst1.append(i)
print(len(lst1), min(lst1))
